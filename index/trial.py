command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started.....")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the car
        """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand that")

A = int(input("Enter value for first side:  "))
B = int(input("Enter value for second side: "))
C = int(input("Enter value for third side: "))

S = ((A + B + C) // 2)
AR = (S * (S - A) * (S - B) * (S - C) * 1 // 2)
print(f"Area of a triangle {AR}")

CSC_101 = int(input('Write the scores of CSC 101: '))
ENT_101 = int(input('Write the scores of ENT 101: '))
CSC_102 = int(input('Write the scores of CSC 102: '))

summation = (CSC_101 + ENT_101 + CSC_102)

print(f"The total score is {summation}")

score = int(input("Write the score of CSC 101:"))
if score >= 40:
    print("You pass")
else:
    print("You fail")


