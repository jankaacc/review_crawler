from celery.utils.log import get_task_logger

from crawler.gp_crawler.consts import Apps
from crawler.gp_crawler.data_getters import ReviewData
from crawler.gp_crawler.models import Review
from crawler.gp_crawler.repository import GPCrawlerRepository

logger = get_task_logger(__name__)


class GPCrawlerService:
    def __init__(self):
        self.repository = GPCrawlerRepository()

    def get_or_create_review(self, review: ReviewData) -> Review:
        obj, created = Review.objects.get_or_create(
            id=review.id,
            defaults={
                "user_name": review.user_name,
                "content": review.content,
                "score": review.score,
            },
        )
        return obj

    def get_newest_reviews(self, app: Apps, pages: int, page_size: int):
        logger.info("Fetching newest reviews from: %s.", app)
        for result in self.repository.get_first_n_pages(
            pages=pages, page_size=page_size, app=app
        ):
            for data in self.repository.get_reviews_data(result):
                self.get_or_create_review(review=data)
