# requisitionsystem.py
# Global variable
req_counter = 0

class RequisitionSystem:
    all_requisitions = []   # class-level list to track all requisitions

    # "def __init__(self):" This defines a special method in a class called the constructor.
    # It is automatically called every time you create a new object (instance) of the class.
    def __init__(self):
        # Call staff_info to collect details
        staff_date, staff_code, staff_name, req_id = self.staff_info()
        # Assign to instance variables
        self.date = staff_date
        self.staff_id = staff_code
        self.staff_name = staff_name
        self.requisition_id = req_id
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not Available"
        RequisitionSystem.all_requisitions.append(self)

    def staff_info(self):
        global req_counter
        req_counter += 1
        
        # Collect input from user      
        print(f"\nRequisition No.{req_counter}")
        date = input("\nEnter Date (dd/mm/yyyy): ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")
        
        # Create requisition ID
        req_id = 10000 + req_counter
        return date, staff_id, staff_name, req_id

    # Sum up all requisitions total
    def requisitions_details(self, items_with_prices):
        self.items = items_with_prices
        self.total = sum(price for _, price in items_with_prices)
        return self.total

    # Auto-approval if Total is < 500
    def requisition_approval(self):
        self.approval_ref = "Not Available"
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        else:
            self.status = "Pending"            
        return self.status

    # Manager response for pending requisitions
    def respond_requisition(self, decision):
        if self.status == "Pending":
            if decision.lower() == "approve" or decision.lower() == "approved":
                self.status = "Approved"
                self.approval_ref = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            elif decision.lower() == "not approve" or decision.lower() == "not approved":
                self.status = "Not Approved"
                self.approval_ref = "Not Available"
        return self.status

    # Display requisition details
    def display_requisitions(self):        
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")
        print("\n")

    # Statistics of all requisitions
    @classmethod
    def requisition_statistic(cls):
        # "len" keyword returns the number of items (length) in a collection
        total_submitted = len(cls.all_requisitions)
        
        #total_approved = sum(1 for r in cls.all_requisitions if r.status == "Approved")
        total_approved = 0  # start counter
        for r in cls.all_requisitions:
            if r.status == "Approved":
                total_approved += 1
        
        #total_pending = sum(1 for r in cls.all_requisitions if r.status == "Pending")
        total_pending = 0  # start counter
        for r in cls.all_requisitions:
            if r.status == "Pending":
                total_pending += 1

        
        #total_not_approved = sum(1 for r in cls.all_requisitions if r.status == "Not Approved")
        total_not_approved = 0  # start counter
        for r in cls.all_requisitions:
            if r.status == "Not Approved":
                total_not_approved += 1

        print("\nStatistics:")
        print("Displaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {total_submitted}")
        print(f"The total number of approved requisitions: {total_approved}")
        print(f"The total number of pending requisitions: {total_pending}")
        print(f"The total number of not approved requisitions: {total_not_approved}")

# -------------------------------------------------------
# Interactive User Input - Execution Starting from here
# ------------------------------------------------------
# The code line if "__name__ == "__main__":"" runs the interactive part of the program (user inputs, approvals, etc.) 
#       only if we run requisitionsystem.py directly. This line ensure that this is starting point of execution.
if __name__ == "__main__":
    num_reqs = int(input("How many requisitions do you want to submit? "))
    print("\n")
    for _ in range(num_reqs):
        # Call to RequisitionSystem class       
        requisition = RequisitionSystem()

        # Enter items
        items = []
        print("\n-----Entries for requisition items starting------")
        print("Enter requisition items (type 'done' when finished):")
        while True:
            item_name = input("Item name (or 'done' to finish): ")
            if item_name.lower() == "done":
                break
            try:
                price = float(input(f"Enter price for {item_name}: $"))
                items.append((item_name, price))
            except ValueError:
                print("Invalid price. Please enter a floating point number (Example: 122.12).")

        requisition.requisitions_details(items)
        requisition.requisition_approval()

    # Manager approval for pending requisitions
    print("\n--- Manager's Review ---")
    for r in RequisitionSystem.all_requisitions:
        if r.status == "Pending":
            while True:
                print(f"Requisition Info-> Requisition Id :{r.requisition_id} , Requisition Total : {r.total}")
                decision = input("Enter decision (approve / not approved / skip): ").strip().lower()
                if decision in ["approve","approved","not approve", "not approved", "skip"]:
                    r.respond_requisition(decision)
                    print("\n")
                    break
                else:
                    print("Invalid input. Please type one of these: approve / not approved / skip.")
           
    # Show final results and statistics
    print("\n--- Final Requisition List ---")
    print("\nPrinting Requisitions:")
    counter_req = 1
    for r in RequisitionSystem.all_requisitions:
        print(f"\nRequisition No. {counter_req}")
        r.display_requisitions()
        counter_req += 1

    RequisitionSystem.requisition_statistic()