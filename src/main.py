from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

source = [{'name': 'United Kingdom', 'isoCode': 'GB'},
          {'name': 'France', 'isoCode': 'FR'}]

destination = [{'name': 'United Kingdom', 'isoCode': 'GB'},
               {'name': 'Spain', 'isoCode': 'ES'},
               {'name': 'France', 'isoCode': 'FR'},
               {'name': 'Ireland', 'charge': 'IE'}]


@main.route('/', methods=['GET'])
def hello_world():
    # return render_template('index.html')
    return jsonify({'message': 'Hello, Sebastian!'})


@main.route('/api/v1/countries/<string:name>', methods=['GET'])
def return_countries(name):
    if name == 'source':
        countries = source
    else:
        countries = destination
    return jsonify({'countries': countries})
