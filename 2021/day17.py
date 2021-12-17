from collections import defaultdict
from typing import Dict, Literal, Tuple


# test_input = "target area: x=20..30, y=-10..-5"
# full_input = "target area: x=29..73, y=-248..-194"
InputTypeAlias = Dict[Literal["x","y"],Tuple[int,int]]
test_input: InputTypeAlias = {"x": (20,30), "y": (-10,-5)}
full_input: InputTypeAlias = {"x": (29,73), "y": (-248,-194)}


# Every valid negative initial y velocity has a corresponding valid positive initial y velocity
# If an initial (-ve) y velocity of `-v` ends within bounds after `s` steps,
# then an inital y velocity of `v-1` ends within bounds after `s + 1 + 2(v-1)` steps,
# since after `2(v-1)+1` steps it will return to `y=0`, and have a (-ve) velocity of exactly `v`


# Part 1
def find_max_height(bounds: InputTypeAlias) -> int:    
    max_y_vel = 0
    for init_vel in range(0, bounds["y"][0]-1, -1):
        curr_vel = init_vel
        curr_dy = 0
        steps = 0
        while curr_dy >= bounds["y"][0]:
            curr_dy += curr_vel
            curr_vel -= 1
            steps += 1
            if (
                bounds["y"][0] <= curr_dy <= bounds["y"][1]  
            ):
                max_y_vel = max(max_y_vel, -init_vel-1)

    triangle_number = lambda n: (n+1)*(n)//2
    return triangle_number(max_y_vel)

assert find_max_height(test_input) == 45
print(find_max_height(full_input))


# Part 2
def count_valid_init_velocities(bounds: InputTypeAlias) -> int:
    # Find valid steps for x velocities
    valid_x_steps = defaultdict(list)
    dropoffs = set()    # If the x velocity = 0 over the target, then all future steps are valid
    for init_vel in range(1, bounds["x"][1] + 1):
        curr_vel = init_vel
        curr_dx = 0
        steps = 0
        while curr_dx <= bounds["x"][1] and curr_vel != 0:
            curr_dx += curr_vel
            curr_vel -= 1
            steps += 1
            if bounds["x"][0] <= curr_dx <= bounds["x"][1]:
                valid_x_steps[steps].append(init_vel)
                if curr_vel == 0:
                    dropoffs.add(init_vel)
    
    valid_init_vels = set()
    for init_y_vel in range(0, bounds["y"][0]-1, -1):
        curr_vel = init_y_vel
        curr_dy = 0
        steps = 0
        while curr_dy >= bounds["y"][0]:
            curr_dy += curr_vel
            curr_vel -= 1
            steps += 1
            if bounds["y"][0] <= curr_dy <= bounds["y"][1]:
                if steps in valid_x_steps:
                    for init_x_vel in valid_x_steps[steps]:
                        valid_init_vels.add((init_x_vel, init_y_vel))

                if (steps + 1 - 2 * (init_y_vel-1)) in valid_x_steps:
                    for init_x_vel in valid_x_steps[steps]:
                        valid_init_vels.add((init_x_vel, -init_y_vel-1))

                for init_x_vel in dropoffs:
                    if steps > init_x_vel:
                        valid_init_vels.add((init_x_vel, init_y_vel))
                    if (steps + 1 - 2 * (init_y_vel-1)) > init_x_vel:
                        valid_init_vels.add((init_x_vel, -init_y_vel-1))
                        
    return len(valid_init_vels)

assert count_valid_init_velocities(test_input) == 112
print(count_valid_init_velocities(full_input))
