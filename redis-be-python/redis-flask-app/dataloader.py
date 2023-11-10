import csv
import json
import requests

#create a dictionary
data_dict = {}
print(data_dict)
 
    #Step 2
    #open a csv file handler
with open('data/tournaments.csv', encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
 
        #convert each row into a dictionary
        #and add the converted data to the data_variable
 
    for rows in csv_reader:
 
            #assuming a column named 'No'
            #to be the primary key
        key = rows['key_id']
        data_dict[key] = rows

with open('data/tournaments.json', 'w', encoding = 'utf-8') as json_file_handler:
    json_file_handler.write(json.dumps(data_dict, indent = 4))

# for data in data_dict:
#     r = requests.post('http://127.0.0.1:5000/tournament/new', json=data_dict[data])
    # print(f"Created tournament {data['tournament_id']} {data['key_id']} with ID {r.text}")r

r = requests.get('http://127.0.0.1:5000/tournaments')
