import math

import math

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8
    time_elapsed = math.sqrt((2 * height) / acceleration_by_gravity)
    return time_elapsed

get_fall_time(15)


def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = get_fall_time(tower_height)

    tower_range = time_in_air*muzzle_velocity
    
    delta_x = tower_x - target_x
    
    delta_y = tower_y - target_y
    

    separation = delta_x**2+delta_y**2

    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return None
    else:
        print("The target is further than the tower range, what should we return?")
        return None

isVulnerable(15, 20, 30, 40, 50)

