import time
from time import sleep
from tqdm import tqdm

seats = [1, 2]


def reserve(array, element):
    if element in array:
        array.remove(element)


def ticket(name, age, phone, address, seat):
    print(f"""
        Passenger data

Name: {name.upper()}
Age: {age}
Phone number: {phone}
Allotted Seat number: {seat}
        Happy journey
""")


def ticket(name, age, phone, address, bseat):
    tkd = f"""
                    INDIAN RAILWAYS RESERVATION SYSTEM ELECTRONIC TICKET
        'name': {name},
        'age': {age},
        'Mobile number': {phone},
        'Address': {address},
        'Allotted Seat': {bseat}
        """
    with open(f'/Users/manohargella/Downloads/{name}.txt', 'w') as eticket:
        eticket.write(tkd)


def main():
    while True:
        print("Indian Railway booKing services")
        next = input("Enter to reservation portal: ")
        if len(seats) == 0:
            print("All seats are reserved")
            break
        else:
            name = input("Name of the passenger: ")
            age = int(input("Age of the passenger: "))
            phone = int(input("Mobile number of the passenger: "))
            address = input("Adress of the passenger: ")
            print(f"Total available seats: {len(seats)}")
            print(seats)
            bseat = int(input("Select on prefferd seat from list of available seats: "))
            ticket(name, age, phone, address, bseat)
            cnf = input("Confirm ticket: 'Y' or 'N': ")
            if cnf.lower() == 'y':
                reserve(seats, bseat)
                print("Gnerating Ticket")
                for i in tqdm(range(1000)):
                    sleep(0.0009)

                print("Ticket downloaded sucessfully")
            elif cnf.lower() == 'n':
                print("Cancelling the ticket")
                for i in tqdm(range(1000)):
                    sleep(0.0009)
                print("Successfully cancelled")
                time.sleep(1)
                print("Returning to home page")
                for i in tqdm(range(1000)):
                    sleep(0.0010)
                main()


main()
