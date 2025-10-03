# Global counter 
req_counter = 0  

def staff_info():
    global req_counter
    req_counter += 1   # Increase counter for unique requisition ID
    
    # Collect input from the user
    date = input("Enter Date (dd/mm/yyyy): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    
    # Generate requisition ID
    req_id = 10000 + req_counter
        
    return date, staff_id, staff_name, req_id

def requisitions_total():
    # Call staff_info function
    staff_details = staff_info()
    
    total = 0
        
    while True:
        itemName = input("Type the item name (or enter E/e to quit): ")
        if itemName.lower() == "e":
            break
        
        price = float(input(f"Enter price for {itemName}: $"))
        total += price
        
    print(f"\nTotal requisition value: ${total}")
    return total

requisitions_total()