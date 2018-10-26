from sys import stdin, stdout

n = int(stdin.readline())
mins = 0
secs = 0
for i in range(n):
    line = [int(x) for x in stdin.readline().split()]
    mins += line[0]
    secs += line[1]
res = secs/60.0/mins
if res <= 1.0:
    print("measurement error")
else:
    print(res)
