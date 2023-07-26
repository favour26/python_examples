import random


def password_converter(password):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXTZ'
    numbers = '0123456789'
    symbols = '@#$%&*/\?>'

    Use_for = lower_case + upper_case + numbers + symbols
    length_for_pass = 8
    output = ''.join(random.sample(Use_for, length_for_pass))
    return output


password = ''
print(password_converter(password))
