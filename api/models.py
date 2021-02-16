from api import db

class CovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date, unique=True)
    cases = db.Column(db.Integer)
    tests = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    vaccinations = db.Column(db.Integer)

    def __init__(self, country='Greece', date, cases, tests, deaths, vaccinations):

        self.country = country
        self.date = date
        self.cases = cases
        self.tests = tests
        self.deaths = deaths
        self.vaccinations = vaccinations
        
class SumCovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country='Greece', date, total_cases, total_deaths, 
        people_fully_vaccinated, population):

        self.country = country
        self.date = date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population

class SumCovidWorldModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country='World', date, total_cases, total_deaths, 
        people_fully_vaccinated, population):
        
        self.country = country
        self.date = date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population

class SumCovidCountryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country, date, total_cases, total_deaths, 
        people_fully_vaccinated, population):
        
        self.country = country
        self.date = date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population
