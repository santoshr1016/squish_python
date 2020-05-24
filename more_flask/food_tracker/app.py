from flask import Flask, render_template, request, g
import sqlite3
from datetime import datetime
import os.path

QUERY_INSERT_FOOD = 'insert into food (name, protein, carbohydrates, fat, calories) values (?,?,?,?,?)'
QUERY_GET_FOOD = 'select name, protein, carbohydrates, fat, calories from food'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)


def connect_db():
    db_path = os.path.join(BASE_DIR, "food_log.db")
    sql = sqlite3.connect(db_path)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date'] # MM-DD-YYYY
        print(date)
        dt = datetime.strptime(date, '%Y-%m-%d')
        db_date = datetime.strftime(dt, '%Y%m%d')

        db.execute('insert into log_date (entry_date) values (?)', [db_date])
        db.commit()

    cursor = db.execute('select entry_date from log_date order by entry_date desc')
    results = cursor.fetchall()

    pretty_dates = []
    for item in results:
        single_date = {}
        dt = datetime.strptime(str(item['entry_date']), '%Y%m%d')
        single_date['entry_date'] = datetime.strftime(dt, '%B %d, %Y')

        pretty_dates.append(single_date)

    return render_template('home.html', pretty_dates=pretty_dates)


@app.route('/view/<date>', methods=['GET', 'POST'])
def view(date):
    db = get_db()
    cur = db.execute('select id, entry_date from log_date where entry_date = ?', [date])
    item = cur.fetchone()

    if request.method == 'POST':
        # return '<h1>Hello, Food item added is #{} </h1>'.format(request.form['food-select'])
        selection = request.form['food-select']
        index = item['id']
        db.execute('insert into food_date (food_id, log_date_id) values (?,?)', [selection, index])
        db.commit()

    dt = datetime.strptime(str(item['entry_date']), '%Y%m%d')
    pretty_date = datetime.strftime(dt, '%B %d, %Y')

    food_cursor = db.execute('select id, name from food')
    food_results = food_cursor.fetchall()

    log_cur = db.execute('select food.name, food.protein, food.carbohydrates, food.fat, food.calories from log_date join \
    food_date on food_date.log_date_id = log_date.id join food on food.id = food_date.food_id where \
    log_date.entry_date = ?',[date])

    log_results = log_cur.fetchall()

    return render_template('day.html', pretty_date=pretty_date, food_results=food_results, log_results=log_results)


@app.route('/food', methods=['GET', 'POST'])
def food():
    db= get_db()
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein*4 + carbohydrates*4 + fat*9

        db.execute(QUERY_INSERT_FOOD, [name, protein, carbohydrates, fat, calories])
        db.commit()
        # return "<h1>Name: {}, protein: {}, carbs: {}, fat:{}</h1>".format(food_name, protein, carbohydrates, fat)
    cur = db.execute(QUERY_GET_FOOD)
    results = cur.fetchall()
    return render_template('add_food.html', results=results)


if __name__ == '__main__':
    app = app.run(debug=True)
