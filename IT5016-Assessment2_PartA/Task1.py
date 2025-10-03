# Global counter 
req_counter = 0  

def staff_info():
    global req_counter
    req_counter += 1   # Increase counter each time function is called
    
    # Collect input of user
    date = input("Enter Date (dd/mm/yyyy): ")
    staffId = input("Enter Staff ID: ")
    staffName = input("Enter Staff Name: ")
    
    # Generate requisition ID
    req_id = 10000 + req_counter
    
    # Print staff information
    print("\nPrinting Staff Information:\n")
    print(f"Date: {date}")
    print(f"Staff ID: {staffId}")
    print(f"Staff Name: {staffName}")
    print(f"Requisition ID: {req_id}")
    
    return date, staffId, staffName, req_id

# run Task1
staff_info()