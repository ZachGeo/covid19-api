from api import db

class CovidModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    cases = db.Column(db.String)
    deaths = db.Column(db.String)

    def __init__(self, date, cases, deaths):
        self.date = date
        self.cases = cases
        self.deaths = deaths

class SumCovidModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.String)
    sum_deaths = db.Column(db.String)
    sum_recovered = db.Column(db.String)

    def __init__(self, sum_cases, sum_deaths, sum_recovered):
        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered

class WorldSumCovidModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_world_cases = db.Column(db.String)
    sum_world_deaths = db.Column(db.String)
    sum_world_recovered = db.Column(db.String)

    def __init__(self, sum_world_cases, sum_world_deaths, sum_world_recovered):
        self.sum_world_cases = sum_world_cases
        self.sum_world_deaths = sum_world_deaths
        self.sum_world_recovered = sum_world_recovered
