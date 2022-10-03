class Competition:
    # Key is season_id and value is season_name
    competition_seasons = {}
    
    def __init__(self, competition_id, competition_name, competition_gender, competition_international, country_name):
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.competition_gender = competition_gender
        self.competition_international = competition_international
        self.country_name = country_name

    def add_season(season_id, season_name):
        competition_seasons[season_id, season_name]

    def get_competition_id(self):
        return self.competition_id

    def get_competition_name(self):
        return self.competition_name


        
