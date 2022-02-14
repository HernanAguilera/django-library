# Library project

## Run project with docker compose

``` bash
$ docker-compose up
```

Open http://localhost:8000/ in your web browser

### Stop server

For stop server press keys `ctl` + `C`

### Removing container

``` bash
$ docker-compose down
```

## Run project without docker

You need to have installed [python](https://www.python.org/) in your SO

``` bash
$ pip install -r requirements.txt
$ python core/manage.py runserver
```

Open http://localhost:8000/ in your web browser