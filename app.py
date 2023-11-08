import json
from xml.dom import NotFoundErr
from flask import Flask, request, jsonify
from pydantic import ValidationError
from tournament import Tournament
from redis_om import Migrator
from redis_om.model import NotFoundError

app = Flask(__name__)


# Utility function to format list of People objects as 
# a results dictionary, for easy conversion to JSON in 
# API responses.
def build_results(people):
    response = []
    for person in people:
        response.append(person.dict())

    return { "results": response }

# Create a new tournament.
@app.route("/tournament/new", methods=["POST"])
def create_tournament():
    try:
        print(request.json)
        new_tournament = Tournament(**request.json)
        new_tournament.save()
        return 'Successful'

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
    print(tournaments_list)
    return jsonify(tournaments_list)
