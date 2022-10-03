from crawler.gp_crawler.consts import Apps
from crawler.gp_crawler.models import Review
from crawler.gp_crawler.service import GPCrawlerService


def test_get_newest_reviews_creates_models(db, reviews_mock):
    service = GPCrawlerService()
    service.get_newest_reviews(pages=2, page_size=2, app=Apps.POKEMON_GO)
    assert Review.objects.count() == 4


def test_get_newest_reviews_get_models_when_already_present(
    db, reviews_mock, review_factory
):
    review_factory(id="gp_1")
    service = GPCrawlerService()
    service.get_newest_reviews(pages=2, page_size=2, app=Apps.POKEMON_GO)
    assert Review.objects.count() == 4
