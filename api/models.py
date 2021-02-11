from api import db

class CovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    cases = db.Column(db.Integer)
    tests = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    vaccinations = db.Column(db.Integer)

    def __init__(self, date, cases, tests, deaths, vaccinations):

        self.date = date
        self.cases = cases
        self.tests = tests
        self.deaths = deaths
        self.vaccinations = vaccinations
class SumCovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_tests = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_tests, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_tests = sum_tests
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidWorldModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_world_cases = db.Column(db.Integer)
    sum_world_deaths = db.Column(db.Integer)
    sum_world_recovered = db.Column(db.Integer)
    sum_world_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_world_cases, sum_world_deaths, sum_world_recovered, 
        sum_world_vaccinations):
        
        self.sum_world_cases = sum_world_cases
        self.sum_world_deaths = sum_world_deaths
        self.sum_world_recovered = sum_world_recovered
        self.sum_world_vaccinations = sum_world_vaccinations

class SumCovidUnitedStatesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidChinaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidFranceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidUnitedKingdomModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidGermanyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidItalyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidRussiaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidJapanModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations

class SumCovidCanadaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sum_cases = db.Column(db.Integer)
    sum_deaths = db.Column(db.Integer)
    sum_recovered = db.Column(db.Integer)
    sum_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        sum_cases, sum_deaths, sum_recovered, sum_vaccinations):

        self.sum_cases = sum_cases
        self.sum_deaths = sum_deaths
        self.sum_recovered = sum_recovered
        self.sum_vaccinations = sum_vaccinations
