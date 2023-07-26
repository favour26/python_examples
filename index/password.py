import random


lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%&?><|}{:*'

use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 10
password = ''.join(random.sample(use_for, length_for_pass))
print(f'Your generated password is: {password} ')


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + "  "
print(output)