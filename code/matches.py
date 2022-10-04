class Matches:
    def __init__(self, match_id, competition, country_name, season, match_date, 
        kick_off, stadium, stadium_country, referee_name, home_team, home_team_gender, 
        home_team_manager, home_team_group, home_team_country, away_team, away_team_gender, 
        away_team_manager, away_team_group, away_team_country, home_score, away_score, match_status,
        match_week, competition_stage):

        self.match_id = match_id
        self.competition = competition
        self.country_name = country_name
        self.season = season
        self.match_date = match_date
        self.kick_off = kick_off
        self.stadium = stadium
        self.stadium_country = stadium_country
        self.referee_name = referee_name
        self.home_team = home_team
        self.home_team_gender = home_team_gender
        self.home_team_manager = home_team_manager
        self.home_team_group = home_team_group
        self.home_team_country = home_team_country
        self.away_team = away_team
        self.away_team_gender = away_team_gender
        self.away_team_manager = away_team_manager
        self.away_team_group = away_team_group
        self.away_team_country = away_team_country
        self.home_score = home_score
        self.away_score = away_score
        self.match_status = match_status
        self.match_week = match_week
        self.competition_stage = competition_stage

    def get_competition_id(self):
        return self.match_id