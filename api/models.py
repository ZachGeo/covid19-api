from api import db

class CovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    date = db.Column(db.Date, unique=True)
    new_cases = db.Column(db.Integer)
    new_tests = db.Column(db.Integer)
    new_deaths = db.Column(db.Integer)
    new_vaccinations = db.Column(db.Integer)

    def __init__(self, 
        country, date, new_cases, new_tests, new_deaths, new_vaccinations):

        self.country = country
        self.date = date
        self.new_cases = new_cases
        self.new_tests = new_tests
        self.new_deaths = new_deaths
        self.new_vaccinations = new_vaccinations
        
class SumCovidGreeceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    last_updated_date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country, last_updated_date, total_cases, total_deaths, 
        people_fully_vaccinated, population):

        self.country = country
        self.last_updated_date = last_updated_date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population

class SumCovidWorldModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    last_updated_date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country, last_updated_date, total_cases, total_deaths, 
        people_fully_vaccinated, population):
        
        self.country = country
        self.last_updated_date = last_updated_date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population

class SumCovidCountryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    last_updated_date = db.Column(db.Date)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)
    people_fully_vaccinated = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def __init__(self, country, last_updated_date, total_cases, total_deaths, 
        people_fully_vaccinated, population):
        
        self.country = country
        self.last_updated_date = last_updated_date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.people_fully_vaccinated = people_fully_vaccinated
        self.population = population
