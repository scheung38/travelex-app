from flask import Flask, request, json, jsonify, Response

app = Flask(__name__)

quarks = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]

source = [{'name': 'United Kingdom', 'isoCode': 'GB'},
          {'name': 'France', 'isoCode': 'FR'}]

destination = [{'name': 'United Kingdom', 'isoCode': 'GB'},
               {'name': 'Spain', 'isoCode': 'ES'},
               {'name': 'France', 'isoCode': 'FR'},
               {'name': 'Ireland', 'charge': 'IE'}]


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World Sebastian!'})


@app.route('/api/v1/countries/<string:name>', methods=['GET'])
def returnCountries(name):
    if name == 'source':
        countries = source
    else:
        countries = destination
    return jsonify({'countries': countries})


if __name__ == "__main__":
    app.run(debug=True)
