from competition import Competition
from matches import Matches

class Competition_factory:
    @staticmethod
    def create_competition(competition_id, competition_name, competition_gender, competition_international, country_name):
        return Competition(competition_id, competition_name, competition_gender, competition_international, country_name)

class Match_factory:
    @staticmethod
    def create_match(match_id, competition, season, match_date, 
        kick_off, stadium, home_team, away_team, home_score, away_score, 
        match_status, match_week, competition_stage):

        return Matches(match_id, competition, season, match_date, 
        kick_off, stadium, home_team, away_team, home_score, away_score, 
        match_status, match_week, competition_stage)