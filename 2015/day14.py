from functools import partial
from typing import List, TypedDict


class Reindeer(TypedDict):
    name: str
    speed: int
    active_time: int
    rest_time: int


test_reindeers: List[Reindeer] = [
    {"name": "Comet", "speed": 14, "active_time": 10, "rest_time": 127},
    {"name": "Dancer", "speed": 16, "active_time": 11, "rest_time": 162},
]


with open('inputs/day14.in', "r", newline="") as readfile:
    full_reindeer_list: List[Reindeer] = [
        {
            "name": reindeer[0],
            "speed": int(reindeer[3]),
            "active_time": int(reindeer[6]),
            "rest_time": int(reindeer[-2]),
        }
        for reindeer in [x.split() for x in readfile.readlines()]
    ]


# Shared

def get_reindeer_position(reindeer: Reindeer, time: int) -> int:
    time_in_motion = (
        reindeer["active_time"] * (time // (reindeer["active_time"] + reindeer["rest_time"])) +
        min(reindeer["active_time"], time % (reindeer["active_time"] + reindeer["rest_time"]))
    )
    return reindeer["speed"] * time_in_motion


# Part 1

def get_max_distance(reindeer_list: List[Reindeer], time_period: int = 1000) -> int:
    return max([get_reindeer_position(reindeer, time_period) for reindeer in reindeer_list])

assert get_max_distance(test_reindeers) == 1120
print(get_max_distance(full_reindeer_list, 2503))


# Part 2

def get_max_points(reindeer_list: List[Reindeer], time_period: int = 1000) -> int:
    points = {reindeer["name"]: 0 for reindeer in reindeer_list}
    for t in range(1, time_period+1):
        lead_pos = max(map(partial(get_reindeer_position, time=t), reindeer_list))
        for reindeer_name in [
            reindeer['name'] for reindeer in reindeer_list
            if get_reindeer_position(reindeer, t) == lead_pos
        ]:
            points[reindeer_name] += 1
    return max(points.values())

assert get_max_points(test_reindeers) == 689
print(get_max_points(full_reindeer_list, 2503))
