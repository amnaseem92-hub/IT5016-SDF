# -----------------------------------------
# Task 4: Display Requisitions            #
# -----------------------------------------

def display_requisitions():
    req_counter = 0
    total, status, date_ , staff_id, staff_name, req_id, approval_ref = requisition_approval()
     
    print("\nPrinting Requisitions:\n")
    print(f"Date: {date_}")
    print(f"Requisition ID: {req_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    
    if approval_ref:
        print(f"Approval Reference Number: {approval_ref}")

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
           
    return total, status, date_ , staff_id, staff_name, req_id, approval_ref

def requisitions_total():
    staff_details = staff_info()
    
    total = 0       
    while True:
        itemName = input("Type the item name Or (p or 'print') to see all 'Printing Requisitions': ")
        if itemName.lower() == "p" or itemName.lower() == "print":
            break
        
        while True:
            try:
                price = float(input(f"Enter price for {itemName}: $"))
                break   
            except ValueError:
                print("Invalid input. Please enter a valid floting point numeric value. Example: 112.11")
    
        total += price
    
    return total, staff_details

def staff_info():
    req_counter = 0
    req_counter += 1
    
    # Collect input from user
    date = input("Enter Date (dd/mm/yyyy): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    
    # Generate requisition ID
    req_id = 10000 + req_counter
    return date, staff_id, staff_name, req_id

display_requisitions()