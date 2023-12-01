import re

numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
pattern = '(?=(' + r'|'.join(numbers.keys() + ['\d{1}))'])

print(pattern)

tot = 0
with open('data.txt') as src:
    for line in src:
        digits = re.findall(pattern, line)
        digits = [int(numbers.get(x,x)) for x in digits]
        tot += digits[0] * 10 + digits[-1]
print(tot)
