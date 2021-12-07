f = open("input.txt", "r")
arr = [int(x) for x in f.readline().strip().split(',')]

mx = max(arr)
mn = min(arr)
minFuel = 999999999999

for i in range(mn, mx+1):     
    fuel = 0 
    for crab in arr:
        fuel += abs(crab-i)
    if (fuel < minFuel):
        minFuel = fuel

print(minFuel)