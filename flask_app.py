from flask import Flask, request, jsonify, render_template
#from threading import Thread

app = Flask(__name__)
variables = {}

@app.route('/')
def home():
    return render_template('index.html')
    # return """Hello. I am alive! I am a Discord bot!</br>I am cool.</br>
    # <iframe src="https://discord.com/widget?id=1081525939726462986&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>"""
    # <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">

# def run():
#     app.run(debug=True)
#     #app.run()


# def keep_alive():
#     print("Hello World!")
#     run()
#     #t = Thread(target=run)
#     #t.start
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
    if variable_name == "d_pgp_LOGIN":
        import pickle
        with open('Backup.pickle', 'wb') as handle:
            pickle.dump(value, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
    variables[variable_name] = value
    return 'Variable updated successfully'

@app.route('/load_backup', methods=['GET'])
def load_backup():
    import pickle
    with open('Backup.pickle', 'rb') as handle:
        a = pickle.load(handle)
        variables["d_pgp_LOGIN"] = a
    return "Sucess! Variables loaded from backup."
if __name__ == '__main__':
    app.run(debug=True)
