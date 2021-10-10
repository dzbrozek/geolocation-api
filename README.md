# geolocation-api

The aim of this project is to build an API that requires JWT authorization. The
application should be able to store geolocation data in the database, based on IP address or URL.
The API should be able to add, delete or provide geolocation data on the base of ip address or URL

[![codecov](https://codecov.io/gh/dzbrozek/geolocation-api/branch/main/graph/badge.svg)](https://codecov.io/gh/dzbrozek/geolocation-api)


### Running

#### Requirements

This app is using Docker so make sure you have both: [Docker](https://docs.docker.com/install/)
and [Docker Compose](https://docs.docker.com/compose/install/)

#### Bootstrap

To bootstrap the app move to the app directory and call

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
