'''
Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes 
registration_number, type, and owner. Implement a method 
update_owner to change the vehicle's owner. Then, create a few 
instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class 
without methods.

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
- Expected Outcome: Completion of the Vehicle class with the 
update_ownermethod and a demonstration script showing the creation 
of Vehicle objects and updating their owners.
'''

class Vehicle:
    def __init__(self,reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
    
    def display_vehicle(self):
        print(f"Registration number: {self.registration_number}\nVehicle: {self.type}\nOwner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, type, owner):
    if reg_num in vehicles:
        print("Vehicle already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle with registration number '{reg_num}' registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner for vehicle with registration number: {reg_num}")
    else:
        print("Vehicle not found.")

def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_vehicle()

while True:
    choice = input("Enter choice (register, update, display, exit): ").lower()
    if choice == "exit":
        break        

    try:
        if choice == "register":
            reg_num = input("Enter registration number: ")
            type = input("Enter vehicle type: ")
            owner = input("Enter name of owner: ")
            register_vehicle(reg_num, type, owner)
        elif choice == "update":
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter name of new owner: ")
            update_vehicle_owner(reg_num, new_owner)
        elif choice == "display":
            display_all_vehicles()
    except Exception as e:
        print(f"Error: {e}")
print("Quit.")