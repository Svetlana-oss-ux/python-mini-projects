import os
import sys
from datetime import datetime

fleets = []
shipments = []
deliverys = []

#-----------------------Fleet Management------------------
def fleet_add():
    print("Please add the details")
    id = str(input("Enter 4 digit vehicle ID "))
    if any(fleet['Vehicle_ID']== id for fleet in fleets ):
        print("Vehicle ID has already been registered")
        input("Press enter to continue...")
        return    
    type = input("Enter vehicle type ")
    capacity = input("Enter vehicle capacity ")
    if int(capacity) >=0:
        fleets.append({'Vehicle_ID':id,'Type':type,'Capacity':capacity})
        print("Record has been added")
        input("Press enter to continue...")
        return
    else:
        print("Invalid capacity")
        input("Press enter to continue...")
        return

def fleet_update():
    id = str(input("Enter the vehicle ID you want to edit "))
    for fleet in fleets:
        if fleet["Vehicle_ID"]==id:
            fleet["Type"] = input("Enter vehicle type ")
            fleet["Capacity"] = input("Enter vehicle capacity ")
            print("Field updated")
            input("Press enter to continue...")
            
            return
    print("Cound not find vehicle ID, try again")
    input("Press enter to continue...")
    return

def fleet_remove():
    id = str(input("Enter the vehicle ID you want to remove "))
    for fleet in fleets:
        if fleet["Vehicle_ID"]==id:
            value = input("Confirm deletion (n/y)")
            if value == 'y' or value == 'Y':
                fleets.remove(fleet)
                print("Record removed")
                input("Press enter to continue...")
                return
            if value =="n" or value == "N":
                print("Deletion cancled")
                input("Press enter to continue...")
                return
            else:
                print("Invalid option entered")
                input("Press enter to continue...")
                return
    print("Vehicle ID not found, please re-enter ID")
    input("Press enter to continue...")
    return

def fleet_view():
    print("Printing all the records")
    for fleet in fleets:
        print(f'''
    Vehicle ID : {fleet["Vehicle_ID"]}
    Type : {fleet["Type"]}
    Capacity : {fleet["Capacity"]}
              ''')
    input("Press enter to continue...")
    return

def fleet_func():
    while (True):
        os.system('cls')
        print("Welcome to Fleet Management")
        print("""
    choose your option:
    1. Add a vehicle
    2. Update vehicle information
    3. Remove a vehicle
    4. View all vehicles
    5. Quit fleet management
              """)
        value = int(input("Choose your option "))
        if value == 1:
            fleet_add()
        elif value == 2:
            fleet_update()
        elif value == 3:
            fleet_remove()
        elif value == 4:
            fleet_view()
        elif value == 5:
            main()
        else:
            print("Please choose proper option")
            input("Press enter to continue...")
                
#fleet_func()
#--------------------------Delivery function-------------------------
def delivery_mark():
    print("Welcome to Shipment Delivery")
    id = str(input("Enter your  shipment id "))
    for shipment in shipments:
        if shipment["Shipment_ID"]==id:
            if  shipment["Status"] =="N/D":
                shipment["Status"] = "D"
                
                print("Your shipment is marked delivered on")
                now = datetime.now()
                date = now.strftime("%y-%m-%d")
                time = now.strftime("%H:%M:%S")
                print(date, time)
                deliverys.append({"Shipment_ID":id,"Date":str(date),"Time":str(time)})
            else:
                print("Your shipment has already been delivered")
            input("Press enter to continue...")
            return
    print("Invalid shipment ID, please check again")
    input("Press enter to continue...")

def delivery_status():
    id = str(input("Enter the shipment ID "))     
    for delivery in deliverys:
        if delivery["Shipment_ID"] == id:
            print("Your shipment was delivered on")
            print(f"Date : {delivery['Date']}")
            print(f"Time : {delivery['Time']}")
            input("Press enter to continue...")
            return
    print("Your ID was not found")
    input("Press enter to continue...")
    return
    
def delivery_func():
    while(True):
        os.system('cls')
        print(""" 
    1. Record delivery for a shipment
    2. View delivery status for a shipment
    3. Quit delivery management
    4. Exit the code
    """)
        value = int(input("Enter your choice "))
        if value == 1:
            delivery_mark()
        elif value == 2:
            delivery_status()
        elif value == 3:
            main()
        elif value == 4:
            print("Press any key to Continue...")
            sys.quit()
        else:
            print("Invalid option")
            input()
            break
              
#delivery_func()    

#--------------------------Shipment Management-----------------         

def shipment_create():
    print("Please enter shipment details ")
    shipment_id = str(input("Enter shipment ID "))
    if any(shipment["Shipment_ID"]==shipment_id for shipment in shipments):
        print("Shipment ID already in use")
        print("Press any key to Continue...")
        return
    fleet_view()
    vehicle_id = str(input("Choose the vehicle ID "))
    if any(fleet["Vehicle_ID"]==vehicle_id for fleet in fleets):
        origin = input("Enter origin location ")
        destination = input("Enter destination location ")
        weight = int(input("Enter weight "))
        if weight < 0:
            print("Weight can not be negative")
            input("Press enter to continue...")
            return
        shipments.append({"Shipment_ID":shipment_id,"Vehicle_ID":vehicle_id,"Status":"N/D","Origin":origin,"Destination":destination,"Weight":weight})
        print("Record has been successfully added ")
        input("Press enter to continue...")
        return
    else:
        print("Cound not find entered vehicle ID ")
        input("Press enter to continue...")
        return

def shipment_track():
    shipment_id = str(input("Enter shipment ID "))
    for shipment in shipments:
        if shipment["Shipment_ID"]==shipment_id:
            if shipment["Status"]=="N/D":
                print("Shipment is in transit")
                input("Press enter to continue...")
                return
            else:
                print("Shipment has been delivered")
                input("Press enter to continue...")
                return
    print("Shipment ID not found, enter again ")
    input("Press enter to continue...")
    return

def shipment_view():
    os.system('cls')
    for shipment in shipments:
        print(f'''
Shipment ID : {shipment["Shipment_ID"]}
Vehicle ID : {shipment["Vehicle_ID"]} 
Status : {shipment["Status"]}             
Origin : {shipment["Origin"]}
Destination : {shipment["Destination"]}
Weingt : {shipment["Weight"]}
              ''')
    value = input("Enter (exit) to return to shipment menu ")
    if value == "exit":
        return
    else:
        shipment_view()
    
def shipment_func():
    while(True):
        os.system('cls')
        print("Welcome to shipment Management")
        print("""
    1. Create a new shipment
    2. Track a shipment
    3. View all shipments
    4. Quit shipment management
              """)
        value = int(input("Enter your option "))
        if value == 1:
            shipment_create()
        elif value == 2:
            shipment_track()
        elif value == 3:
            shipment_view()
        elif value == 4:
            main()              
        else:
            print("Enter valid option")
            input("Press enter to continue...")
            return
        

#shipment_func()
#--------------------------Main()------------------------------              
def main():
    while (True):
        os.system('cls')
        print ("Welcome to Main menu")
        print("""
    1. Fleet Management
    2. Shipment Management
    3. Delivery Management
    4. Quit Application """)
        value = int(input("Enter your option "))
        if value == 1:
            fleet_func()
        elif value == 2:
            shipment_func()
        elif value == 3:
            delivery_func()
        elif value == 4:
            print("Press any key to Continue...")
            sys.quit()
        else:
            print("Invalid option")
            input("Press enter to continue...")
main()
