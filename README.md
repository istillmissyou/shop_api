![Workflow](https://github.com/istillmissyou/test_guru/actions/workflows/test_guru_workflow.yml/badge.svg)

# API shops

## Description

* **GET /api/v1/city/** — getting all cities from the database
* **POST /api/v1/city/** — creating a city
* **GET /api/v1/city/city_id/street/** —  getting all the streets of the city
* **POST /api/v1/city/city_id/street/** —  creating a street in the city
* **POST /api/v1/shop/** —  creating a store; This method receives a json with
a store object, returns the data of the created record in response
* **GET /api/v1/shop/?street=&city=&open=0/1** — getting a list of stores.
I. The method accepts parameters for filtering. Parameters are optional. If there
are no parameters, all stores are displayed, if there is at least one parameter
, then filtering will be performed on it.
II. Important! The name of the city and street is displayed in the object of each store, not the id
of the records.
III. Parameter open: 0 - closed, 1 - open. This status determines the outcome of
the parameters "Opening Time", "Closing Time" and the current server time.

JWT token technology is used
* **POST /api/auth/users/** — creating a user
* **POST /api/auth/jwt/create/** — pass the username and password of the user. In the received token, copy "access" and paste it into Headers where `KEY` add `Authorization`, in the `VALUE` field add `Bearer access`, where access is inserted from the received token. Now you can send requests!

## Technologies

* Python 3.10.6
* Django 4.1.2
* Django Rest Framework 3.14.0
* Simple-JWT 4.8.0
* Gunicorn 20.1.0

## Preparatory actions

Clone a project

```
git clone https://github.com/istillmissyou/shop_api.git
```

Install Docker

```
sudo apt install docker.io
```

```
sudo apt install docker-compose
```


### env file filling template

```
DB_ENGINE=indicate that we are working with postgresql
DB_NAME=database name
POSTGRES_USER=login to connect to the database
POSTGRES_PASSWORD =password to connect to the database (set your own)
DB_HOST=name of the service (container)
DB_PORT=port for connecting to the database
```

### How to launch a project:

Clone the repository and go to the "infra" directory to open the docker-compose file.yaml and in line 11, change `image: ssd256/test_guru` to `build: .` Next on the command line:

``` 
sudo docker-compose up
```

## Author
Danil Shtun
