#Write a program that adds to a travel log.
#Travel_log already has 2 dicitionaries
#Create a function that takes a country, # of visits, and a list of cities and add them to the exisiting log

travel_log = [
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
]


def add_new_country(country, visits, list_of_cities):
    travel_log.append(
        {
            "country": country, 
            "cities_visited": list_of_cities, 
            "total_visits": visits,
        }
    )

def main():
    countryToAdd = input("Enter in a country you've visited: ")
    
    citiesVisitedToAdd = []

    while(True):
        cityToAddToList = input("Enter in a city: ")
        citiesVisitedToAdd.append(cityToAddToList)

        keepGoing = input("Do you have another city to add?\nType '1' for Yes. Type '0' for No.\n")
        if(keepGoing == "0"):
            break

    totalVisitsToAdd = int(input("Enter total visits: "))

    add_new_country(countryToAdd, totalVisitsToAdd, citiesVisitedToAdd)

    print(f"I've been to {travel_log[2]['country']} {travel_log[2]['total_visits']} times.")
    print(f"My favortite city is {travel_log[2]['cities_visited'][0]}")

if __name__ == "__main__":
    main()