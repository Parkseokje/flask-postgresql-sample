
```bash
$ export FLASK_ENV=development
$ export FLASK_APP=flask_postgresql_sample/__init__.py
$ poetry run flask run # flask run
$ poetry run flask db init 
$ poetry run flask db migrate
$ poetry run flask shell
```

### Migrate

```
$ poetry run flask db stamp head # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
$ poetry run flask db migrate # To detect automatically all the changes.
$ poetry run flask db upgrade # To apply all the changes.
```

## 도움말

- https://wikidocs.net/book/4542
- https://blog.gyus.me/2020/introduce-poetry/
- https://velog.io/@sangmin7648/%EC%98%A4%EB%8A%98%EC%9D%98-%EB%B0%B0%EC%9B%80-035
- https://newbedev.com/sqlalchemy-cascade-delete
- https://medium.com/analytics-vidhya/building-rest-apis-using-flask-restplus-sqlalchemy-marshmallow-cff76b202bfb
- https://pythonspeed.com/articles/pipenv-docker/