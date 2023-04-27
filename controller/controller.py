import json

from flask import Flask, request
from service import movies, planets

app = Flask(__name__)

DEFAULT_STATUS_CODE = "failure"
SUCCESS_STATUS_CODE = "success"

@app.route('/')
def health_check():
    return 'Health check'

@app.route('/movies', methods=['GET'])
def get_movies():
    """
    API endpoint for fetching movie/movies
    """
    response = prepare_result_container()
    try:
        user_id = request.get_json().get("user_id", None)
        searchTerm = request.args.get('searchTerm', None)
        if not user_id:
            response["error"] = "Please proviede User Id"
            return json.dumps(response)
        
        if searchTerm:
            searchTerm = str(request.args.get('searchTerm'))
        response["response"] = movies.fetch_all_movies(user_id, searchTerm)
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)
    

@app.route('/movies/add_favorite', methods=['POST'])
def add_movie_favorite():
    """
    API endpoint for adding favorite movie
    """
    response = prepare_result_container()
    try:
        inpReq = request.get_json()
        user_id = inpReq.get("user_id", None)
        title = inpReq.get("title")
        custom_title = inpReq.get("custom_title", "")
        if not user_id:
            response["error"] = "Please proviede User Id"
            return json.dumps(response)
        response["response"] = movies.add_favorite_movie(user_id, title, custom_title)
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)


@app.route('/planets', methods=['GET'])
def get_planets():
    """
    API endpoint for fetching planet/planets
    """
    response = prepare_result_container()
    try:
        user_id = request.get_json().get("user_id", None)
        searchTerm = request.args.get('searchTerm', None)
        if not user_id:
            response["error"] = "Please proviede User Id"
            return json.dumps(response)
        if searchTerm:
            searchTerm = str(request.args.get('searchTerm'))
        response["response"] = planets.fetch_all_planets(user_id, searchTerm)
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)
    

@app.route('/planets/add_favorite', methods=['POST'])
def add_planet_favorite():
    """
    API endpoint for adding favorite planet
    """
    response = prepare_result_container()
    try:
        inpReq = request.get_json()
        user_id = inpReq.get("user_id", None)
        name = inpReq.get("name")
        custom_name = inpReq.get("custom_name", "")
        if not user_id:
            response["error"] = "Please proviede User Id"
            return json.dumps(response)
        response["response"] = planets.add_favorite_planet(user_id, name, custom_name)
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)
    

def prepare_result_container():
    """
    Returns a dict - response
    """
    return {
        "response":{},
        "status":DEFAULT_STATUS_CODE,
        "error": ""
    }
