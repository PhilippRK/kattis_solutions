from sys import stdin

arr = [int(x) for x in stdin.readline().split()]
print(arr[0] * (arr[1] - 1) + 1)
