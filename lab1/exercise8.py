n = 1
number = int(input())

for i in range(100):
    estimate = number / n
    mean = (n + estimate) / 2
    n = mean

print(n)
