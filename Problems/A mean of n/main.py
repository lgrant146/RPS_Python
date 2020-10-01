

import statistics
iterate = int(input())

count = []

while len(count) < iterate:
    n = float(input())
    count.append(n)

print(statistics.mean(count))
