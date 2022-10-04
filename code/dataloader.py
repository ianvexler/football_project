import json

from sqlalchemy import null

from object_factory import Competition_factory
from object_factory import Match_factory
from competition import Competition
from matches import Matches

competitions = []
matches = []
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

    def new_match(self, match_id, competition, country_name, season, match_date, 
        kick_off, stadium, stadium_country, referee_name, home_team, home_team_gender, 
        home_team_manager, home_team_group, home_team_country, away_team, away_team_gender, 
        away_team_manager, away_team_group, away_team_country, home_score, away_score, match_status,
        match_week, competition_stage):

        # Uses competition_factory class to create a new competition object
        return Match_factory.create_match(match_id, competition, country_name, season, match_date, 
        kick_off, stadium, stadium_country, referee_name, home_team, home_team_gender, 
        home_team_manager, home_team_group, home_team_country, away_team, away_team_gender, 
        away_team_manager, away_team_group, away_team_country, home_score, away_score, match_status,
        match_week, competition_stage)

    def load_matches(self, data):
        for d in data:
            for m in matches:
                matches.append(self.new_match(d["match_id"], d["competition"], d["country_name"], 
                    d["season"], d["match_date"], d["kick_off"] , d["stadium"], d["stadium_country"],
                    d["referee_name"], d["home_team"], d["home_team_gender"], d["home_team_manager"],
                    d["home_team_group"], d["home_team_country"], d["away_team"], d["away_team_gender"], 
                    d["away_team_manager"], d["away_team_group"], d["away_team_country"], d["home_score"], 
                    d["away_score"], d["match_status"], d["match_week"], d["competition_stage"]))


    def load_match(self, competition_id, match_id):
            # This will open a specific match file depending on the match_id
            with open("/Users/ianvexler/Documents/Archivos Ian/Projects/open-data/data/matches/" 
                + str(competition_id) + "/" + str(match_id) + ".json") as json_file:

                match_json_data = json.load(json_file)

            self.load_matches(match_json_data)
            print(matches)