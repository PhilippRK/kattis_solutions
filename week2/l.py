from sys import stdin
n = int(stdin.readline())
mins = 0
secs = 0
for i in range(n):
    m, s = (int(x) for x in stdin.readline().split())
    mins += m
    secs += s
slmin = secs / 60.0 / mins
if slmin <= 1.0:
    print("measurement error")
else:
    print(slmin)
