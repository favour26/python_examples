phone_book = []

def collect_phone_book_entry():
    entry = {}

    entry['full_name'] = input("Enter your full name: ")
    entry['phone_number'] = input("Enter your phone number: ")
    entry['sex'] = input("Enter your sex: ")
    entry['home_address'] = input('Enter your home address')
