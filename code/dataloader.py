import os, json
import pandas as pd

from sqlalchemy import null

from object_factory import Competition_factory
from object_factory import Match_factory
from competition import Competition
from matches import Matches

competitions = []
matches = []
event_list = []
json_data = None

class Dataloader:

    # Function that loads the dataset
    def load_data(self, path):
        # This should be replaced with the correct path to json files
        # Loads the competitions.json file
        with open(path) as json_file:
            json_data = json.load(json_file)

        self.load_competitions(json_data)

    # Method that uses competition_factory to add new competitions
    def new_competition(self, competition_id, competition_name, competition_gender, 
            competition_international, country_name):

        # Uses competition_factory class to create a new competition object
        return Competition_factory.create_competition(competition_id, competition_name, competition_gender, 
            competition_international, country_name)


    # Method that loads all competition and adds them to the list
    def load_competitions(self, data):
        in_data = False

        # For loop to load competitions in the dataset and add them to the list
        for d in data:
            if len(competitions) != 0:
                for c in competitions:
                    if d["competition_id"] == c.get_competition_id():
                        # Variable to check if competition is already in the list
                        in_data = True

            if in_data == False:
                competitions.append(self.new_competition(d["competition_id"], d["competition_name"], 
                    d["competition_gender"], d["competition_international"], d["country_name"]))
            
            # Sets in_data to false to check if the next competition is in the list
            in_data = False

    def new_match(self, match_id, competition, season, match_date, 
        kick_off, stadium, home_team, away_team, home_score, away_score, 
        match_status, match_week, competition_stage):

        # Uses competition_factory class to create a new competition object
        return Match_factory.create_match(match_id, competition, season, match_date, 
        kick_off, stadium, home_team, away_team, home_score, away_score, 
        match_status, match_week, competition_stage)

    def load_match(self, competition_id, match_id):
            # This will open a specific match file depending on the match_id
            with open("/Users/ianvexler/Documents/Archivos Ian/Projects/open-data/data/matches/" 
                + str(competition_id) + "/" + str(match_id) + ".json") as json_file:

                match_json_data = json.load(json_file)

            self.load_matches(match_json_data)

    def load_matches(self, data):
        for d in data:
            matches.append(self.new_match(d["match_id"], d["competition"], d["season"], 
                d["match_date"], d["kick_off"] , d["stadium"], d["home_team"], 
                d["away_team"], d["home_score"], d["away_score"], d["match_status"], 
                d["match_week"], d["competition_stage"]))

    def load_events(self):
        json_file_path = "/Users/ianvexler/Documents/Archivos Ian/Projects/open-data/data/events/69242.json"

        with open(json_file_path, 'r') as j:
            events = json.loads(j.read())

        self.load_event_types(events)
        
    def load_event_types(self, events):
        for event in events:
            if "player" in event:
                if (event["type"])["name"] not in event_list:
                    event_list.append((event["type"])["name"])

# Types: ball receipt, ball recovery, dispossessed, duel, block, 
# offside, clearance, interception, dribble, shot, pressure, half start
# substitution, own goal against, foul won, foul committed, goalkeeper,
# bad behaviour, own goal for, player on, player off, shield, pass, 50/50
# hald end*, starting XI, tatical shift, error, miscontrol, dribble past, injury stoppage, referee ball-drop