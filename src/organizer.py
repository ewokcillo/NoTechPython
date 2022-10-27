import json
import csv
from typing import List

# put your best code here


def load_rooms(path: str) -> List[dict]:
    with open(path, 'r') as rooms_file:
        rooms = json.load(rooms_file)
    return rooms


def load_developers(path: str) -> List[List]:
    developers = []
    with open(path) as developers_file:
        developeres_reader = csv.reader(developers_file, delimiter=',')
        for developer_info in developeres_reader:
            developers.append(developer_info)
    return developers


def initial_rooms_setup(rooms: List[dict]) -> List[dict]:
    for room in rooms:
        room["developers"] = []
        room["filled"] = False
        room["departments"] = []


def fit_in_perfect_room(rooms: List[dict], developer: str, department: str) -> (bool, List[dict]):
    for room in rooms:
        if fits_in_room(room, developer, department):
            room["developers"].append(developer)
            room["departments"].append(department)
            room["filled"] = room["places"] > len(room["developers"])
            return True, rooms
    return False, rooms


def fit_in_any_room(rooms: List[dict], developer: str) -> (bool, List[dict]):
    for room in rooms:
        if fits_in_room(room, developer):
            room["developers"].append(developer)
            room["filled"] = room["places"] > len(room["developers"])
            return True, rooms
    return False, rooms


def fits_in_room(room: dict , department: str = None) ->  bool :
    return not room["filled"] and department not in room["departments"]


rooms = load_rooms('../data/rooms.json')
developers = load_developers('../data/developers_departments.csv')


print(rooms)
print(developers)