from crawler.gp_crawler.consts import Apps
from crawler.gp_crawler.data_getters import ReviewData
from crawler.gp_crawler.repository import GPCrawlerRepository


def test_get_first_n_pages_stops_when_no_cursor(reviews_mock):
    repository = GPCrawlerRepository()
    res = repository.get_first_n_pages(
        pages=3, page_size=2, app=Apps.POKEMON_GO
    )
    assert len(list(res)) == 2


def test_get_first_n_pages_stops_when_last_page(reviews_mock):
    repository = GPCrawlerRepository()
    res = repository.get_first_n_pages(
        pages=1, page_size=2, app=Apps.POKEMON_GO
    )
    assert len(list(res)) == 1


def test_get_review_data(reviews_mock):
    repository = GPCrawlerRepository()
    data = repository.get_reviews_data(
        [
            {
                "reviewId": "gp_1",
                "userName": "test 1",
                "content": "great review 1",
                "score": 1,
            }
        ]
    )
    assert data == [
        ReviewData(
            id="gp_1",
            user_name="test 1",
            content="great review 1",
            score=1,
        )
    ]
