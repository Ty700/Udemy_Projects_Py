#Nesting dicitionary in a dicitionary

travel_log0 = {
    "France": {
        "cities_visited": ["Paris", "Lilie", "Dijon",],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart",],
        "total_visits": 5,
    },
    "United States of America": {
        "states_visited": ["Texas", "New York", "Washington", "Florida",],
        "total_visits": 20,
    }
}

#Nesting dicitionary in a list

travel_log1 = [
    {   
        "country": "France",
        "cities_visited": ["Paris", "Lilie", "Dijon",],
        "total_visits": 12,
    },
    {   
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart",],
        "total_visits": 5,
    },
    {   
        "country": "United States of America",
        "cities_visited": ["Texas", "New York", "Washington", "Florida",],
        "total_visits": 20,
    },
]

for country in travel_log1:
    currentCountry = country["country"]
    print(f"\nCountry: {currentCountry}")

    print(f"\tCities Visited: ", end = "")
    for city in country["cities_visited"]:
        print(f"{city}", end = ", ")
    print()

    