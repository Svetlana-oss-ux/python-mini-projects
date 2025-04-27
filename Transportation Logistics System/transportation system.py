import os  # Used to clear the console screen.
import sys  # Provides access to exit function.
from datetime import datetime  # Enables timestamping delivery status with date and time.

# Global data structures for storing system records
fleets = []       # Stores vehicle details for the fleet management module
shipments = []    # Stores all registered shipments
deliveries = []    # Stores confirmed delivery records including timestamp


# ============================== FLEET MANAGEMENT ==============================

# Function to add a new vehicle to the fleet
def fleet_add():
    global fleets
    print("=== Add a New Vehicle ===")
    
    # Prompt for a 4-digit vehicle ID
    vehicle_id = input("Enter a 4-digit vehicle ID: ")
    
    # Validate the vehicle ID length
    if len(vehicle_id)!= 4:
        print("Error: Vehicle ID must be 4 digits.")
        input("Press Enter to continue...")
        return
    
    # Check if vehicle ID is already used
    if any(fleet["Vehicle_ID"] == vehicle_id for fleet in fleets):
        print("Error: Vehicle ID already exists.")
        input("Press Enter to continue...")
        return

    # Collect vehicle type and capacity
    vehicle_type = input("Enter the vehicle type: ")
    capacity = input("Enter the vehicle capacity (kg): ")
    
    # Ensure capacity is a positive number
    if int(capacity) < 0:
        print("Error: Capacity cannot be negative.")
        input("Press Enter to continue...")
        return

    # Add vehicle to fleet list
    fleets.append({"Vehicle_ID": vehicle_id, "Type": vehicle_type, "Capacity": capacity})
    print("Success: Vehicle added.")
    input("Press Enter to continue...")

# Function to update vehicle information
def fleet_update():
    global fleet
    print("=== Update Vehicle Info ===")
    vehicle_id = input("Enter the vehicle ID to update: ")

    # Find the vehicle in fleet list
    for fleet in fleets:
        if fleet["Vehicle_ID"] == vehicle_id:
            # Prompt user to update vehicle type
            fleet["Type"] = input("Enter new vehicle type: ")

            # Loop until a valid positive integer capacity is entered
            new_capacity = input("Enter new vehicle capacity (positive integer): ")
            if new_capacity.isdigit() and int(new_capacity) > 0:
                fleet["Capacity"] = new_capacity
                print("Vehicle information updated successfully.")
            else:
                print("Error: Capacity must be a positive integer. Update cancelled.")

            input("Press Enter to continue...")
            return

    print("Error: Vehicle ID not found.")
    input("Press Enter to continue...")

# Function to remove a vehicle
def fleet_remove():
    print("=== Remove a Vehicle ===")
    vehicle_id = input("Enter the vehicle ID to remove: ")

    # Search for vehicle in list
    for fleet in fleets:
        if fleet["Vehicle_ID"] == vehicle_id:
            confirm = input("Are you sure you want to delete this record? (y/n): ")
            if confirm.lower() == 'y':
                fleets.remove(fleet)
                print("Vehicle removed.")
            else:
                print("Deletion cancelled.")
            input("Press Enter to continue...")
            return

    print("Error: Vehicle ID not found.")
    input("Press Enter to continue...")

# Function to view all fleet vehicles
def fleet_view():
    print("=== All Fleet Vehicles ===")
    for fleet in fleets:
        print(f"Vehicle ID: {fleet['Vehicle_ID']}, Type: {fleet['Type']}, Capacity: {fleet['Capacity']}kg")
    input("Press Enter to continue...")

# Fleet Management Menu
def fleet_func():
    while True:
        os.system('cls')
        print("=== Fleet Management ===")
        print("1. Add Vehicle\n2. Update Vehicle\n3. Remove Vehicle\n4. View Fleet\n5. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            fleet_add()
        elif choice == '2':
            fleet_update()
        elif choice == '3':
            fleet_remove()
        elif choice == '4':
            fleet_view()
        elif choice == '5':
            return
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

# ============================ SHIPMENT MANAGEMENT ============================

# Function to create a new shipment
def shipment_create():
    print("=== Create New Shipment ===")
    
    # Step 1: Ask for Shipment ID and check uniqueness
    shipment_id = input("Enter Shipment ID: ")
    if any(s["Shipment_ID"] == shipment_id for s in shipments):
        print("Error: Shipment ID already exists.")
        input("Press Enter to continue...")
        return

    # Step 2: Display all available Vehicle IDs from current fleet
    print("\nAvailable Vehicle IDs:")
    if len(fleets) == 0:
        print("No vehicles available. Please add vehicles first.")
        input("Press Enter to continue...")
        return
    for f in fleets:
        print(f"- Vehicle ID: {f['Vehicle_ID']}, Type: {f['Type']}, Capacity: {f['Capacity']}kg")

    # Step 3: Ask user to select a valid Vehicle ID
    vehicle_id = input("\nEnter Vehicle ID to assign: ")
    if not any(f["Vehicle_ID"] == vehicle_id for f in fleets):
        print("Error: Invalid Vehicle ID.")
        input("Press Enter to continue...")
        return

    # Step 4: Collect other shipment details from the user
    origin = input("Enter Origin Location: ")
    destination = input("Enter Destination: ")
    
    # Step 5: Validate the shipment weight
    weight_input = input("Enter Shipment Weight (kg): ")
    if not weight_input.isdigit() or int(weight_input) < 0:
        print("Error: Weight must be a positive number.")
        input("Press Enter to continue...")
        return
    weight = int(weight_input)

    # Step 6: Store the shipment information
    shipments.append({
        "Shipment_ID": shipment_id,
        "Vehicle_ID": vehicle_id,
        "Status": "N/D",  # Not Delivered
        "Origin": origin,
        "Destination": destination,
        "Weight": weight
    })

    # Step 7: Confirm shipment creation
    print("Shipment created successfully.")
    input("Press Enter to continue...")


# Function to track a shipment status
def shipment_track():
    print("=== Track Shipment ===")
    shipment_id = input("Enter Shipment ID: ")

    # Search for shipment and report status
    for s in shipments:
        if s["Shipment_ID"] == shipment_id:
            if s["Status"] == "N/D":
                print("Shipment is in transit.")
            else:
                print("Shipment has been delivered.")
            input("Press Enter to continue...")
            return

    print("Error: Shipment ID not found.")
    input("Press Enter to continue...")

# Function to view all shipments
def shipment_view():
    print("=== All Shipments ===")
    for s in shipments:
        print(f"\nShipment ID: {s['Shipment_ID']}, Vehicle: {s['Vehicle_ID']}, Status: {s['Status']}, Origin: {s['Origin']}, Destination: {s['Destination']}, Weight: {s['Weight']}kg")
    input("\nEnter 'exit' to return to Shipment Menu: ")

# Shipment Management Menu
def shipment_func():
    while True:
        os.system('cls')
        print("=== Shipment Management ===")
        print("1. Create Shipment\n2. Track Shipment\n3. View Shipments\n4. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            shipment_create()
        elif choice == '2':
            shipment_track()
        elif choice == '3':
            shipment_view()
        elif choice == '4':
            return
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

# =========================== DELIVERY MANAGEMENT ============================

# Function to mark a shipment as delivered
def delivery_mark():
    print("=== Mark Shipment as Delivered ===")
    shipment_id = input("Enter Shipment ID: ")

    for s in shipments:
        if s["Shipment_ID"] == shipment_id:
            if s["Status"] == "N/D":
                s["Status"] = "D"  # Mark as delivered
                now = datetime.now()
                deliveries.append({
                    "Shipment_ID": shipment_id,
                    "Date": now.strftime("%Y-%m-%d"),
                    "Time": now.strftime("%H:%M:%S")
                })
                print("Shipment marked as delivered.")
            else:
                print("Shipment already delivered.")
            input("Press Enter to continue...")
            return

    print("Error: Shipment ID not found.")
    input("Press Enter to continue...")

# Function to check delivery status
def delivery_status():
    print("=== Check Delivery Status ===")
    shipment_id = input("Enter Shipment ID: ")
    
    for d in deliveries:
        if d["Shipment_ID"] == shipment_id:
            print(f"Delivered on {d['Date']} at {d['Time']}")
            input("Press Enter to continue...")
            return
    print("Shipment not yet delivered or not found.")
    input("Press Enter to continue...")

# Delivery Management Menu
def delivery_func():
    while True:
        os.system('cls')
        print("=== Delivery Management ===")
        print("1. Record Delivery\n2. View Delivery Status\n3. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            delivery_mark()
        elif choice == '2':
            delivery_status()
        elif choice == '3':
            return
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

# =============================== MAIN PROGRAM ===============================

def main():
    while True:
        os.system('cls')
        print("=== Main Menu ===")
        print("1. Fleet Management\n2. Shipment Management\n3. Delivery Management\n4. Exit Program")
        choice = input("Enter your choice: ")

        if choice == '1':
            fleet_func()
        elif choice == '2':
            shipment_func()
        elif choice == '3':
            delivery_func()
        elif choice == '4':
            print("Exiting Program. Goodbye!")
            sys.exit()
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

# Start the program
main()
