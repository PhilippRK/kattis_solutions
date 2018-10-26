from sys import stdin, stdout

n = stdin.readline()
arr = [int(x) for x in stdin.readline().split()]
count = 0
for i in arr:
    if i < 0:
        count += 1
print(count)
