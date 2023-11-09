import csv
import requests
import json

with open('data/tournaments.csv', encoding = 'utf-8') as csv_file_handler:
    reader = csv.DictReader(csv_file_handler)
    data = list(reader)

for row in data:
    r = requests.post('http://127.0.0.1:5000/tournament/new', json=row)
    print(f"Created tournament {row['key_id']}")

# data =  {
#         "count_teams": 13,
#         "end_date": "1930-07-30",
#         "final": 1,
#         "final_round": 0,
#         "group_stage": 1,
#         "host_country": "Uruguay",
#         "host_won": 0,
#         "id": 1,
#         "key_id": 1,
#         "quarter_finals": 0,
#         "round_of_16": 0,
#         "second_group_stage": 0,
#         "semi_finals": 1,
#         "start_date": "",
#         "third_place_match": 0,
#         "tournament_id": "WC-1930",
#         "tournament_name": "1930 FIFA Men's World Cup",
#         "winner": "Uruguay",
#         "year": 1930
#     },

# r = requests.post('http://127.0.0.1:5000/tournament/update', json=data, headers={'Content-Type': 'application/json'})
