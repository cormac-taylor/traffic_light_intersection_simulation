speed_limit = 25            # mph
green_time = 30             # seconds
yellow_time_multiple = 0.1  # seconds
car_len = 15                # feet
stopped_car_spacing = 0.5   # multiple of car length
go_threshold = 1.5          # multiple of car length
acceleration = 5            

# advanced parameters
left_turn_probability = 0.0 # probability of a left turn
reaction_time = 0.0         # time to begin acceleration
speed_tolerance = 5

# basic case:
# single-lane no-turn intersection with traffic light
# infinite amount of cars in queue
# "through" is defined as the car breaking the stop line's plane
def throughput_basic(sp_lim, g_t, y_m, c_len, st_sp, go_th, acc):
    
    return 0

def main():
    print(f"""
Throughput of traffic at stoplight given the following conditions:
    Speed limit: {speed_limit}
    Time green: {green_time}
    Time yellow: {yellow_time_multiple * speed_limit}
    Avg. car length: {car_len}
    Stopped spacing: {stopped_car_spacing}
    Space threshold to acc.: {go_threshold}
""")
    throughput(green_time, speed_limit, yellow_time_multiple, car_len, stopped_car_spacing, go_threshold)

if __name__=="__main__":
    main()