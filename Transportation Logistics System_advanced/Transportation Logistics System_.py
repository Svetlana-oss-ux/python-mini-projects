# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 07:49:01 2025

@author: Svetlana
"""

from abc import ABC, abstractmethod
import re
from datetime import datetime

# ========================== Abstract Base Manager Class ===========================

class Manager(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def display_summary(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    @property
    def name(self):
        return self._name

# ============================== Entity Classes =====================================

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity

    def __str__(self):
        return f"{self.vehicle_id}\t\t{self.vehicle_type}\t\t{self.capacity} kg"

class Customer:
    def __init__(self, customer_id, name, dob, address, phone, email):
        self.customer_id = customer_id
        self.name = name
        self._dob = dob
        self.address = address
        self._phone = phone
        self._email = email

    def __str__(self):
        return f"{self.customer_id}\t{self.name}\t{self.address}\t{self._phone}, {self._email}"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value):
            raise ValueError("Invalid email format")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not re.match(r"^04\d{8}$", value):
            raise ValueError("Phone must be in the format 04XXXXXXXX")
        self._phone = value

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        try:
            birth_date = datetime.strptime(value, "%d/%m/%Y")
            age = (datetime.today() - birth_date).days // 365
            if age < 18:
                raise ValueError("Customer must be at least 18 years old")
            self._dob = value
        except ValueError:
            raise ValueError("Invalid date of birth format or underage")


# Represents a shipment, linking a customer and a vehicle, and tracking its status
class Shipment:
    def __init__(self, shipment_id, origin, destination, weight, vehicle_id, customer_id):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.status = "In transit"
        self.delivery_date = None

    def __str__(self):
        return f"{self.shipment_id}\t{self.origin}\t{self.destination}\t{self.weight}kg\t{self.vehicle_id}\t{self.status}\t{self.delivery_date or 'N/A'}"

    @property   
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight (self, value):
        if isinstance(value,(int,float)) and value >0:
            return self._value
        else:
            raise ValueError("Weight must be positive number")
      

# Represents the delivery status of a shipment with optional delivery date
class Delivery:
    def __init__(self, shipment_id, delivery_date=None):
        self.shipment_id = shipment_id
        self.delivery_date = delivery_date or datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"Shipment {self.shipment_id} delivered on {self.delivery_date}"

# ============================= FleetManager Class ==================================
# Handles all vehicle-related operations and inherits the standard manager interface

class FleetManager(Manager):
    def __init__(self):
        super().__init__("Fleet Manager")
        self.fleet = []

    def validate_vehicle_id(self, vehicle_id):
        return re.fullmatch(r"[A-Za-z0-9]{3,10}", vehicle_id)

    def find_vehicle(self, vehicle_id):
        for vehicle in self.fleet:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def add_vehicle(self):
        print("=== Add a New Vehicle ===")
        while True:
            vehicle_id = input("Enter Vehicle ID (e.g., V001) or type 'exit' to cancel: ").strip()
            if vehicle_id.lower() == 'exit':
                print("Vehicle creation cancelled.")
                input("Press Enter to return to menu...")
                return
            if not self.validate_vehicle_id(vehicle_id):
                print("Invalid Vehicle ID. It should be in English and alphanumeric and 3–10 characters long.")
                input("Press Enter to continue...")
                continue
            if self.find_vehicle(vehicle_id):
                print("Vehicle ID already exists.")
                input("Press Enter to continue...")
                return
            break

        vehicle_type = input("Enter Vehicle Type (Truck, Van, Car) or type 'exit' to cancel: ").strip()
        if vehicle_type.lower() == 'exit':
            print("Vehicle creation cancelled.")
            input("Press Enter to return to menu...")
            return

        while True:
            cap_input = input("Enter Vehicle Capacity in kg (e.g., 1000) or type 'exit' to cancel: ").strip()
            if cap_input.lower() == 'exit':
                print("Vehicle creation cancelled.")
                input("Press Enter to return to menu...")
                return
            try:
                capacity = int(cap_input)
                if capacity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid capacity. Must be a positive integer.")
                input("Press Enter to continue...")

        new_vehicle = Vehicle(vehicle_id, vehicle_type, capacity)
        self.fleet.append(new_vehicle)
        print("Vehicle added successfully.")
        input("Press Enter to return to menu...")

    def update_vehicle(self):
        print("=== Update Vehicle Information ===")
        vehicle_id = input("Enter Vehicle ID to update or type 'exit' to cancel: ").strip()
        if vehicle_id.lower() == 'exit':
            print("Update cancelled.")
            input("Press Enter to return to menu...")
            return

        vehicle = self.find_vehicle(vehicle_id)
        if not vehicle:
            print("Vehicle ID not found.")
            input("Press Enter to continue...")
            return

        vehicle_type = input("Enter new Vehicle Type or type 'exit' to cancel: ").strip()
        if vehicle_type.lower() == 'exit':
            print("Update cancelled.")
            input("Press Enter to return to menu...")
            return

        while True:
            cap_input = input("Enter new Vehicle Capacity in kg or type 'exit' to cancel: ").strip()
            if cap_input.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to return to menu...")
                return
            try:
                capacity = int(cap_input)
                if capacity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid capacity. Must be a positive integer.")
                input("Press Enter to continue...")

        vehicle.vehicle_type = vehicle_type
        vehicle.capacity = capacity
        print("Vehicle information updated successfully.")
        input("Press Enter to return to menu...")

    def remove_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to remove or type 'exit' to cancel: ").strip()
        if vehicle_id.lower() == 'exit':
            print("Removal cancelled.")
            input("Press Enter to return to menu...")
            return

        vehicle = self.find_vehicle(vehicle_id)
        if not vehicle:
            print("Vehicle ID not found.")
            input("Press Enter to continue...")
            return

        confirm = input(f"Are you sure you want to remove vehicle {vehicle_id}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self.fleet.remove(vehicle)
            print("Vehicle removed successfully.")
        else:
            print("Vehicle removal cancelled.")
        input("Press Enter to return to menu...")

    def view_all_vehicles(self):
        if not self.fleet:
            print("No vehicles in the fleet.")
        else:
            print("Fleet Vehicles:")
            print("ID		Type		Capacity")
            print("-" * 30)
            for vehicle in self.fleet:
                print(vehicle)

        while True:
            choice = input("Type 'exit' to return to the Fleet Management Menu: ")
            if choice.lower() == 'exit':
                break

    def display_summary(self):
        print(f"[{self.name}] Total vehicles: {len(self.fleet)}")

    def menu(self):
        self.fleet_management_menu()

    def fleet_management_menu(self):
        while True:
            print("--- Fleet Management Menu ---")
            print("1. Add a vehicle")
            print("2. Update vehicle information")
            print("3. Remove a vehicle")
            print("4. View all vehicles")
            print("5. Quit fleet management")
            print("0. Show system summary")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.update_vehicle()
            elif choice == '3':
                self.remove_vehicle()
            elif choice == '4':
                self.view_all_vehicles()
            elif choice == '5':
                print("Returning to Main Menu...")
                break
            elif choice == '0':
                print("\n=== System Summary ===")
                self.display_summary()
                input("Press Enter to return to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")


# ============================= CustomerManager Class ==================================
class CustomerManager(Manager):
    def __init__(self):
        super().__init__("Customer Manager")
        self.customers = []
        self.shipment_manager = None

    def validate_customer_id(self, customer_id):
        return re.match(r"^[A-Za-z0-9]{3,10}$", customer_id)

    def validate_dob(self, dob):
        try:
            birth_date = datetime.strptime(dob, "%d/%m/%Y")
            age = (datetime.today() - birth_date).days // 365
            return age >= 18
        except ValueError:
            return False

    def validate_address(self, address):
        return re.match(r"^\d+ .+, [A-Z]{2,3} \d{4}, Australia$", address.strip())

    def validate_phone(self, phone):
        return re.match(r"^04\d{8}$", phone)

    def validate_email(self, email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def add_customer(self):
        customer_id = input("Enter Customer ID (e.g., ABC123) or type 'exit' to cancel: ")
        if customer_id.lower() == 'exit':
            print("Customer creation cancelled.")
            input("Press Enter to continue...")
            return
        if not self.validate_customer_id(customer_id):
            print("Invalid Customer ID. It should be alphanumeric and 3-10 characters long.")
            input("Press Enter to continue...")
            return

        if self.find_customer(customer_id):
            print("Customer ID already exists.")
            input("Press Enter to continue...")
            return

        name = input("Enter Name or type 'exit' to cancel: ")
        if name.lower() == 'exit':
            print("Customer creation cancelled.")
            input("Press Enter to continue...")
            return

        dob = input("Enter Date of Birth (DD/MM/YYYY) or type 'exit': ")
        if dob.lower() == 'exit':
            print("Customer creation cancelled.")
            input("Press Enter to continue...")
            return
        if not self.validate_dob(dob):
            print("Invalid DOB or underage customer (must be 18+).")
            input("Press Enter to continue...")
            return
        
            # Loop until a valid new address is entered or 'exit' is typed
        while True:
              address = input("Enter Address or type 'exit': ")
              if address.lower() == 'exit':
                 print("Customer creation cancelled.")
                 input("Press Enter to continue...")
                 break
              if not self.validate_address(address):
                 print("Invalid Address. Format: '123 Main St, Sydney, NSW 2000, Australia'")
                 input("Press Enter to continue...")
                 continue
              break

              phone = input("Enter Phone Number (e.g., 04XXXXXXXX) or type 'exit': ")
              if phone.lower() == 'exit':
                  print("Customer creation cancelled.")
                  input("Press Enter to continue...")
              break
              if not self.validate_phone(phone):
                  print("Invalid phone number.")
                  input("Press Enter to continue...")
                  return

              email = input("Enter Email or type 'exit': ")
              if email.lower() == 'exit':
                  print("Customer creation cancelled.")
                  input("Press Enter to continue...")
                  break
              if not self.validate_email(email):
                   print("Invalid email address.")
                   input("Press Enter to continue...")
                   return

        customer = Customer(customer_id, name, dob, address, phone, email)
        self.customers.append(customer)
        print("Customer added successfully.")
        input("Press Enter to continue...")

    def update_customer(self):
        customer_id = input("Enter Customer ID to update or type 'exit': ")
        if customer_id.lower() == 'exit':
            print("Update cancelled.")
            input("Press Enter to continue...")
            return

        customer = self.find_customer(customer_id)
        if not customer:
            print("Customer ID not found.")
            input("Press Enter to continue...")
            return

        attempts = 3
        while attempts > 0:
            name = input("Enter new Name or type 'exit': ")
            if name.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to continue...")
                return

            dob = input("Enter new Date of Birth (DD/MM/YYYY) or type 'exit': ")
            if dob.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to continue...")
                return

            address = input("Enter new Address or type 'exit': ")
            if address.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to continue...")
                return

            phone = input("Enter new Phone or type 'exit': ")
            if phone.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to continue...")
                return

            email = input("Enter new Email or type 'exit': ")
            if email.lower() == 'exit':
                print("Update cancelled.")
                input("Press Enter to continue...")
                return

            if not (self.validate_dob(dob) and self.validate_address(address) and self.validate_phone(phone) and self.validate_email(email)):
                attempts -= 1
                print(f"Invalid input. {attempts} attempts remaining.")
                input("Press Enter to continue...")
            else:
                customer.name = name
                customer.dob = dob
                customer.address = address
                customer.phone = phone
                customer.email = email
                print("Customer information updated successfully.")
                input("Press Enter to continue...")
                return
        print("Failed to update customer after 3 attempts.")
        input("Press Enter to continue...")
        
    def remove_customer(self):
        customer_id = input("Enter Customer ID to remove: ")
        customer = self.find_customer(customer_id)
        if not customer:
            print("Customer ID not found.")
            return

        confirm = input(f"Are you sure you want to remove customer {customer_id}? (yes/no): ")
        if confirm.lower() == 'yes':
            self.customers.remove(customer)
            print("Customer removed successfully.")
        else:
            print("Customer removal cancelled.")

    def view_all_customers(self):
        if not self.customers:
            print("No customers available.")
        else:
            print("\nCustomer List:")
            print("ID\tName\tAddress\tContact")
            print("-" * 60)
            for customer in self.customers:
                print(customer)

    def view_customer_shipments(self):
        customer_id = input("Enter Customer ID to view shipments: ")
        if not self.find_customer(customer_id):
            print("Customer ID not found.")
            return

        if not self.shipment_manager.shipments:
            print("Shipments empty")
            return

        print("ID\tOrigin\tDestination\tWeight\tVehicle\tStatus\tDelivery Date")
        print("-" * 70)        
        for shipment in self.shipment_manager.shipments:
            if shipment.customer_id == customer_id:
                print(shipment)
                
    def display_summary(self):
        print(f"[{self.name}] Total customers: {len(self.customers)}")

    def menu(self):
        self.customer_management_menu()

    def customer_management_menu(self):
        while True:
            print("\n--- Customer Management Menu ---")
            print("1. Add a customer")
            print("2. Update customer information")
            print("3. Remove a customer")
            print("4. View all customers")
            print("5. View a customer's shipments")
            print("6. Quit customer management")
            print("0. Show system summary")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_customer()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                self.remove_customer()
            elif choice == '4':
                self.view_all_customers()
            elif choice == '5':
                self.view_customer_shipments()
            elif choice == '6':
                print("Returning to Main Menu...")
                break
            elif choice == '0':
                customer_manager.display_summary()
                break
            else:
                print("Invalid choice. Please try again.")

                
#------------------------------------------Shipment management--------------------------
# ShipmentManager class
class ShipmentManager(Manager):
    def __init__(self):
        super().__init__("Shipment Management")
        self.shipments = []
        self.customer_manager = None
        self.fleet_manager = None

    def validate_shipment_id(self, shipment_id):
        return re.match(r"^[A-Za-z0-9]{2,10}$", shipment_id)

    def validate_address(self, address):
        return re.match(r"^\d+ .+, [A-Z]{2,3} \d{4}, Australia$", address.strip())

    def validate_vehicle_id(self, vehicle_id):
        return re.match(r"^[A-Za-z0-9]{3,10}$", vehicle_id)

    def validate_weight(self, weight):
        try:
            weight = float(weight)
            return weight > 0
        except ValueError:
            return False

    def find_shipment(self, shipment_id):
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        return None

    def create_shipment(self):
        shipment_id = input("Enter Shipment ID (e.g., S123) or type 'exit' to cancel: ")
        if shipment_id.lower() == 'exit':
            print("Returning to menu...")
            return
        if not self.validate_shipment_id(shipment_id):
            print("Invalid Shipment ID format.")
            input("Press Enter to continue...")
            return
        if self.find_shipment(shipment_id):
            print("Shipment ID already exists.")
            input("Press Enter to continue...")
            return

        origin = input("Enter Origin location (e.g., 123 Main St, Sydney, NSW 2000, Australia) or type 'exit': ")
        if origin.lower() == 'exit':
            print("Returning to menu...")
            return
        if not self.validate_address(origin):
            print("Invalid Address. Format: '123 Main St, Sydney, NSW 2000, Australia'")
            input("Press Enter to continue...")
            return

        destination = input("Enter Destination location in the same format or type 'exit': ")
        if destination.lower() == 'exit':
            print("Returning to menu...")
            return
        if not self.validate_address(destination):
            print("Invalid Address. Format: '123 Main St, Sydney, NSW 2000, Australia'")
            input("Press Enter to continue...")
            return

        # Get weight input
        while True:
            weight_input = input("Enter Weight in kg (e.g., 500) or type 'exit': ").strip()
            if weight_input.lower() == 'exit':
                print("Returning to menu...")
                return
            try:
                weight_value = float(weight_input)
                if weight_value <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid weight. Must be a positive number.")
                input("Press Enter to continue...")

        # Show available vehicles
        print("\nAvailable Vehicles:")
        available_vehicles = [v for v in self.fleet_manager.fleet]
        if not available_vehicles:
            print("No vehicles available.")
            input("Press Enter to continue...")
            return
        for v in available_vehicles:
            print(v)

        # Get vehicle ID
        vehicle_id = input("Enter Vehicle ID to assign or type 'exit': ")
        if vehicle_id.lower() == 'exit':
            print("Returning to menu...")
            return
        if not self.validate_vehicle_id(vehicle_id):
            print("Invalid Vehicle ID.")
            input("Press Enter to continue...")
            return
        vehicle = self.fleet_manager.find_vehicle(vehicle_id)
        if not vehicle:
            print("Vehicle not found.")
            input("Press Enter to continue...")
            return

        # Get customer ID
        customer_id = input("Enter Customer ID for the shipment or type 'exit': ")
        if customer_id.lower() == 'exit':
            print("Returning to menu...")
            return
        customer = self.customer_manager.find_customer(customer_id)
        if not customer:
            print("Customer ID not found.")
            input("Press Enter to continue...")
            return

        # Create and save Shipment
        shipment = Shipment(shipment_id, origin, destination, weight_value, vehicle_id, customer_id)
        self.shipments.append(shipment)
        print("Shipment created successfully.")
        input("Press Enter to continue...")

    def track_shipment(self):
        shipment_id = input("Enter Shipment ID to track or type 'exit': ")
        if shipment_id.lower() == 'exit':
            print("Returning to menu...")
            return
        shipment = self.find_shipment(shipment_id)
        if shipment:
            print(f"Shipment Status: {shipment.status}")
        else:
            print("Shipment ID not found.")
        input("Press Enter to continue...")

    def view_all_shipments(self):
        if not self.shipments:
            print("No shipments available.")
        else:
            print("\nAll Shipments:")
            print("ID\tOrigin\tDestination\tWeight\tVehicle\tStatus\tDelivery Date")
            print("-" * 70)
            for shipment in self.shipments:
                print(shipment)
        input("Press Enter to continue...")

    def display_summary(self):
        print(f"[{self.name}] Total shipments: {len(self.shipments)}")

    def menu(self):
        self.shipment_management_menu()

    def shipment_management_menu(self):
        while True:
            print("\n--- Shipment Management Menu ---")
            print("1. Create a new shipment")
            print("2. Track a shipment")
            print("3. View all shipments")
            print("4. Quit shipment management")
            print("0. Show system summary")
            choice = input("Enter your choice (0-4): ")

            if choice == '1':
                self.create_shipment()
            elif choice == '2':
                self.track_shipment()
            elif choice == '3':
                self.view_all_shipments()
            elif choice == '0':
                self.display_summary()
            elif choice == '4':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")

                
#------------------------------------------------Delivery management------------------ 

class DeliveryManager(Manager):
    def __init__(self):
        super().__init__("Delivery Manager")
        self.shipment_manager = None
        self.deliveries = []  # Stores delivered shipments

    def mark_delivery(self):
        print(f"\nCurrent date and time: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        shipment_id = input("Enter Shipment ID to mark as delivered: ")
        shipment = self.shipment_manager.find_shipment(shipment_id)

        if not shipment:
            print("Shipment ID not found.")
            input("Press Enter to continue...")
            return

        if shipment.status.lower() == "delivered":
            print("Shipment has already been marked as delivered.")
            input("Press Enter to continue...")
            return

        shipment.status = "Delivered"
        delivery_datetime = datetime.now()
        shipment.delivery_date = delivery_datetime.strftime("%d/%m/%Y")
        shipment.delivery_time = delivery_datetime.strftime("%H:%M")
        self.deliveries.append(shipment)
        print("Shipment marked as delivered successfully.")
        input("Press Enter to continue...")

    def view_delivery_status(self):
        shipment_id = input("Enter Shipment ID to view delivery status: ")
        shipment = self.shipment_manager.find_shipment(shipment_id)

        if not shipment:
            print("Shipment ID not found.")
            input("Press Enter to continue...")
            return

        if shipment.status.lower() != "delivered":
            print("Shipment has not been delivered yet.")
            input("Press Enter to continue...")
            return

        print(f"Shipment {shipment.shipment_id} was delivered on {shipment.delivery_date} at {shipment.delivery_time}.")
        input("Press Enter to continue...")

    # Polymorphic method from base class
    def display_summary(self):
        print(f"[{self.name}] Total deliveries: {len(self.deliveries)}")

    # Polymorphic method to trigger menu
    def menu(self):
        self.delivery_management_menu()

       
    def delivery_management_menu(self):
        while True:
            print("\n--- Delivery Management Menu ---")
            print("1. Mark Shippment delivery")
            print("2. View delivery status for a shipment")
            print("3. Quit delivery management")
            print("0. Show system summary")
            choice = input("Enter your choice (0-3): ")

            if choice == '1':
                self.mark_delivery()
            elif choice == '2':
                self.view_delivery_status()
            elif choice == '0':
                delivery_manager.display_summary()
            elif choice == '3':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")


                
#-------------------------------------------------Main menu---------------------------

def main_menu():
    fleet_manager = FleetManager()
    customer = CustomerManager()
    shipment = ShipmentManager()
    delivery = DeliveryManager()

    
    customer.shipment_manager = shipment
    shipment.customer_manager = customer
    shipment.fleet_manager = fleet_manager
    delivery.shipment_manager = shipment

    while True:
        print("\n=== Main Menu ===")
        print("1. Fleet Management")
        print("2. Customer Management")
        print("3. Shipment Management")
        print("4. Delivery Management")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            fleet_manager.fleet_management_menu()
        elif choice == '2':
            customer.customer_management_menu()
        elif choice == '3':
            shipment.shipment_management_menu()
        elif choice == '4':
            delivery.delivery_management_menu()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

            
#-----------------------------------Solving Class Recursion problem
fleet_manager = FleetManager()
customer_manager = CustomerManager()
shipment_manager = ShipmentManager()
delivery_manager = DeliveryManager()


#------linking it up

#---------------for customer manager
customer_manager.shipment_manager = shipment_manager
#---------------for shipment manager
shipment_manager.customer_manager = customer_manager
shipment_manager.fleet_manager = fleet_manager
#--------------for delivery manager
delivery_manager.shipment_manager = shipment_manager








main_menu()