# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

# API END-POINTS

### GET /keywords_main/

Returns all main keywords in the database.

### GET /keywords_modifier/

Returns all modifier keywords in the database.

### GET /get_orders/<id>

Gets all orders for resteraunts with <id>

### PUT /new_order/<id>

Adds new order for user with <id>. Payload must have latitude, longitude, and the id of a keywords group (name=keywords).

### POST /call_uber/

Calls an uber. Pass in slat, slng (starting longitude and latitude), elat, elng.

### PUT /new_keyword/<id>

Makes a new keyword GROUP. Paylod should be keywords as a list of strings.
