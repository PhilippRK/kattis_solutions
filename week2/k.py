from sys import stdin

n = int(stdin.readline())
for i in range(n):
    a, b, c = (int(x) for x in stdin.readline().split())
    if a + b == c or a - b == c or b - a == c or a * b == c or c * b == a or c * a == b:
        print("Possible")
    else:
        print("Impossible")
