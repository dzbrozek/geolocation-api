# geolocation-api

The aim of this project is to build an API that requires JWT authorization. The
application should be able to store geolocation data in the database, based on IP address or URL.
The API should be able to add, delete or provide geolocation data on the base of ip address or URL

[![codecov](https://codecov.io/gh/dzbrozek/geolocation-api/branch/main/graph/badge.svg)](https://codecov.io/gh/dzbrozek/geolocation-api)


### Development

#### Requirements

This app is using Docker so make sure you have both: [Docker](https://docs.docker.com/install/)
and [Docker Compose](https://docs.docker.com/compose/install/)

#### Prepare env variables

Copy env variables from the template

```
cp .env.template .env
```

and add missing variables:

* `DJANGO_IPSTACK_ACCESS_KEY`: To obtain access API visit [https://ipstack.com/signup/free](https://ipstack.com/signup/free)


#### Copy dev settings

```
cp geolocationapi/geolocationapi/settings_dev_template.py geolocationapi/geolocationapi/settings_dev.py
```

#### Bootstrap

To bootstrap the app you have to build the image and bootstrap the environment

```
make build
make bootstrap
```

Once it's done the app should be up app and running. You can verify that visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### Running

Next time you want to start or stop the app use `up` or `down` command.

```
make up
```

```
make down
```

#### Users

Test users created during bootstrapping the project.

| Login    | Password |
|----------|----------|
| demo     | password |

### Tests

To run the tests use `make test` command
