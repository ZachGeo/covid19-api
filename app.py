from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

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

class CovidSchema(ma.Schema):
    class Meta:
        fields = ('date', 'cases', 'deaths')

class SumCovidSchema(ma.Schema):
    class Meta:
        fields = ('sum_cases', 'sum_deaths', 'sum_recovered')

covid_schema = CovidSchema()
covids_schema = CovidSchema(many=True)

sum_covid_schema = SumCovidSchema()

# ----------- Summary CovidGR -------------
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

# -------------- CovidGR ---------------
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

if __name__ == '__main__':
    app.run(debug=True)
