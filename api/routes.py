from flask import request, jsonify
from api import app, db
from api.models import (
    CovidGreeceModel, SumCovidGreeceModel, SumCovidWorldModel, 
    SumCovidCountryModel)
from api.schemas import ( 
    covid_greece_schema, all_covid_greece_schema, sum_covid_greece_schema, 
    sum_covid_world_schema, sum_covid_country_schema, 
    sum_covid_all_countries_schema)

import datetime

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to our \
        <a href="https://github.com/ZachGeo/covidGR_API">Covid19 API</a>.<h1>'

@app.route('/covid19/summary-data/greece', methods=['GET'])
def get_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()

    return sum_covid_greece_schema.jsonify(sum_greece_data)

@app.route('/covid19/summary-data/greece', methods=['POST'])
def add_summary_covid_data_greece():
    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']

    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()

    new_sum_greece_covid = SumCovidGreeceModel(
        country, date_obj, total_cases, total_deaths, people_fully_vaccinated, 
        population)
    
    db.session.add(new_sum_greece_covid)
    db.session.commit()

    return sum_covid_greece_schema.jsonify(new_sum_greece_covid)

@app.route('/covid19/summary-data/greece', methods=['PUT'])
def update_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()

    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']

    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()

    sum_greece_data.country = country
    sum_greece_data.last_updated_date = last_updated_date
    sum_greece_data.total_cases = total_cases
    sum_greece_data.total_deaths = total_deaths
    sum_greece_data.people_fully_vaccinated = people_fully_vaccinated
    sum_greece_data.population = population

    db.session.commit()

    return sum_covid_greece_schema.jsonify(sum_greece_data)

@app.route('/covid19/summary-data/greece', methods=['DELETE'])
def delete_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()
    
    db.session.delete(sum_greece_data)
    db.session.commit()

    return sum_covid_greece_schema.jsonify(sum_greece_data)

@app.route('/covid19/all-daily-data/greece', methods=['GET'])
def get_all_daily_covid_data_greece():
    all_daily_data = CovidGreeceModel.query.all()

    return all_covid_greece_schema.jsonify(all_daily_data)

@app.route('/covid19/daily-data/greece/date/<date>', methods=['GET'])
def get_specific_date_covid_data_greece(date):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    specific_date_data = CovidGreeceModel.query.filter_by(date=date_obj).first()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/daily-data/greece', methods=['POST'])
def add_daily_covid_data_greece():
    country = request.json['country']
    date = request.json['date']
    new_cases = request.json['new_cases']
    new_tests = request.json['new_tests']
    new_deaths = request.json['new_deaths']
    new_vaccinations = request.json['new_vaccinations']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    new_data = CovidGreeceModel(
        country, date_obj, new_cases, new_tests, new_deaths, new_vaccinations)
    db.session.add(new_data)
    db.session.commit()

    return covid_greece_schema.jsonify(new_data)

@app.route('/covid19/daily-data/greece/date/<date>', methods=['PUT'])
def update_specific_date_covid_data_greece(date):
    specific_date_data = CovidModel.query.filter_by(date=date).first()
   
    country = request.json['country']
    date = request.json['date']
    new_cases = request.json['cases']
    new_tests = request.json['tests']
    new_deaths = request.json['deaths']
    new_vaccinations = request.json['vaccinations']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    specific_date_data.country = country
    specific_date_data.date = date_obj
    specific_date_data.new_cases = new_cases
    specific_date_data.new_tests = new_tests
    specific_date_data.new_deaths = new_deaths
    specific_date_data.new_vaccintations = new_vaccinations

    db.session.commit()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/daily-data/greece/date/<date>', methods=['DELETE'])
def delete_specific_date_covid_data_greece(date):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    specific_date_data = CovidGreeceModel.query.filter_by(date=date_obj).first()
    
    db.session.delete(specific_date_data)
    db.session.commit()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/daily-data/greece/date-period/<from_date>/<until_date>', methods=['GET'])
def get_specific_period_covid_data_greece(from_date, until_date):
    from_date_obj = datetime.datetime.strptime(from_date, '%Y-%m-%d').date()
    until_date_obj = datetime.datetime.strptime(until_date, '%Y-%m-%d').date()

    specific_period_data = CovidGreeceModel.query.filter(
        CovidGreeceModel.date <= until_date_obj).filter(
            CovidGreeceModel.date >= from_date_obj)

    return all_covid_greece_schema.jsonify(specific_period_data)

@app.route('/covid19/summary-data/world', methods=['GET'])
def get_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/world', methods=['POST'])
def add_summary_covid_data_world():
    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']
    
    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()
    
    new_sum_world_data = SumCovidWorldModel(
        country, date_obj, total_cases, total_deaths, people_fully_vaccinated, 
        population)
        
    db.session.add(new_sum_world_data)
    db.session.commit()

    return sum_covid_world_schema.jsonify(new_sum_world_data)

@app.route('/covid19/summary-data/world', methods=['PUT'])
def update_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']

    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()
    
    sum_world_data.country = country
    sum_world_data.last_updated_date = last_updated_date
    sum_world_data.total_cases = total_cases
    sum_world_data.total_deaths = total_deaths
    sum_world_data.people_fully_vaccinated = people_fully_vaccinated
    sum_world_data.population = population

    db.session.commit()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/world', methods=['DELETE'])
def delete_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    db.session.delete(sum_world_data)
    db.session.commit()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/all-countries', methods=['GET'])
def get_summary_covid_data_all_countries():
    sum_all_countries_data = SumCovidCountryModel.query.all()

    return sum_covid_all_countries_schema.jsonify(sum_all_countries_data)

@app.route('/covid19/summary-data/country/<country>', methods=['GET'])
def get_summary_covid_data_specific_country(country):
    sum_specific_country_data = SumCovidCountryModel.query.filter_by(country=country).first()

    return sum_covid_country_schema.jsonify(sum_specific_country_data)

@app.route('/covid19/summary-data/country', methods=['POST'])
def add_summary_covid_data_country():
    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']

    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()

    new_sum_country_data = SumCovidCountryModel(
        country, date_obj, total_cases, total_deaths, people_fully_vaccinated, 
        population)
        
    db.session.add(new_sum_country_data)
    db.session.commit()

    return sum_covid_country_schema.jsonify(new_sum_country_data)

@app.route('/covid19/summary-data/country/<country>', methods=['PUT'])
def update_summary_covid_data_usa(country):
    sum_country_data = SumCovidCountryModel.query.filter_by(country=country).first()

    country = request.json['country']
    last_updated_date = request.json['last_updated_date']
    total_cases = request.json['total_cases']
    total_deaths = request.json['total_deaths']
    people_fully_vaccinated = request.json['people_fully_vaccinated']
    population = request.json['population']

    date_obj = datetime.datetime.strptime(last_updated_date, '%Y-%m-%d').date()
    
    sum_country_data.country = country
    sum_country_data.last_updated_date = last_updated_date
    sum_country_data.total_cases = total_cases
    sum_country_data.total_deaths = total_deaths
    sum_country_data.people_fully_vaccinated = people_fully_vaccinated
    sum_country_data.population = population

    db.session.commit()

    return sum_covid_country_schema.jsonify(sum_country_data)

@app.route('/covid19/summary-data/country/<country>', methods=['DELETE'])
def delete_summary_covid_data_usa(country):
    sum_country_data = SumCovidCountryModel.query.filter_by(country=country).first()

    db.session.delete(sum_country_data)
    db.session.commit()

    return sum_covid_country_schema.jsonify(sum_country_data)
