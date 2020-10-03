 # put your python code here
a = int(input())
b = int(input())
c = []

for n in range(a, b + 1):
    if n % 3 == 0:
        c.append(n)

print(sum(c) / len(c))
