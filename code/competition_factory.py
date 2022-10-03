from competition import Competition

class Competition_factory:

    @staticmethod
    def create_competition(competition_id, competition_name, competition_gender, competition_international, country_name):
        return Competition(competition_id, competition_name, competition_gender, competition_international, country_name)
