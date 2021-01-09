# Movies List API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql moviesapp < moviesapp.psql
```

## Running the server

From within the `./back-end` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for movies. This endpoint should return a list of movies, number of total movies. 
3. Create an endpoint to DELETE movie using a movie ID. 
4. Create an endpoint to POST a new movie, which will require the title and rating. 
5. Create a POST endpoint to get movie based on a search term. It should return any movie for whom the search term is a substring of the title. 
6. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/api/v1.0/movies'
POST '/api/v1.0/movies'
POST '/api/v1.0//movies_search'
DELETE '/api/v1.0/movies/<id>'

GET '/api/v1.0/movies'
- Fetches a dictionary of movies in which the keys are the ids , the titles and the ratings
- Request Arguments: None
- Returns: An object with movies. 
{ "Movies": [
    {
      "id": 1, 
      "rating": 4, 
      "title": "Avengers: infinity war"
    }, 
    {
      "id": 2, 
      "rating": 4, 
      "title": "Black Panther"
    }, 
    {
      "id": 10, 
      "rating": 3, 
      "title": "Snow White"
    }
  ], 
  "success": true, 
  "total_movies": 3
}

```

```
