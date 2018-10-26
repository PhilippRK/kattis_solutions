from sys import stdin, stdout

given = [int(x) for x in stdin.readline().split()]
wanted = [1,1,2,2,2,8]
for i, val in enumerate(given):
    stdout.write(str(wanted[i] - val) + " ")
print("")
