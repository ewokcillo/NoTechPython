import json
import csv
from typing import List

# put your best code here

def load_rooms(path: str) -> dict:
    with open(path, 'r') as rooms_file:
        rooms = json.load(rooms_file)
    return rooms

def read_developers(path: str) -> List:
    developers = []
    with open(path) as developers_file:
        developeres_reader = csv.reader(developers_file, delimiter=',')
        for developer_info in developeres_reader:
            developers.append(developer_info)
    return developers


rooms = load_rooms('../data/rooms.json')
developers = read_developers('../data/developers_departments.csv')
print(rooms)
print(developers)