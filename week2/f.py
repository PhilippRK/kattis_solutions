from sys import stdin
c = float(stdin.readline())
l = int(stdin.readline())
cost = 0.0
for i in range(l):
    arr = [float(x) for x in stdin.readline().split()]
    cost += c * arr[0] * arr[1]
print(cost)
