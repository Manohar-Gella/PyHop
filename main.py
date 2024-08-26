import random
import time

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def remove_element(array, element):
    if element in array:
        array.remove(element)
def generate_random_5_digit_number():
    return random.randint(10000, 99999)

def ticket(name, age, nseats):
    print(f"Name of the passenger {name.upper()}")
    time.sleep(1)
    print(f"Age of the passenger {age}")
    time.sleep(1)
    print(f"Allotted seat number {nseats}")
    time.sleep(1)
    print("Happy journey")
    time.sleep(1)
    print("Ticket number")
    random_number = generate_random_5_digit_number()
    print(random_number)

def main():
    while True:
        print("_____________________________________________________________________________________________________________________________________________________________________")
        print("Railway Seat Reservation Portal")
        name = input("Name of the passenger: ")
        age = int(input("Enter age: "))
        print(seats)
        nseats = int(input("Enter preferred seats from the list: "))
        print("Generating tick")
        time.sleep(3)
        remove_element(seats, nseats)
        ticket(name, age, nseats)

main()

