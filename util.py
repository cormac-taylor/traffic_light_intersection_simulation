import math

# get largest solution
# given: a and b are positive and c is negitive
def solve_quadratic(a, b, c):
  disc = b**2 - 4*a*c
  assert disc >= 0
  
  x = (-b + math.sqrt(disc)) / (2*a)
  assert x >= 0
  return x

def m_to_ft(m):
    return m * 3.28084

def ft_to_m(ft):
    return ft / 3.28084

def mps_to_mph(mps):
    return mps * 2.23694

def mph_to_mps(mph):
    return mph / 2.23694
