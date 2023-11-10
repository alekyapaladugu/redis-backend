import json
from xml.dom import NotFoundErr
from flask import Flask, request, jsonify
from pydantic import ValidationError
from schema import Tournament, AwardWinners
from redis_om import Migrator
from redis_om.model import NotFoundError
from flask_cors import CORS, cross_origin
import rom

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def crossOrigin():
  return jsonify({'success': 'ok'})

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

# Update a tournament.
@app.route('/tournament/update/winner', methods=['POST'])
def update_tournament():
    try:
        key = request.json['key_id']
        winner = request.json['winner'].encode('utf-8')
        update_tournament = Tournament.get(key)
        print(update_tournament)
        update_tournament.winner = winner
        update_tournament.save()
        return jsonify({'success': True}), 200
    except ValidationError as e:
        if not key:
            return jsonify({'error': 'Missing key'}), 400 
        if update_tournament is None:
            return jsonify({'error': 'No column exists'}), 404

# Delete a tournament
@app.route('/tournament/delete', methods=['POST'])
def delete_tournament():
    try:
        key = request.json['key_id']
        record = Tournament.get(key)
        if record is not None:
            record.delete()
        return jsonify({'success': True}), 200
    except ValidationError as e:
        if not key:
            return jsonify({'error': 'Missing key'}), 400 
        if update_tournament is None:
            return jsonify({'error': 'No column exists'}), 404
        
# Create a new award winner.
@app.route("/award_winners/new", methods=['POST'])
def create_award_winner():
    try:
        new_award_winner = AwardWinners(**request.json)
        new_award_winner.save()
        return jsonify({'success': True}), 200
    except ValidationError as e:
        print(e)
        return "Bad request.", 400
    
# For each tournament, send the award winners along with team names and award name
@app.route("/awardWinners", methods=["POST"])
def get_award_winners():
    try:
        awards_winners_list = []
        tournament_id = request.json['tournament_id']
        print(tournament_id)
        award_winners = AwardWinners.query.filter(tournament_id=tournament_id).all()
        print(award_winners)
        for winner in award_winners:
            winners_dict = winner.to_dict()
        print(winners_dict)
        for key,value in winners_dict.items():
            if isinstance(value, bytes):
                winners_dict[key] = value.decode('utf-8')
        awards_winners_list.append(winners_dict)
        return jsonify({'award_winners': awards_winners_list})

    except ValidationError as e:
        if not tournament_id:
            return jsonify({'error': 'Empty Tournament ID'}), 400 
        if award_winners is None:
            return jsonify({'error': 'Incorrect Tournament ID'}), 404
 
if __name__ == "__main__":
    app.run(debug=True)

# @app.after_request
# def after(response):
#     # todo with response
#     print(response.status)
#     print(response.headers)
#     print(response.get_data())
#     return response