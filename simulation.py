import math

# get max solution
def solve_quadratic(a, b, c):
    D_2 = b**2 - 4*a*c
    assert D_2 >= 0
    x = (-b + math.sqrt(D_2)) / (2*a)
    return x

# description:
  # no-turn and no-lane-change intersection with traffic light
# assume:
  # infinite cars in queue
  # "through" := car breaking the stop line's plane
  # no variance (all drivers act perfectly average)
def throughput_basic(speed_lim, t_green, yellow_mult, car_len, stop_spacing, go_threshold, acc):
    # time
    t_total = t_green + speed_lim * yellow_mult
    t_to_limit = speed_lim / acc
    t_acc = min(t_to_limit, t_total)
    t_limit = t_total - t_acc
    
    # distance
    d_hood_to_hood = stop_spacing + car_len
    d_acc = (0.5 * acc * t_acc**2)
    d_limit = speed_lim * t_limit

    if stop_spacing >= go_threshold:
        return math.ceil((d_acc + d_limit) / d_hood_to_hood)
    else:
        d_to_go_threshold = go_threshold - stop_spacing
        if d_to_go_threshold < d_acc:
            t_delay = math.sqrt((2 * d_to_go_threshold) / acc)
            c = acc * t_total**2
            t_to_plane = solve_quadratic(d_to_go_threshold, d_hood_to_hood)
        else:
            t_delay = t_acc + (d_to_go_threshold - d_acc) / speed_lim
            t_to_plane = 0
        
        return 0

def main():
    speed_limit = 25            # m/s
    green_time = 30             # s
    yellow_time_multiple = 0.1  # s^2/m
    car_length = 15             # m
    stopped_car_spacing = 8     # m
    go_threshold = 20           # m
    acceleration = 5            # m/s^2

    # advanced parameters
    left_turn_probability = 0.0 # probability of a left turn
    reaction_time = 0.0         # time to begin acceleration
    speed_tolerance = 5

    print(f"""
Throughput of traffic at stoplight given the following conditions:
    Speed limit: {speed_limit}
    Time green: {green_time}
    Time yellow: {yellow_time_multiple * speed_limit}
    Avg. car length: {car_length}
    Stopped spacing: {stopped_car_spacing}
    Space threshold to acc.: {go_threshold}
""")
    throughput_basic(speed_limit, green_time, yellow_time_multiple, car_length, stopped_car_spacing, go_threshold, acceleration)

if __name__=="__main__":
    main()