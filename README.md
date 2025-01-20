# flask-api-starter
basic config api template for quick flask api with simple postgres docker env with -- has hot reloading


### Setup
```
$ docker compose build
$ docker compose up flask_app
```

To run commands from the flask_app container (e.g. for migrations) do:
```
$ docker exec flask_app flask db upgrade
$ docker exec flask_app <command>
```
