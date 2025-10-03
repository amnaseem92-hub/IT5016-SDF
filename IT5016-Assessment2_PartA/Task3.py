# ----------------------------
# Task 1: Staff Information
# ----------------------------
req_counter = 0  # global counter 

def staff_info():
    global req_counter
    req_counter += 1
    
    # Collect input from user
    date = input("Enter Date (dd/mm/yyyy): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    
    # Generate requisition ID
    req_id = 10000 + req_counter
    
    return date, staff_id, staff_name, req_id

def requisitions_total():
    staff_details = staff_info()
    
    total = 0
    print("\nEnter requisition items (type E/e to finish):")
    
    while True:
        itemName = input("Type the item name (or enter E/e to quit): ")
        if itemName.lower() == "e":
            break
        
        price = float(input(f"Enter price for {itemName}: $"))
        total += price
    
    return total, staff_details

def requisition_approval():
    total, staff_details = requisitions_total()
    date_, staff_id, staff_name, req_id = staff_details
    
    # Default status
    status = "Pending"
    approval_ref = None
    
    # Auto-approval rule
    if total < 500:
        status = "Approved"
        approval_ref = f"{staff_id}{str(req_id)[-3:]}"
    
    # Print decision
    print("\n--- Requisition Approval ---")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    if approval_ref:
        print(f"Approval Reference Number: {approval_ref}")
    
# Call function requisition_approval() for Task 3
requisition_approval()