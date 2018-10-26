from sys import stdin
import math

def area(r):
    return math.pi * r * r

r, c = (int(x) for x in stdin.readline().split())
whole = area(r)
inner = area(r-c)
print(100 * (inner/whole))
