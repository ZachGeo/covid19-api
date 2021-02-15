from api import db

class CovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date, unique=True)
    cases = db.Column(db.Integer)
    tests = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    vaccinations = db.Column(db.Integer)

    def __init__(self, date, cases, tests, deaths, vaccinations):

        self.country = 'Greece'
        self.date = date
        self.cases = cases
        self.tests = tests
        self.deaths = deaths
        self.vaccinations = vaccinations
        
class SumCovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)
    last_date_modified = db.Column(db.Date)

    def __init__(self, sum_cases, sum_tests, sum_deaths, sum_recovered, 
        sum_vaccinations, last_date_modified):

        self.country = 'Greece'
        self.sum_cases = sum_cases
        self.sum_tests = sum_tests
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations
        self.last_date_modified = last_date_modified

class SumCovidWorldModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    sum_world_cases = db.Column(db.Integer)
    sum_world_deaths = db.Column(db.Integer)
    sum_world_recovered = db.Column(db.Integer)
    sum_world_vaccinations = db.Column(db.Integer)
    last_date_modified = db.Column(db.Date)

    def __init__(self, sum_world_cases, sum_world_deaths, 
        sum_world_recovered, sum_world_vaccinations, last_date_modified):
        
        self.label = 'Worldwide'
        self.sum_world_cases = sum_world_cases
        self.sum_world_deaths = sum_world_deaths
        self.sum_world_recovered = sum_world_recovered
        self.sum_world_vaccinations = sum_world_vaccinations
        self.last_date_modified = last_date_modified

class SumCovidCountryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)
    last_date_modified = db.Column(db.Date)

    def __init__(self, country, sum_cases, sum_deaths, sum_recovered, 
        sum_vaccinations, last_date_modified):

        self.country = country
        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations
        self.last_date_modified = last_date_modified

