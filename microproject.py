from collections import deque
import heapq
 
donors = []
receivers = []
volunteers = []
 
donations = {}
priority_queue = []
pickup_queue = deque()
delivery_history = []
 
donation_counter = 1
receiver_counter = 1
volunteer_counter = 1
 
 
def add_donor():
    name = input("Enter donor name: ")
    location = input("Enter donor location: ")
    phone = input("Enter phone number: ")
 
    donor = {
        "name": name,
        "location": location,
        "phone": phone
    }
 
    donors.append(donor)
    print("Donor added successfully.")
 
 
def add_receiver():
    global receiver_counter
 
    name = input("Enter receiver name: ")
    location = input("Enter receiver location: ")
    required = int(input("Enter required quantity (meals): "))
 
    receiver = {
        "id": receiver_counter,
        "name": name,
        "location": location,
        "required": required
    }
 
    receivers.append(receiver)
    print("Receiver ID:", receiver_counter)
    receiver_counter += 1
 
 
def add_volunteer():
    global volunteer_counter
 
    name = input("Enter volunteer name: ")
    location = input("Enter volunteer location: ")
 
    volunteer = {
        "id": volunteer_counter,
        "name": name,
        "location": location,
        "available": True
    }
 
    volunteers.append(volunteer)
    print("Volunteer ID:", volunteer_counter)
    volunteer_counter += 1
 
 
def get_priority(expiry_hours):
    if expiry_hours <= 1:
        return 1, "Critical"
    elif expiry_hours <= 3:
        return 2, "High"
    elif expiry_hours <= 6:
        return 3, "Medium"
    else:
        return 4, "Low"
 
 
def add_donation():
    global donation_counter
 
    donor = input("Enter donor name: ")
    food = input("Enter food name: ")
    quantity = int(input("Enter quantity (meals): "))
    location = input("Enter food location: ")
    expiry = float(input("Enter expiry time in hours: "))
 
    priority, level = get_priority(expiry)
 
    donation = {
        "id": donation_counter,
        "donor": donor,
        "food": food,
        "quantity": quantity,
        "location": location,
        "expiry": expiry,
        "priority": priority,
        "level": level,
        "status": "Available"
    }
 
    donations[donation_counter] = donation
 
    heapq.heappush(
        priority_queue,
        (priority, expiry, donation_counter)
    )
 
    print("Donation added successfully.")
    print("Donation ID:", donation_counter)
    print("Priority:", level)
 
    donation_counter += 1
 
 
def view_donations():
    if not donations:
        print("No donations available.")
        return
 
    print("\n--- FOOD DONATIONS ---")
 
    for d in donations.values():
        print(
            "ID:", d["id"],
            "| Food:", d["food"],
            "| Quantity:", d["quantity"],
            "| Priority:", d["level"],
            "| Status:", d["status"]
        )
 
 
def match_food():
    if not receivers:
        print("No receivers registered.")
        return
 
    receiver_id = int(input("Enter receiver ID: "))
 
    receiver = None
    for r in receivers:
        if r["id"] == receiver_id:
            receiver = r
            break
 
    if receiver is None:
        print("Receiver not found.")
        return
 
    required = receiver["required"]
 
    temp = []
    matched = None
 
    while priority_queue:
        priority, expiry, donation_id = heapq.heappop(priority_queue)
 
        donation = donations[donation_id]
 
        if donation["status"] == "Available" and donation["quantity"] >= required:
            matched = donation
            break
 
        temp.append((priority, expiry, donation_id))
 
    for item in temp:
        heapq.heappush(priority_queue, item)
 
    if matched is None:
        print("No suitable food donation found.")
        return
 
    matched["status"] = "Reserved"
 
    request = {
        "donation_id": matched["id"],
        "receiver_id": receiver["id"],
        "receiver_name": receiver["name"],
        "food": matched["food"],
        "quantity": required
    }
 
    pickup_queue.append(request)
 
    print("Food matched successfully.")
    print("Pickup request added to queue.")
 
 
def process_pickup():
    if not pickup_queue:
        print("No pending pickup requests.")
        return
 
    available_volunteer = None
 
    for volunteer in volunteers:
        if volunteer["available"]:
            available_volunteer = volunteer
            break
 
    if available_volunteer is None:
        print("No volunteer is currently available.")
        return
 
    request = pickup_queue.popleft()
    donation = donations[request["donation_id"]]
 
    available_volunteer["available"] = False
 
    delivery = {
        "donation_id": donation["id"],
        "food": request["food"],
        "quantity": request["quantity"],
        "receiver": request["receiver_name"],
        "volunteer": available_volunteer["name"]
    }
 
    delivery_history.append(delivery)
 
    donation["quantity"] -= request["quantity"]
 
    if donation["quantity"] > 0:
        donation["status"] = "Available"
    else:
        donation["status"] = "Delivered"
 
    available_volunteer["available"] = True
 
    print("Pickup processed successfully.")
    print("Volunteer:", available_volunteer["name"])
    print("Delivery completed.")
 
 
def view_history():
    if not delivery_history:
        print("No completed deliveries.")
        return
 
    print("\n--- DELIVERY HISTORY ---")
 
    for delivery in reversed(delivery_history):
        print(
            "Food:", delivery["food"],
            "| Quantity:", delivery["quantity"],
            "| Receiver:", delivery["receiver"],
            "| Volunteer:", delivery["volunteer"]
        )
 
 
def dashboard():
    print("\n--- FOOD RESCUE NETWORK ---")
    print("Total donors:", len(donors))
    print("Total receivers:", len(receivers))
    print("Total volunteers:", len(volunteers))
    print("Total donations:", len(donations))
    print("Pending pickups:", len(pickup_queue))
    print("Completed deliveries:", len(delivery_history))
 
 
def main():
    while True:
        print("\n========== FOOD RESCUE NETWORK ==========")
        print("1. Add Donor")
        print("2. Add Food Donation")
        print("3. Add Receiver")
        print("4. Add Volunteer")
        print("5. View Donations")
        print("6. Match Food")
        print("7. Process Pickup")
        print("8. View Delivery History")
        print("9. Dashboard")
        print("0. Exit")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            add_donor()
        elif choice == "2":
            add_donation()
        elif choice == "3":
            add_receiver()
        elif choice == "4":
            add_volunteer()
        elif choice == "5":
            view_donations()
        elif choice == "6":
            match_food()
        elif choice == "7":
            process_pickup()
        elif choice == "8":
            view_history()
        elif choice == "9":
            dashboard()
        elif choice == "0":
            print("Thank you for using Food Rescue Network.")
            break
        else:
            print("Invalid choice. Please try again.")
 
 
if __name__ == "__main__":
    main()
