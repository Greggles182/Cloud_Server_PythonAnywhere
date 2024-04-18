from flask import Flask, request, jsonify, render_template
#from threading import Thread

app = Flask(__name__)
variables = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list_variables', methods=['GET'])
def list_variables():
    return variables

@app.route('/get_variable', methods=['GET'])
def get_variable():
    variable_name = request.args.get('name')
    return jsonify({variable_name: variables.get(variable_name, None)})


@app.route('/update_variable', methods=['POST'])
def update_variable():
    global i
    data = request.json
    variable_name = data['name']
    value = data['value']
    variables[variable_name] = value
    return 'Variable updated successfully'
app.run()