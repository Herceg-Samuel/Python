# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
MAX_SEATS = 8

passengers = {
    1: {
        "name": "Buddy",
        "breed": "Golden Retriever",
        "pickup_time": "10:00 AM",  
        "dropoff_time": "11:30 AM"  
    },
    2: {    
        "name": "Max",
        "breed": "Labrador Retriever",
        "pickup_time": "11:00 AM",  
        "dropoff_time": "12:30 PM"  
    },
    3: {
        "name": "Bella",    
        "breed": "Poodle",
        "pickup_time": "1:0",
        "dropoff_time": "2:30 PM"
    },
    4: {
        "name": "Charlie",
        "breed": "German Shepherd",
        "pickup_time": "2:00 PM",
        "dropoff_time": "3:30 PM"
    }

}

print(passengers)

print("Starting roster")
for seat, info in passengers.items():
    print(f"Seat {seat}: {info['name']} ({info['breed']}) - Pickup: {info['pickup_time']}")

#print(input("Add new passeneger? Yes or No."))
#if input == "Yes":
    
#if len(passengers) < MAX_SEATS:
#    new_passenger = {
#        "name": input("Enter the name of the new passenger: "),
#        "breed": input("Enter the breed of the new passenger: "),
#        "pickup_time": input("Enter the pickup time of the new passenger: "),
#        "dropoff_time": input("Enter the dropoff time of the new passenger: ")
#    }
#    next_seat = len(passengers) + 1
#    passengers[next_seat] = new_passenger
#else:
#    print("Bus is full. Cannot add more passengers.")

    



#)
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times. 


remove = input("Who goes home early?").strip().lower()

seat_to_remove = 0
for seat, info in passengers.items():
    if info['name'].lower() == remove:
        seat_to_remove = seat
        del passengers[seat_to_remove]


