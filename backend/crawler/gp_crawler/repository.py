from typing import List

from celery.utils.log import get_task_logger
from google_play_scraper import Sort, reviews

from crawler.gp_crawler.consts import Apps
from crawler.gp_crawler.data_getters import ReviewData

logger = get_task_logger(__name__)


class GPCrawlerRepository:
    def get_first_n_pages(
        self, pages: int, app: Apps, page_size: int
    ) -> List[dict]:
        logger.info("Fetching reviews pages.")

        page = 1
        result, continuation_token = reviews(
            app, sort=Sort.NEWEST, count=page_size
        )
        yield result

        while continuation_token and page < pages:
            result, continuation_token = reviews(
                app, continuation_token=continuation_token
            )
            page += 1
            yield result

    def get_reviews_data(self, results: List[dict]) -> List[ReviewData]:
        return [
            ReviewData(
                id=result["reviewId"],
                user_name=result["userName"],
                content=result["content"],
                score=result["score"],
            )
            for result in results
        ]
