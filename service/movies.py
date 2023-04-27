import json

def fetch_all_movies(user_id, searchTerm = None):
    """
    Fetches all movies
    """
    movie_file_object = open('movie.json')
    movies_list = json.load(movie_file_object)
    movie_list = []
    if searchTerm:
        for movie in movies_list['data']:
            if ("favorite" in movie and user_id in movie["favorite"] and movie["favorite"][user_id]==searchTerm) or movie.get("title") == searchTerm:
                movie_list.append({"title": movie["favorite"][user_id] if "favorite" in movie and user_id in movie["favorite"] else movie.get("title", ""),
                                "release_date":movie.get("release_date", ""), 
                                "created":movie.get("created", ""),
                                "updated":movie.get("edited", ""),
                                "URL":movie.get("url", ""),
                                "is_favourite": True if "favorite" in movie and user_id in movie["favorite"] else False
                })
                break
    else:
        for movie in movies_list['data']:
            movie_list.append({"title": movie["favorite"][user_id] if "favorite" in movie and user_id in movie["favorite"] else movie.get("title", ""),
                                "release_date":movie.get("release_date", ""), 
                                "created":movie.get("created", ""),
                                "updated":movie.get("edited", ""),
                                "URL":movie.get("url", ""),
                                "is_favourite": True if "favorite" in movie and user_id in movie["favorite"] else False
            })
    return movie_list

def add_favorite_movie(user_id, title, custom_title = None):
    with open("./movie.json", "r") as movie_json:
        movie_obj = json.load(movie_json)
        movie_json.close()

    new_movie_list = []
    for movie in movie_obj["data"]:
        if movie.get("title") == title:
            if "favorite" not in movie:
                movie["favorite"] = {}
            movie["favorite"][user_id] = custom_title if custom_title else title
        new_movie_list.append(movie)
    new_movie_obj = json.dumps({"data": new_movie_list})
        
    with open("./movie.json", "w") as movie_json:
        movie_json.write(new_movie_obj)
        movie_json.close()

    return "successfully added movie to favorite"

