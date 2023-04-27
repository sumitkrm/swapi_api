import json

def fetch_all_planets(user_id, searchTerm = None):
    """
    Fetches all planets
    """
    planet_file_object = open('planet.json')
    planets_list = json.load(planet_file_object)
    searched_planet_list = []
    if searchTerm:
        for planet in planets_list['data']:
            if ("favorite" in planet and user_id in planet["favorite"] and planet["favorite"][user_id]==searchTerm) or planet.get("name") == searchTerm:
                searched_planet_list.append({"name": planet["favorite"][user_id] if "favorite" in planet and user_id in planet["favorite"] else planet.get("name", ""),
                                "created":planet.get("created", ""),
                                "updated":planet.get("edited", ""),
                                "URL":planet.get("url", ""),
                                "is_favourite": True if "favorite" in planet and user_id in planet["favorite"] else False
                })
                break
    else:
        for planet in planets_list['data']:
            searched_planet_list.append({"name": planet["favorite"][user_id] if "favorite" in planet and user_id in planet["favorite"] else planet.get("name", ""),
                                "created":planet.get("created", ""),
                                "updated":planet.get("edited", ""),
                                "URL":planet.get("url", ""),
                                "is_favourite": True if "favorite" in planet and user_id in planet["favorite"] else False
            })
    return searched_planet_list


def add_favorite_planet(user_id, name, custom_name = None):
    with open("./planet.json", "r") as planet_json:
        planet_obj = json.load(planet_json)
        planet_json.close()

    new_planet_list = []
    for planet in planet_obj["data"]:
        if planet.get("name") == name:
            if "favorite" not in planet:
                planet["favorite"] = {}
            planet["favorite"][user_id] = custom_name if custom_name else name
        new_planet_list.append(planet)
    new_planet_obj = json.dumps({"data": new_planet_list})
        
    with open("./planet.json", "w") as planet_json:
        planet_json.write(new_planet_obj)
        planet_json.close()

    return "successfully added planet to favorite"