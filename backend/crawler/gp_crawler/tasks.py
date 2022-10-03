from celery.utils.log import get_task_logger

from crawler import celery_app
from crawler.gp_crawler.consts import Apps
from crawler.gp_crawler.service import GPCrawlerService

logger = get_task_logger(__name__)


@celery_app.task(name="gp_crawler.tasks.fetch_reviews")
def fetch_reviews_task(pages: int, page_size: int):
    logger.info("fetching reviews for Pokemon Go")
    gp_service = GPCrawlerService()
    gp_service.get_newest_reviews(
        app=Apps.POKEMON_GO, pages=pages, page_size=page_size
    )
