from flask import request, jsonify
from api import app, db
from api.models import (
    CovidGreeceModel, SumCovidGreeceModel, SumCovidWorldModel, 
    SumCovidUnitedStatesModel, SumCovidChinaModel, SumCovidFranceModel,
    SumCovidUnitedKingdomModel, SumCovidGermanyModel, SumCovidItalyModel,
    SumCovidRussiaModel, SumCovidJapanModel, SumCovidCanadaModel)
from api.schemas import (
    covid_greece_schema, all_covid_greece_schema, sum_covid_greece_schema, 
    sum_covid_world_schema, sum_covid_usa_schema, sum_covid_china_schema, 
    sum_covid_france_schema, sum_covid_uk_schema, sum_covid_germany_schema, 
    sum_covid_italy_schema, sum_covid_russia_schema, sum_covid_japan_schema, 
    sum_covid_canada_schema)

import datetime

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to our \
        <a href="https://github.com/ZachGeo/covidGR_API">Covid19 API</a>.<h1>'

@app.route('/covid19/summary-data/greece', methods=['POST'])
def add_summary_covid_data_greece():
    sum_greece_cases = request.json['sum_greece_cases']
    sum_greece_tests = request.json['sum_greece_tests']
    sum_greece_deaths = request.json['sum_greece_deaths']
    sum_greece_recovered = request.json['sum_greece_recovered']
    sum_greece_vaccinations = request.json['sum_greece_vaccinations']

    add_sum_greece_covid = SumCovidGreeceModel(
        sum_greece_cases, sum_greece_tests, sum_greece_deaths, 
        sum_greece_recovered, sum_greece_vaccinations)
    db.session.add(add_sum_greece_covid)
    db.session.commit()

    return sum_covid_greece_schema.jsonify(add_sum_greece_covid)

@app.route('/covid19/summary-data/greece', methods=['GET'])
def get_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()
    result = sum_covid_greece_schema.dump(sum_greece_data)

    return jsonify(result)

@app.route('/covid19/summary-data/greece', methods=['PUT'])
def update_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()

    sum_greece_cases = request.json['sum_greece_cases']
    sum_greece_tests = request.json['sum_greece_tests']
    sum_greece_deaths = request.json['sum_greece_deaths']
    sum_greece_recovered = request.json['sum_greece_recovered']
    sum_greece_vaccinations = request.json['sum_greece_vaccinations']

    sum_greece_data.sum_greece_cases = sum_greece_cases
    sum_greece_data.sum_greece_tests = sum_greece_tests
    sum_greece_data.sum_greece_deaths = sum_greece_deaths
    sum_greece_data.sum_greece_recovered = sum_greece_recovered
    sum_greece_data.sum_greece_vaccinations = sum_greece_vaccinations

    db.session.commit()

    return sum_covid_greece_schema.jsonify(sum_greece_data)

@app.route('/covid19/summary-data/greece', methods=['DELETE'])
def delete_summary_covid_data_greece():
    sum_greece_data = SumCovidGreeceModel.query.filter_by(id=1).first()
    
    db.session.delete(sum_greece_data)
    db.session.commit()

    return sum_covid_greece_schema.jsonify(sum_greece_data)

@app.route('/covid19/data/greece', methods=['POST'])
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

@app.route('/covid19/data/greece', methods=['GET'])
def get_all_daily_covid_data_greece():
    all_daily_data = CovidGreeceModel.query.all()
    result = all_covid_greece_schema.dump(all_daily_data)

    return jsonify(result)

@app.route('/covid19/data/greece/date/<date>', methods=['GET'])
def get_specific_date_covid_data_greece(date):
    specific_date_data = CovidGreeceModel.query.filter_by(date=date).first()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/data/greece/date-period/<from_date>/<until_date>', 
    methods=['GET'])
def get_specific_period_covid_data_greece(from_date, until_date):
    specific_period_data = CovidGreeceModel.query.filter(
        CovidModel.date <= until_date).filter(CovidModel.date >= from_date)
    result = all_covid_greece_schema.dump(specific_period_data)

    return jsonify(result)

@app.route('/covid19/data/greece/date/<date>', methods=['PUT'])
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

@app.route('/covid19/data/greece/date/<date>', methods=['DELETE'])
def delete_specific_date_covid_data_greece(date):
    specific_date_data = CovidModel.query.filter_by(date=date).first()
    
    db.session.delete(specific_date_data)
    db.session.commit()

    return covid_greece_schema.jsonify(specific_date_data)

@app.route('/covid19/summary-data/world', methods=['GET'])
def get_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()
    result = sum_covid_world_schema.dump(sum_world_data)

    return jsonify(result)

@app.route('/covid19/summary-data/world', methods=['POST'])
def add_summary_covid_data_world():
    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']
    sum_world_vaccinations = request.json['sum_world_vaccinations']
    
    add_sum_world_data = SumCovidWorldModel(sum_world_cases, sum_world_deaths, 
        sum_world_recovered, sum_world_vaccinations)
        
    db.session.add(add_sum_world_data)
    db.session.commit()

    return sum_covid_world_schema.jsonify(add_sum_world_data)

@app.route('/covid19/summary-data/world', methods=['PUT'])
def update_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']
    sum_world_vaccinations = request.json['sum_world_vaccinations']

    sum_world_data.sum_world_cases = sum_world_cases
    sum_world_data.sum_world_deaths = sum_world_deaths
    sum_world_data.sum_world_recovered = sum_world_recovered
    sum_world_data.sum_world_vaccinations = sum_world_vaccinations

    db.session.commit()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/world', methods=['DELETE'])
def delete_summary_covid_data_world():
    sum_world_data = SumCovidWorldModel.query.filter_by(id=1).first()

    db.session.delete(sum_world_data)
    db.session.commit()

    return sum_covid_world_schema.jsonify(sum_world_data)

@app.route('/covid19/summary-data/usa', methods=['GET'])
def get_summary_covid_data_usa():
    sum_usa_data = SumCovidUnitedStatesModel.query.filter_by(id=1).first()
    result = sum_covid_usa_schema(sum_usa_data)

    return jsonify(result)

@app.route('/covid19/summary-data/usa', methods=['POST'])
def add_summary_covid_data_usa():
    sum_usa_cases = request.json['sum_usa_cases']
    sum_usa_deaths = request.json['sum_usa_deaths']
    sum_usa_recovered = request.json['sum_usa_recovered']
    sum_usa_vaccinations = request.json['sum_usa_vaccinations']
    
    add_sum_usa_data = SumCovidUnitedStatesModel(sum_usa_cases, sum_usa_deaths, 
        sum_usa_recovered, sum_usa_vaccinations)
        
    db.session.add(add_sum_usa_data)
    db.session.commit()

    return sum_covid_usa_schema.jsonify(add_sum_usa_data)

@app.route('/covid19/summary-data/usa', methods=['PUT'])
def update_summary_covid_data_usa():
    sum_usa_data = SumCovidUnitedStatesModel.query.filter_by(id=1).first()

    sum_usa_cases = request.json['sum_usa_cases']
    sum_usa_deaths = request.json['sum_usa_deaths']
    sum_usa_recovered = request.json['sum_usa_recovered']
    sum_usa_vaccinations = request.json['sum_usa_vaccinations']

    sum_usa_data.sum_usa_cases = sum_usa_cases
    sum_usa_data.sum_usa_deaths = sum_usa_deaths
    sum_usa_data.sum_usa_recovered = sum_usa_recovered
    sum_usa_data.sum_usa_vaccinations = sum_usa_vaccinations

    db.session.commit()

    return sum_covid_usa_schema.jsonify(sum_usa_data)

@app.route('/covid19/summary-data/usa', methods=['DELETE'])
def delete_summary_covid_data_usa():
    sum_usa_data = SumCovidUnitedStatesModel.query.filter_by(id=1).first()

    db.session.delete(sum_usa_data)
    db.session.commit()

    return sum_covid_usa_schema.jsonify(sum_usa_data)

@app.route('/covid19/summary-data/china', methods=['GET'])
def get_summary_covid_data_china():
    sum_china_data = SumCovidChinaModel.query.filter_by(id=1).first()

    return sum_covid_china_schema.jsonify(sum_china_data)

@app.route('/covid19/summary-data/china', methods=['POST'])
def add_summary_covid_data_china():
    sum_china_cases = request.json()
    sum_china_deaths = request.json()
    sum_china_recovered = request.json()
    sum_china_vaccinations = request.json()

    add_sum_china_data = SumCovidChinaModel(sum_china_cases, sum_china_deaths,
        sum_china_recovered, sum_china_vaccinations)
    
    db.session.add(add_sum_china_data)
    db.session.commit()

    return sum_covid_china_schema.jsonify(add_sum_china_data)

@app.route('/covid19/summary-data/china', methods=['PUT'])
def update_summary_covid_data_china():
    sum_china_data = SumCovidChinaModel.query.filter_by(id=1).first()

    sum_china_cases = request.json()
    sum_china_deaths = request.json()
    sum_china_recovered = request.json()
    sum_china_vaccinations = request.json()

    sum_china_data.sum_china_cases = sum_china_cases
    sum_china_data.sum_china_deaths = sum_china_deaths
    sum_china_data.sum_china_recovered = sum_china_recovered
    sum_china_data.sum_china_vaccinations = sum_china_vaccinations

    db.session.commit()

    return sum_covid_china_schema.jsonify(sum_china_data)

@app.route('/covid19/summary-data/china', methods=['DELETE'])
def delete_summary_covid_data_china():
    sum_china_data = SumCovidChinaModel.query.filter_by(id=1).first()

    db.session.delete(sum_china_data)
    db.session.commit()

    return sum_covid_china_schema.jsonify(sum_china_data)
