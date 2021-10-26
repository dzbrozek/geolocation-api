# geolocation-api

The aim of this task is to build an API (backed by any kind of database) that requires JWT authorization. The
application should be able to store geolocation data in the database, based on IP address or URL - you can use
https://ipstack.com/ to get geolocation data (you can obtain free API KEY here -> https://ipstack.com/signup/free).
The API should be able to add, delete or provide geolocation data on the base of ip address or URL.

### Application specification

* It should be a RESTful API
* You can use [https://ipstack.com/](https://ipstack.com/) for the geolocation of IP addresses and URLs
* The back-end part of the application can be built in any framework of your choice
* The application should preferably be hosted and available online (for example on Heroku - [https://www.heroku.com/free](https://www.heroku.com/free))
* Heroku also provides some free DBs so you can use them
* It is preferable that the API operates using JSON (for both input and output)
* You can create a registration form but using hardcoded values for authorisation is also acceptable (just make sure that API is secured by JWT token)
* Specs, serializers and docker are always welcome!

### Notes

* We will run the application on our local machines for testing purposes. This implies that the solution should provide a quick and easy way to get the system up and running, including test data (hint: you can add Docker support so we can run it easily)
* We will test the behavior of the system under various "unfortunate" conditions (hint: How will the app behave when we take down the DB? How about the GeoIP API?)
* After we finish reviewing the solution, we'll invite you to Sofomo's office (or to a Zoom call) for a short discussion about the provided solution. We may also use that as an opportunity to ask questions and drill into the details of your implementation.

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

and add missing variables to `.env`:

* `DJANGO_IPSTACK_ACCESS_KEY`: To obtain access key visit [https://ipstack.com/signup/free](https://ipstack.com/signup/free)


#### Build and bootstrap the app

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

#### API spec

API spec is available under [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/).
