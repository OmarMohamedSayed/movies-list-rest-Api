import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import setup_db, Movies


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  set up CORS. Allow '*' for origins.
  '''
  CORS(app)

  '''
  set Access-Control-Allow
  '''
  
  @app.route('/movies')
  def get_all_movies():

    """Get all movies with id , title and rating
       or status code 500 due to server error
    """
    
    try:
      movies_query = Movies.query.order_by(Movies.id).all()
      formated_movies = [movie.format() for movie in movies_query]

      return jsonify({
        'success':True,
        'Movies':formated_movies,
        'total_movies': len(formated_movies)
      }),200
    except:
      abort(500)

  @app.route('/movies/<int:id>', methods=['DELETE'])
  def delete_movies(id):
    """Delete movie by id
       or get status code 404 for noy found the item"""
    try:
      movies_query = Movies.query.filter_by(id=id).one_or_none()
      movies_query.delete()

      return jsonify({
        'success':True,
        'deleted_item_id': id,
        'message':'movie deleted'
      }),200
    except:
      abort(404)

  @app.route('/movies' , methods=['POST'])
  def create_question():
    body = request.get_json()
    

    title = body.get('title', '')
    rating = body.get('rating', '')
    
    if ((title == '') or (rating == '')):
      abort(422)

    try:
      movie_insert = Movies(title=title , rating=rating)
      movie_insert.insert()
      
      return jsonify({
      'success':True,
      'inserted': movie_insert.id,
      'message':'movie created'
      }),201

    except:
      abort(422)


  @app.route('/movies_search', methods=['POST'])
  def search_title():
    """Search movie title and return all movies titles like,
      or status code 422 if nothing in search 
      or status code 404 if not like any movies"""

    body = request.get_json()
    search = body.get('searchTerm', '')
    
    if search == '':
      abort(422)
    print(search)
    try:
      search_result = Movies.query.order_by(Movies.id).filter(Movies.title.ilike('%{}%'.format(search))).all()
      
      if len(search_result) == 0:
        abort(404)

      
      return jsonify({
        'success':True,
        'movies':[movie.format() for movie in search_result],
        'total_questions':len(search_result)
      }),200

    except:
      abort(404)


  
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad Request"
      }), 400


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


  @app.errorhandler(422)
  def unprocessable_entity(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Unprocessable"
      }), 422

  @app.errorhandler(500)
  def unprocessable_entity(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message": "server error"
      }), 422

  return app

