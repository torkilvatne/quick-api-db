# Simple PostgreSQL with Docker

https://towardsdatascience.com/how-to-run-postgresql-using-docker-15bf87b452d4

## Setup of DB

To set up the Docker container, run

```sh
$ docker compose up
```

Then you need to create the DB (username and password is 'root'):

```sh
$ docker exec -it pg_container bash
$ psql -h pg_container -d test_db -U root -f infile
```

To check if database is created properly, run

```sh
$ docker exec -it pg_container bash
$ psql -h pg_container -d test_db -U root
$ \dt
```

If you want to delete the backup volume of the database data, run

```sh
$ docker volume rm postgresql-snippets_pg_data
```

## Setup of API

Install dependencies and run

```sh
$ uvicorn main:app --reload
```
