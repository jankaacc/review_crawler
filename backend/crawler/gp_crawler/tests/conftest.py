from unittest import mock

import pytest

REVIEWS = [
    (
        [
            {
                "reviewId": "gp_1",
                "userName": "test 1",
                "content": "great review 1",
                "score": 1,
            },
            {
                "reviewId": "gp_2",
                "userName": "test 2",
                "content": "great review 2",
                "score": 2,
            },
        ],
        "cursor1",
    ),
    (
        [
            {
                "reviewId": "gp_3",
                "userName": "test 3",
                "content": "great review 3",
                "score": 3,
            },
            {
                "reviewId": "gp_4",
                "userName": "test 4",
                "content": "great review 4",
                "score": 4,
            },
        ],
        None,
    ),
]


@pytest.fixture()
def reviews_mock():
    with mock.patch("crawler.gp_crawler.repository.reviews") as m:
        m.side_effect = REVIEWS
        yield m
