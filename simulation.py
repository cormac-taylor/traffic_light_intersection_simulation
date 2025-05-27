import math

# get largest solution
# given: a and b are positive and c is negitive
def solve_quadratic(a, b, c):
    disc = b**2 - 4*a*c
    assert disc >= 0
    
    x = (-b + math.sqrt(disc)) / (2*a)
    assert x >= 0
    return x

def mps_to_mph(x):
    return x * 3600 / 1609.34

def m_to_ft(x):
    return x * 3.28084

# description:
  # no-turn and no-lane-change intersection with traffic light
# assume:
  # infinite cars in queue
  # "through" := car breaking the stop line's plane
  # no variance (all drivers act perfectly average)
def throughput_basic(speed_lim, t_green, t_yellow, car_len, stop_spacing, go_threshold, acc):
    # time
    t_total = t_green + t_yellow
    t_to_speed_limit = speed_lim / acc
    t_acc = min(t_to_speed_limit, t_total)
    t_limit = t_total - t_acc
    
    # distance
    d_car = stop_spacing + car_len
    d_acc = (0.5 * acc * t_acc**2)
    d_limit = speed_lim * t_limit

    if stop_spacing >= go_threshold:
        # enough space to accelerate immediately
        # solved in distance
        return math.ceil((d_acc + d_limit) / d_car)
    else:
        # must wait to accelerate
        # solved in time
        d_to_go_threshold = go_threshold - stop_spacing    
        a = (2 * d_to_go_threshold) / acc
        b = (2 * d_car) / acc
        c = - t_total ** 2
        return math.ceil(solve_quadratic(a, b, c))

def main():
    speed_limit = 11                # m/s
    green_time = 30                 # s
    yellow_time_multiple = 0.25     # s^2/m
    car_length = 5                  # m
    stopped_car_spacing = 2.5       # m
    go_threshold = 6                # m
    acceleration = 2                # m/s^2

    # advanced parameters
    left_turn_probability = 0.0 # probability of a left turn
    reaction_time = 0.0         # time to begin acceleration
    speed_tolerance = 5

    print(f"""
Stoplight situation:
    no-turn and no-lane-change intersection with traffic light
    
Given conditions:
    Speed limit ----------- {mps_to_mph(speed_limit)} mph
    Time green ------------ {green_time} s
    Time yellow ----------- {yellow_time_multiple * speed_limit} s
    Car lengths ----------- {m_to_ft(car_length)} ft
    Stopped spacing ------- {m_to_ft(stopped_car_spacing)} ft
    Space to accelerate --- {m_to_ft(go_threshold)} ft
    Acceleration ---------- {acceleration} m/s^2
    
Throughput: {throughput_basic(speed_limit, green_time, speed_limit * yellow_time_multiple, car_length, stopped_car_spacing, go_threshold, acceleration)}
""")

if __name__=="__main__":
    main()