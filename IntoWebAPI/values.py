from IntoWebAPI import app
from flask import url_for
from IntoWebAPI.records import query_db
from datetime import date

@app.route('/values')
def values():
    values = query_db('select * from records')
    return values

@app.route('/values/country/<country>')
def get_country_cases(country):
    values = query_db('select * from records where countriesAndTerritories = ?',
                        [country])
    return values

@app.route('/values/country_code/<country_code>')
def get_country_cases_code(country_code):
    values = query_db('select * from records where countryterritoryCode = ?',
                        [country_code])
    print(country_code)
    return values

@app.route('/values/date/today')
def get_todays_cases():
    values = query_db('select * from records where dateRep = ?', 
                        [date.today().strftime("%d/%m/%Y")])
    return values

@app.route('/values/date/<date>')
def get_cases_for_date(date):
    values = query_db('select * from records where dateRep = ?',
        [date[:2] + '/' + date[2:4] + '/' + date[4:8]])
    print('select * from records where dateRep = ?',date[:2] + '/' + date[2:4] + '/' + date[4:8])
    return values

with app.test_request_context():
    print(url_for('values'))
    print(url_for('get_country_cases',country='Greece'))
    print(url_for('get_country_cases_code',country_code='GBR'))
    print(url_for('get_todays_cases'))
    print(url_for('get_cases_for_date',date='08042020'))