import requests
import pytest
import re
from jsonschema import validate

BASE_URL = "https://swapi.dev/api"

# Schema definitions
all_films_schema = {
    "type": "object",
    "properties": {
        "count": {"type": "number"},
        "next": {},
        "previous": {},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "episode_id": {"type": "number"},
                    "opening_crawl": {"type": "string"},
                    "director": {"type": "string"},
                    "producer": {"type": "string"},
                    "release_date": {"type": "string"},
                    "characters": {"type": "array", "items": {"type": "string"}},
                    "planets": {"type": "array", "items": {"type": "string"}},
                    "starships": {"type": "array", "items": {"type": "string"}},
                    "vehicles": {"type": "array", "items": {"type": "string"}},
                    "species": {"type": "array", "items": {"type": "string"}},
                    "created": {"type": "string"},
                    "edited": {"type": "string"},
                    "url": {"type": "string"}
                },
                "required": ["title", "episode_id", "opening_crawl", "director", "producer", "release_date", "characters", "planets", "starships", "vehicles", "species", "created", "edited", "url"]
            }
        }
    },
    "required": ["count", "next", "previous", "results"],
    "additionalProperties": False
}

specific_film_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "episode_id": {"type": "number"},
        "opening_crawl": {"type": "string"},
        "director": {"type": "string"},
        "producer": {"type": "string"},
        "release_date": {"type": "string"},
        "characters": {"type": "array", "items": {"type": "string"}},
        "planets": {"type": "array", "items": {"type": "string"}},
        "starships": {"type": "array", "items": {"type": "string"}},
        "vehicles": {"type": "array", "items": {"type": "string"}},
        "species": {"type": "array", "items": {"type": "string"}},
        "created": {"type": "string"},
        "edited": {"type": "string"},
        "url": {"type": "string"}
    },
    "required": ["title", "episode_id", "opening_crawl", "director", "producer", "release_date", "characters", "planets", "starships", "vehicles", "species", "created", "edited", "url"],
    "additionalProperties": False
}

def test_get_all_films():
    response = requests.get(f"{BASE_URL}/films")
    
    # Test 1: Validate response status (200) for all films
    assert response.status_code == 200
    
    # Test 2: Validate response body json schema
    validate(instance=response.json(), schema=all_films_schema)
    
    # Test 3: Validate response time (1500ms)
    assert response.elapsed.total_seconds() * 1000 < 1500
    
    json_data = response.json()
    
    # Test 4: Validate 'count' response property matches the number of 'results' property
    assert len(json_data["results"]) == json_data["count"]
    
    # Test 5: Validate each film in the 'results' property contains correct properties
    required_props = ['title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'species', 'starships', 'vehicles', 'characters', 'planets', 'url', 'created', 'edited']
    for film in json_data["results"]:
        assert all(prop in film for prop in required_props)
    
    # Test 6: Validate date formats in response
    date_format_regex = r'^\d{4}-\d{2}-\d{2}$'
    date_time_format_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$'
    
    for film in json_data["results"]:
        assert re.match(date_format_regex, film["release_date"])
        assert re.match(date_time_format_regex, film["created"])
        assert re.match(date_time_format_regex, film["edited"])

def test_get_specific_film():
    film_id = 1  # You can parameterize this
    response = requests.get(f"{BASE_URL}/films/{film_id}/")
    
    # Test 9: Validate response status (200) for individual film
    assert response.status_code == 200
    
    # Test 10: Validate response body json schema
    validate(instance=response.json(), schema=specific_film_schema)
    
    # Test 11: Validate response time (1500ms)
    assert response.elapsed.total_seconds() * 1000 < 1500
    
    json_data = response.json()
    
    # Test 12: Validate the response body contains correct properties
    required_props = ['title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'species', 'starships', 'vehicles', 'characters', 'planets', 'url', 'created', 'edited']
    assert all(prop in json_data for prop in required_props)
    
    # Test 13: Validate the date format in response body properties
    date_format_regex = r'^\d{4}-\d{2}-\d{2}$'
    date_time_format_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$'
    
    assert re.match(date_format_regex, json_data["release_date"])
    assert re.match(date_time_format_regex, json_data["created"])
    assert re.match(date_time_format_regex, json_data["edited"])
    
    # Test 14: Validate the url format in response body results properties
    url_regex = r'^https://swapi\.dev/api/.+/\d+/?$'
    array_props = ['characters', 'planets', 'starships', 'vehicles', 'species']
    for prop in array_props:
        assert isinstance(json_data[prop], list)
        for url in json_data[prop]:
            assert re.match(url_regex, url)

def test_get_non_existent_film():
    response = requests.get(f"{BASE_URL}/films/999/")
    
    # Test 15: Validate when [id] is invalid (out of range or random characters)
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()