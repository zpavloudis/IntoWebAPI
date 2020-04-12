from IntoWebAPI import app
from IntoWebAPI.records import query_db
from datetime import date

@app.route('/values')
def values():
    values = query_db('select * from records')
    return values

@app.route('/values/<country>')
def get_country_cases(country):
    values = query_db('select * from records where countriesAndTerritories = ?',
                        [country])
    return values

@app.route('/values/<country_code>')
def get_country_cases_code(country_code):
    values = query_db('select * from records where countryterritoryCode = ?',
                        [country_code])
    return values

@app.route('/values/date')
def get_todays_cases():
    values = query_db('select * from records where dateRep = ?', 
                        [date.today().strftime("%d/%m/%y")])
    return values

@app.route('/values/date/<date>')
def get_cases_for_date(date):
   # dt = date[:2] + '/' + date[2:4] + '/' + date[4:6]
   # print(dt)
    values = query_db('select * from records where dateRep = ?',
        [date[:2] + '/' + date[2:4] + '/' + date[4:6]])
    return values