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

class CovidSchema(ma.Schema):
    class Meta:
        fields = ('date', 'cases', 'deaths')

covid_schema = CovidSchema()
covids_schema = CovidSchema(many=True)

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

    covid_data.date = date
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
