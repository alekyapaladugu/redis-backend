import csv
import requests

with open('data/tournaments.csv', encoding = 'utf-8') as csv_file_handler:
    reader = csv.DictReader(csv_file_handler)
    data = list(reader)

for row in data:
    r = requests.post('http://127.0.0.1:5000/tournament/new', json=row)
    print(f"Created tournament {row['key_id']}")

# r = requests.get('http://127.0.0.1:5000/tournaments')
