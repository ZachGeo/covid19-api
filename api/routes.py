from flask import request, jsonify
from api import app, db
from api.models import CovidModel, SumCovidModel, WorldSumCovidModel
from api.schemas import covid_schema, covids_schema, sum_covid_schema, sum_world_schema

import datetime

@app.route('/summary/covidgr', methods=['POST'])
def add_summary_covid():
    sum_cases = request.json['sum_cases']
    sum_deaths = request.json['sum_deaths']
    sum_recovered = request.json['sum_recovered']

    new_sum_covid = SumCovidModel(sum_cases, sum_deaths, sum_recovered)
    db.session.add(new_sum_covid)
    db.session.commit()

    return sum_covid_schema.jsonify(new_sum_covid)

@app.route('/summary/covidgr', methods=['GET'])
def get_summary_covid():
    sum_covid_data = SumCovidModel.query.filter_by(id=1).first()
    result = sum_covid_schema.dump(sum_covid_data)

    return jsonify(result)

@app.route('/summary/covidgr', methods=['PUT'])
def update_summary_covid():
    sum_covid_data = SumCovidModel.query.filter_by(id=1).first()

    sum_cases = request.json['sum_cases']
    sum_deaths = request.json['sum_deaths']
    sum_recovered = request.json['sum_recovered']

    sum_covid_data.sum_cases = sum_cases
    sum_covid_data.sum_deaths = sum_deaths
    sum_covid_data.sum_recovered = sum_recovered

    db.session.commit()

    return sum_covid_schema.jsonify(sum_covid_data)

@app.route('/summary/covidgr', methods=['DELETE'])
def delete_summary_covid():
    sum_covid_data = SumCovidModel.query.filter_by(id=1).first()
    
    db.session.delete(sum_covid_data)
    db.session.commit()

    return sum_covid_schema.jsonify(sum_covid_data)

@app.route('/covidgr', methods=['POST'])
def add_covid():
    date = request.json['date']
    cases = request.json['cases']
    deaths = request.json['deaths']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    new_covid = CovidModel(date_obj, cases, deaths)
    db.session.add(new_covid)
    db.session.commit()

    return covid_schema.jsonify(new_covid)

@app.route('/covidgr', methods=['GET'])
def get_all_covid():
    all_covid_data = CovidModel.query.all()
    result = covids_schema.dump(all_covid_data)

    return jsonify(result)

@app.route('/covidgr/<date>', methods=['GET'])
def get_covid(date):
    covid_data = CovidModel.query.filter_by(date=date).first()

    return covid_schema.jsonify(covid_data)

@app.route('/covidgr/period/<from_date>/<until_date>', methods=['GET'])
def get_period_covid(from_date, until_date):
    covid_period_data = CovidModel.query.filter(
        CovidModel.date <= until_date).filter(CovidModel.date >= from_date)
    result = covids_schema.dump(covid_period_data)

    return jsonify(result)

@app.route('/covidgr/<date>', methods=['PUT'])
def update_covid(date):
    covid_data = CovidModel.query.filter_by(date=date).first()

    date = request.json['date']
    cases = request.json['cases']
    deaths = request.json['deaths']

    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    covid_data.date = date_obj
    covid_data.cases = cases
    covid_data.deaths = deaths

    db.session.commit()

    return covid_schema.jsonify(covid_data)

@app.route('/covidgr/<date>', methods=['DELETE'])
def delete_covid(date):
    covid_data = CovidModel.query.filter_by(date=date).first()
    
    db.session.delete(covid_data)
    db.session.commit()

    return covid_schema.jsonify(covid_data)

@app.route('/summary/covid/world', methods=['GET'])
def get_summary_covid_world():
    sum_covid_world_data = WorldSumCovid.query.filter_by(id=1).first()

    return sum_covid_schema.jsonify(sum_covid_world_data)

@app.route('/summary/covid/world', methods=['POST'])
def add_summary_covid_world():
    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']
    
    new_sum_covid_world = WorldSumCovidModel(
        sum_world_cases, sum_world_deaths, sum_world_recovered)
        
    db.session.add(new_sum_covid_world)
    db.session.commit()

    return sum_world_schema.jsonify(new_sum_covid_world)

@app.route('/summary/covid/world', methods=['PUT'])
def update_summary_covid_world():
    sum_covid_world_data = WorldSumCovidModel.query.filter_by(id=1).first()

    sum_world_cases = request.json['sum_world_cases']
    sum_world_deaths = request.json['sum_world_deaths']
    sum_world_recovered = request.json['sum_world_recovered']

    sum_covid_world_data.sum_world_cases = sum_world_cases
    sum_covid_world_data.sum_world_deaths = sum_world_deaths
    sum_covid_world_data.sum_world_recovered = sum_world_recovered

    db.session.commit()

    return sum_world_schema.jsonify(sum_covid_world_data)
