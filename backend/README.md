# backend



## Getting started

This is backend service used for Pokemon GO crawler Admin.

Build it using `docker-compose build backend`.\
Start it using `docker-compose up backend`.\
Run tests `docker-compose exec ./docker/run-tests.sh`

This service should be placed inside review_crawler.

Service is ran by docker-compose in review_crawler behind nginx proxy.

You can find admin panel under:

```
localhost:5000/backend/admin
```