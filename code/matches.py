class Matches:
    def __init__(self, match_id, competition, season, match_date, 
        kick_off, stadium, home_team, away_team, home_score, away_score, 
        match_status, match_week, competition_stage):

        self.match_id = match_id
        self.competition = competition
        self.season = season
        self.match_date = match_date
        self.kick_off = kick_off
        self.stadium = stadium
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.match_status = match_status
        self.match_week = match_week
        self.competition_stage = competition_stage

    def get_competition_id(self):
        return self.match_id