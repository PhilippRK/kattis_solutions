from sys import stdin
n = int(stdin.readline())
for i in range(n):
    arr = [int(x) for x in stdin.readline().split()]
    a = arr[0]
    b = arr[1] - arr[2]
    if a > b:
        print("do not advertise")
    if a == b:
        print("does not matter")
    if a < b:
        print("advertise")
