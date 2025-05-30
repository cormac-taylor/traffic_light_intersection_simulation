import math
import util

# get largest solution
# given: a and b are positive and c is negitive
def solve_quadratic(a, b, c):
  disc = b**2 - 4*a*c
  assert disc >= 0
  
  x = (-b + math.sqrt(disc)) / (2*a)
  assert x >= 0
  return x

# description:
  # no-turn and no-lane-change intersection with traffic light
# assume:
  # infinite cars in queue
  # "through" := car being on both sides of the stop line's plane
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

  if stop_spacing > go_threshold:
    # enough space to accelerate immediately
    # solved in distance
    
    return math.ceil((d_acc + d_limit) / d_car)
  
  else:
    # must wait to accelerate
    # solved in time
    
    d_to_go_threshold = go_threshold - stop_spacing
    
    # this assumes:
      # i * d_car > d_acc > d_to_go_threshold
      # this is reasonable under realistic considerations
    num = t_total + (d_acc / speed_lim) - t_acc
    den = math.sqrt(2 * d_to_go_threshold / acc) + d_car / speed_lim
    return math.ceil(num / den)

# This is the exausive handling but the condition to decide the equation seems to depend on the result 
    # if d_acc > d_to_go_threshold:
    #   if distance traveled by last car is < d_acc:
    #     a = 2 * d_to_go_threshold / acc
    #     b = 2 * d_car / acc
    #     c = -1 * (t_total ** 2)
    #     return math.ceil(solve_quadratic(a, b, c))
    #   else:
    #     num = t_total + (d_acc / speed_lim) - t_acc
    #     den = math.sqrt(2 * d_to_go_threshold / acc) + d_car / speed_lim
    #     return math.ceil(num / den)
    # else: 
    #   if distance traveled by last car is < d_acc:
    #     a = (t_acc + (d_to_go_threshold - d_acc) / speed_lim) ** 2
    #     b = 2 * d_car / acc
    #     c = -1 * (t_total ** 2)
    #     return math.ceil(solve_quadratic(a, b, c))
    #   else:
    #     print("hit")
    #     num = t_total + (d_acc / speed_lim) - t_acc
    #     den = t_acc + (d_to_go_threshold - d_acc + d_car) / speed_lim
    #     return math.ceil(num / den)

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
  Speed limit ----------- {util.mps_to_mph(speed_limit)} mph
  Time green ------------ {green_time} s
  Time yellow ----------- {yellow_time_multiple * speed_limit} s
  Car lengths ----------- {util.m_to_ft(car_length)} ft
  Stopped spacing ------- {util.m_to_ft(stopped_car_spacing)} ft
  Space to accelerate --- {util.m_to_ft(go_threshold)} ft
  Acceleration ---------- {acceleration} m/s^2
    
Throughput: {throughput_basic(speed_limit, green_time, speed_limit * yellow_time_multiple, car_length, stopped_car_spacing, go_threshold, acceleration)}
""")

if __name__=="__main__":
  main()
