import json
from xml.dom import NotFoundErr
from flask import Flask, request, jsonify
from pydantic import ValidationError
from tournament import Tournament
from redis_om import Migrator
from redis_om.model import NotFoundError
from flask_cors import CORS, cross_origin
import rom

app = Flask(__name__)

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

# Create a new tournament.
@app.route("/tournament/new", methods=["POST"])
def create_tournament():
    try:
        new_tournament = Tournament(**request.json)
        new_tournament.save()
        return jsonify({'success': True}), 200

    except ValidationError as e:
        print(e)
        return "Bad request.", 400

# Get All tournament records.
@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    tournaments_list = []
    # Query all Tournament records
    tournaments = Tournament.query.all()
    # Convert Tournament objects to dictionaries
    for tournament in tournaments:
        tournaments_dict = tournament.to_dict()
        for key,value in tournaments_dict.items():
            if isinstance(value, bytes):
                tournaments_dict[key] = value.decode('utf-8')
        tournaments_list.append(tournaments_dict)
    # Return JSON response
    return jsonify({'tournaments': tournaments_list})

# Update a tournament. Use where clauses
@app.route('/tournament/update', methods=['POST'])
def update():
    key = request.json['key_id']
    host_country = request.json['host_country']
    if not key:
        return jsonify({'error': 'Missing key'}), 400
    update_existing_tournament = Tournament.query.filter(key_id=key).all()
    if update_existing_tournament is None:
        return jsonify({'error': 'No such key/column exists'}), 404
    else:
        update_existing_tournament.host_won = host_country
        update_existing_tournament.save()
        return jsonify({'success': True}), 200

@app.after_request
def after(response):
    # todo with response
    print(response.status)
    print(response.headers)
    print(response.get_data())
    return response