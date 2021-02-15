from flask import request, jsonify
from api import app, db
from api.models import (
    CovidGreeceModel, SumCovidGreeceModel, SumCovidWorldModel, SumCovidCountryModel)
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
    sum_greece_cases = request.json['sum_greece_cases']
    sum_greece_deaths = request.json['sum_greece_deaths']
    sum_greece_recovered = request.json['sum_greece_recovered']
    sum_greece_vaccinations = request.json['sum_greece_vaccinations']
    last_date_modified = request.json['last_date_modified']

    last_date_modified_obj = datetime.datetime.strptime(last_date_modified, '%Y-%m-%d').date()

    new_sum_greece_covid = SumCovidGreeceModel(
        sum_greece_cases, sum_greece_deaths, sum_greece_recovered, 
        sum_greece_vaccinations, last_date_modified_obj)
    
    db.session.add(new_sum_greece_covid)
    db.session.commit()

    return sum_covid_greece_schema.jsonify(new_sum_greece_covid)

@app.route('/covid19/summary-data/greece', methods=['PUT'])
def update_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()

    sum_greece_cases = request.json['sum_greece_cases']
    sum_greece_deaths = request.json['sum_greece_deaths']
    sum_greece_recovered = request.json['sum_greece_recovered']
    sum_greece_vaccinations = request.json['sum_greece_vaccinations']
    last_date_modified = request.json['last_date_modified']

    last_date_modified_obj = datetime.datetime.strptime(last_date_modified, '%Y-%m-%d').date()

    sum_greece_data.sum_greece_cases = sum_greece_cases
    sum_greece_data.sum_greece_deaths = sum_greece_deaths
    sum_greece_data.sum_greece_recovered = sum_greece_recovered
    sum_greece_data.sum_greece_vaccinations = sum_greece_vaccinations
    sum_greece_data.last_date_modified = last_date_modified_obj

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
    date = request.json['date']
    cases = request.json['cases']
    tests = request.json['tests']
    deaths = request.json['deaths']
    vaccinations = request.json['vaccinations']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    new_data = CovidModel(date_obj, cases, test, deaths, vaccinations)
    db.session.add(new_data)
    db.session.commit()

    return covid_greece_schema.jsonify(new_data)

@app.route('/covid19/daily-data/greece/date/<date>', methods=['PUT'])
def update_specific_date_covid_data_greece(date):
    specific_date_data = CovidModel.query.filter_by(date=date).first()

    date = request.json['date']
    cases = request.json['cases']
    tests = request.json['tests']
    deaths = request.json['deaths']
    vaccinations = request.json['vaccinations']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    specific_date_data.date = date_obj
    specific_date_data.cases = cases
    specific_date_data.tests = tests
    specific_date_data.deaths = deaths
    specific_date_data.vaccintations = vaccinations

    db.session.commit()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/daily-data/greece/date/<date>', methods=['DELETE'])
def delete_specific_date_covid_data_greece(date):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    specific_date_data = CovidModel.query.filter_by(date=date_obj).first()
    
    db.session.delete(specific_date_data)
    db.session.commit()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/daily-data/greece/date-period/<from_date>/<until_date>', methods=['GET'])
def get_specific_period_covid_data_greece(from_date, until_date):
    from_date_obj = datetime.datetime.strptime(from_date, '%Y-%m-%d').date()
    until_date_obj = datetime.datetime.strptime(until_date, '%Y-%m-%d').date()

    specific_period_data = CovidGreeceModel.query.filter(
        CovidModel.date <= until_date_obj).filter(CovidModel.date >= from_date_obj)

    return all_covid_greece_schema.jsonify(specific_period_data)

@app.route('/covid19/summary-data/world', methods=['GET'])
def get_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/world', methods=['POST'])
def add_summary_covid_data_world():
    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']
    sum_world_vaccinations = request.json['sum_world_vaccinations']
    last_date_modified = request.json['last_date_modified']
    
    last_date_modified_obj = datetime.datetime.strptime(last_date_modified, '%Y-%m-%d').date()
    new_sum_world_data = SumCovidWorldModel(sum_world_cases, sum_world_deaths, 
        sum_world_recovered, sum_world_vaccinations, last_date_modified_obj)
        
    db.session.add(new_sum_world_data)
    db.session.commit()

    return sum_covid_world_schema.jsonify(new_sum_world_data)

@app.route('/covid19/summary-data/world', methods=['PUT'])
def update_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']
    sum_world_vaccinations = request.json['sum_world_vaccinations']
    last_date_modified = request.json['last_date_modified']

    last_date_modified_obj = datetime.datetime.strptime(last_date_modified, '%Y-%m-%d').date()

    sum_world_data.sum_world_cases = sum_world_cases
    sum_world_data.sum_world_deaths = sum_world_deaths
    sum_world_data.sum_world_recovered = sum_world_recovered
    sum_world_data.sum_world_vaccinations = sum_world_vaccinations
    sum_world_data.last_date_modified = last_date_modified_obj

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
    sum_country_cases = request.json['sum_country_cases']
    sum_country_deaths = request.json['sum_country_deaths']
    sum_country_recovered = request.json['sum_country_recovered']
    sum_country_vaccinations = request.json['sum_country_vaccinations']
    last_date_modified = request.json['last_date_modified']
    
    last_date_modified_obj = datetime.datetime.strptime(last_date_modified, '%Y-%m-%d').date()

    new_sum_country_data = SumCovidCountryModel(country, sum_country_cases, 
    sum_country_deaths, sum_country_recovered, sum_usa_vaccinations,
    last_date_modified_obj)
        
    db.session.add(new_sum_country_data)
    db.session.commit()

    return sum_covid_country_schema.jsonify(new_sum_country_data)

@app.route('/covid19/summary-data/country/<country>', methods=['PUT'])
def update_summary_covid_data_usa(country):
    sum_country_data = SumCovidCountryModel.query.filter_by(country=country).first()

    country = request.json['country']
    sum_country_cases = request.json['sum_country_cases']
    sum_country_deaths = request.json['sum_country_deaths']
    sum_country_recovered = request.json['sum_country_recovered']
    sum_country_vaccinations = request.json['sum_country_vaccinations']
    last_modified_date = request.json['last_modified_date']

    sum_country_data.country = country
    sum_country_data.sum_country_cases = sum_country_cases
    sum_country_data.sum_country_deaths = sum_country_deaths
    sum_country_data.sum_country_recovered = sum_country_recovered
    sum_country_data.sum_country_vaccinations = sum_country_vaccinations
    sum_country_data.last_modified_date = last_modified_date

    db.session.commit()

    return sum_covid_country_schema.jsonify(sum_country_data)

@app.route('/covid19/summary-data/country/<country>', methods=['DELETE'])
def delete_summary_covid_data_usa(country):
    sum_country_data = SumCovidUnitedStatesModel.query.filter_by(country=country).first()

    db.session.delete(sum_country_data)
    db.session.commit()

    return sum_covid_country_schema.jsonify(sum_country_data)
