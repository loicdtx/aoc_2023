tot = 0
with open('data.txt') as src:
    for line in src:
        digits = [int(x) for x in line if x.isdigit()]
        tot += digits[0] * 10 + digits[-1]
print(tot)

