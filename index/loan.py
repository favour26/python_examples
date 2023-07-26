import numbers
from telnetlib import XDISPLOC


has_good_credit = True
has_high_income = False

if has_high_income and has_good_credit:
    print('Eligibele for loan')
else:
    print('Not eligible for loan')


# for loops
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'Total: {total}')

# nested loop
numbers = [2, 2, 2, 2, 5]
max = numbers[0]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


highest_number = [10, 2, 4, 6, 87, 55]
max_number = highest_number[0]
for highest in highest_number:
    if highest > max:
        max = highest
print(max)

