from sys import stdin
import math

arr = stdin.readline().split()
opp = float(arr[0])
ang = math.radians(float(arr[1]))
print(int(math.ceil(opp / math.sin(ang))))
