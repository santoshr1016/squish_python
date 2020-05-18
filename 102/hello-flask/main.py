from flask import Flask, jsonify, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'

# localhost:5000/home/santosh
@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'default'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
    return '<h1>This is home page, Welcome home, {}</h1>'.format(name)


@app.route('/json')
def json():
    item = {
        'key1': 'value1',
        'key2': [1, 2, 3, 4, 5]
    }
    return jsonify(item)


# localhost:5000/query?name=Sara&location=Singapore
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1> hello {}, You are from {} right </h1>'.format(name, location)


@app.route('/theform', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                  <input type="text" name="name">
                  <input type="text" name="location"> 
                  <input type="submit" value ="submit">
                  </form>'''
    else:

        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('home', name=name))
        # return '<h2>Welcome to the process, Mr {} from {}</h2>'.format(name, location)


# @app.route('/process', methods=["POST"])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return '<h2>Welcome to the process, Mr {} from {}</h2>'.format(name, location)


@app.route('/processjson', methods=['POST'])
def process_json():
    data = request.get_json()
    name = data['name']
    location = data['location']
    the_list = data['thelist']
    print(name, location, the_list)
    return jsonify({'result': 'success', 'name': name, 'location': location, 'list': the_list})
    pass


if __name__ == '__main__':
    app.run(debug=True)
