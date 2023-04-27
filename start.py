import requests
import json

PORT = 8085

def get_data(api, response_value = []):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            response_json = response.json()
            response_value.extend(response_json["results"])
            if response_json["next"] != None:
                get_data(response_json["next"], response_value)
            return {"data": response_value}
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")


def initialize_database():
    with open("movie.json", "w") as movie_db:
        print("Fetching movie details")
        movie_data = json.dumps(get_data("https://swapi.dev/api/films/", []))
        movie_db.write(movie_data)
        movie_db.close()

    with open("planet.json", "w") as planet_db:
        print("Fetching planet details")
        planet_data = json.dumps(get_data("https://swapi.dev/api/planets/", []))
        planet_db.write(planet_data)
        planet_db.close()
          

if __name__ == "__main__":
    initialize_database()
    from controller.controller import app
    app.run(host='0.0.0.0', port=PORT, threaded=True)
