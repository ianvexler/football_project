from competition import Competition
from matches import Matches

class Competition_factory:
    @staticmethod
    def create_competition(competition_id, competition_name, competition_gender, competition_international, country_name):
        return Competition(competition_id, competition_name, competition_gender, competition_international, country_name)

class Match_factory:
    @staticmethod
    def create_match(match_id, competition, country_name, season, match_date, 
        kick_off, stadium, stadium_country, referee_name, home_team, home_team_gender, 
        home_team_manager, home_team_group, home_team_country, away_team, away_team_gender, 
        away_team_manager, away_team_group, away_team_country, home_score, away_score, match_status,
        match_week, competition_stage):

        return Matches(match_id, competition, country_name, season, match_date, 
        kick_off, stadium, stadium_country, referee_name, home_team, home_team_gender, 
        home_team_manager, home_team_group, home_team_country, away_team, away_team_gender, 
        away_team_manager, away_team_group, away_team_country, home_score, away_score, match_status,
        match_week, competition_stage)