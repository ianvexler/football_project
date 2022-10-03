import numpy as np 
import json

from competition_factory import Competition_factory
from competition import Competition

competitions = []

# Function that loads the dataset
def load_data():
    with open("test.json") as json_file:
        json_data = json.load(json_file)

    return json_data

# Method that uses competition_factory to add new competitions
def new_competition(competition_id, competition_name, competition_gender, 
        competition_international, country_name):

    # Uses competition_factory class to create a new competition object
    return Competition_factory.create_competition(competition_id, competition_name, competition_gender, 
        competition_international, country_name)


# Method that loads all competition and adds them to the list
def load_competitions(data):
    in_data = False
    x = 0

    # For loop to load competitions in the dataset and add them to the list
    for d in data:

        if len(competitions) != 0:
            for c in competitions:
                if d["competition_id"] == c.get_competition_id():
                    # Variable to check if competition is already in the list
                    in_data = True

        if in_data == False:
            competitions.append(new_competition(d["competition_id"], d["competition_name"], 
                d["competition_gender"], d["competition_international"], d["country_name"]))
        
        # Sets in_data to false to check if the next competition is in the list
        in_data = False

# Main method
def main():
    data = load_data()
    load_competitions(data)

if __name__ == "__main__":
    main()