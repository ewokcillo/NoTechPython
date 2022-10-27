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
    return rooms


def fit_in_room(rooms: List[dict], developer_name: str, department: str = None) -> (bool, List[dict]):
    for room in rooms:
        if fits_in_room(room, department):
            room["developers"].append(developer_name)
            if department is not None:
                room["departments"].append(department)
            room["filled"] = room["places"] == len(room["developers"])
            return True, rooms
    return False, rooms


def fits_in_room(room: dict, department: str = None) -> bool:
    return not room["filled"] and department not in room["departments"]


# Load initial data
rooms = load_rooms('../data/rooms.json')
developers = load_developers('../data/developers_departments.csv')
sad_developers_without_room = []
# Setup initial rooms state
rooms = initial_rooms_setup(rooms)
# Search best fit for developers
for developer in developers:
    fit, rooms = fit_in_room(rooms, developer[0], developer[1])
    if not fit:
        fit, rooms = fit_in_room(rooms, developer[0])
        if not fit:
            sad_developers_without_room.append(developer)

# print final results
print(f"Final result of each room")
for room in rooms:
    print(f"Room {room['name']}: {room['developers']} form departments {room['departments']}")
print(f"poor sad lonely guys {sad_developers_without_room}")
