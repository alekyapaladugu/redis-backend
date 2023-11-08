from datetime import date
# from redis_om import Field, JsonModel, RedisOM
from redis import Redis
import rom
from typing import Optional, List

# Connect to Redis

rom.util.set_connection_settings(host='redis-13794.c73.us-east-1-2.ec2.cloud.redislabs.com', port=13794,password='ebU15KawkzA4nWCBKoCtussWgCLhGWAp')

class Tournament(rom.Model):
     key_id = rom.Integer(required=True, index=True)
     tournament_id = rom.String(required=True)
     tournament_name = rom.String(required=True)
     year = rom.Integer(index=False)
     start_date = rom.String()
     end_date = rom.String()
     host_country = rom.String(required=True)
     winner = rom.String(required=True)
     host_won = rom.Integer(required=True)
     count_teams = rom.Integer(required=True)
     group_stage = rom.Integer()
     second_group_stage = rom.Integer()
     final_round = rom.Integer()
     round_of_16 = rom.Integer()
     quarter_finals = rom.Integer()
     semi_finals = rom.Integer()
     third_place_match = rom.Integer()
     final = rom.Integer()
