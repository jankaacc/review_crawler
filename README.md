# Review crawler

This is developer environment for \
PokemonGO Google App store review crawler.


## Getting started


To Run app in review_crawler folder

```
docker-compose up
```

To Run tests in review_crawler folder

```
docker-compose run --rm backend ./docker/run-tests.sh
```

## Admin 

To create admin user run:

```
docker-compose run --rm backend python manage.py createsuperuser
```

You can find admin panel under:

```
localhost:5000/backend/admin
```
You can find there Reviews which were downloaded from Google App store.
Those reviews are downloaded by periodic task defined in backend app.
You cen run this task manually using action in `Periodic tasks` section. 
This should download latest reviews to the database.
