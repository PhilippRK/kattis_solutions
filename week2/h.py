from sys import stdin
arr = [int(x) for x in stdin.readline().split()]
if arr[1] % 2 == 0:
    print("possible")
else:
    print("impossible")
