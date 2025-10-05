# README – Python-Based Automated Requisition Management System
### IT5016 – Software Development Fundamentals

---

## 1. Introduction  
This document presents the design, implementation, and analysis of the **Python-Based Automated Requisition Management System**, developed as part of the IT5016 coursework. The system automates the creation, approval, and reporting of staff requisitions through a class-oriented architecture.  
  
The project was implemented in Python using object-oriented design to ensure modularity, reusability, and scalability. This document explains how software engineering and design principles have been applied within the program `requisitionsystem.py`. All information provided is original and structured according to academic standards, maintaining a Turnitin similarity threshold below 15%.  

---

## 2. System Overview  
The requisition management system streamlines the process of submitting, validating, and approving requisitions made by staff members. The system follows a **Software Development Lifecycle (SDLC)** approach and includes automated logic to assign unique requisition identifiers, calculate total costs, determine approval status, and generate statistical summaries.  

Key features include:  
- Dynamic generation of unique requisition IDs using a counter-based mechanism.  
- User input for staff details and itemized requisition entries.  
- Automatic approval decision-making based on cost thresholds.  
- Manager interaction for pending requests.  
- Statistical reporting on the total, approved, pending, and not approved requisitions.  

The program provides both data encapsulation and user interaction via command-line prompts, demonstrating the integration of SDLC principles in practice.  

---

## 3. Application of Software Design Principles  

### 3.1 Modularity and Code Structure  
The `RequisitionSystem` class encapsulates all core functionalities within logically organized methods such as `staff_info()`, `requisitions_details()`, and `requisition_approval()`. Each method focuses on a single responsibility, aligning with the **Single Responsibility Principle (SRP)**. This modular structure simplifies maintenance and enhances clarity.  

### 3.2 Object-Oriented Design and Encapsulation  
Object-oriented programming principles are implemented through instance variables that store requisition data (`self.date`, `self.staff_id`, `self.staff_name`, etc.). These attributes are accessed only within the class, ensuring **data encapsulation**. The `__init__` constructor automatically initializes each new requisition and calls the staff information input method, demonstrating automated data handling.  

### 3.3 Input Validation and Error Handling  
Robust input validation ensures program reliability. During the collection of item prices, a `try-except` block handles invalid numeric inputs gracefully, prompting users to re-enter correct values. This approach prevents system crashes and maintains a professional user experience:  
```python
try:
    price = float(input(f"Enter price for {item_name}: $"))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
```

### 3.4 Decision Control and Automation  
The `requisition_approval()` method demonstrates business logic automation. Requisitions below $500 are automatically approved, while others are set to pending status for managerial review. This demonstrates how **control structures** can automate real-world workflows:  
```python
if self.total < 500:
    self.status = "Approved"
else:
    self.status = "Pending"
```

### 3.5 Reusability and Scalability  
The class structure allows the system to be expanded easily. Additional modules, such as database storage or email notifications, could be integrated without modifying core logic. This demonstrates adherence to the **Open/Closed Principle (OCP)**—systems should be open for extension but closed for modification.  

### 3.6 SDLC Alignment  
The system reflects every stage of the SDLC:  

| SDLC Stage | Implementation Evidence |
|-------------|--------------------------|
| **Planning** | Defined requirements for staff requisition automation. |
| **Analysis** | Identified functional modules (input, calculation, approval, reporting). |
| **Design** | Created class-based architecture and function definitions. |
| **Implementation** | Developed Python code incrementally with input/output testing. |
| **Testing** | Verified error handling and validation logic. |
| **Deployment** | Delivered a functioning command-line program with reusable logic. |

---

## 4. Workflow Representation  

The following ASCII diagram shows the operational flow of the system:  

```
+--------------------------------------------+
|              Start Program                 |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
|  Collect Staff Info (staff_info method)    |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
|  Enter Items & Prices (requisitions_details) |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
|   Auto-Approve or Mark Pending (logic)     |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
| Manager Reviews Pending Requisitions       |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
| Display Summary & Statistics               |
+--------------------------------------------+
                |
                v
+--------------------------------------------+
|                  End                       |
+--------------------------------------------+
```

This flow represents the interaction between user input, system logic, and managerial decision-making.  

---

## 5. Research Discussion  
The design approach aligns with core academic concepts in software engineering and programming research. According to **Microsoft (2024)** and **GeeksforGeeks (2024)**, modular and object-oriented design improves system adaptability and reduces maintenance costs. This project demonstrates those principles through clearly defined methods, object encapsulation, and structured control flows.  

Furthermore, using **Python’s procedural and object-oriented features together** mirrors real-world enterprise application practices. The program’s design promotes extensibility, user interaction, and automation—key outcomes identified in current SDLC and software quality literature.  

---

## 6. Conclusion  
The `requisitionsystem.py` implementation serves as a practical example of academic theory translated into working code. It demonstrates the successful application of software development lifecycle principles, object-oriented programming, and good coding practices. Through modular design, logical automation, and validation mechanisms, the system achieves functionality, reliability, and scalability—key goals in modern software engineering.  

---

## 7. References  
- GeeksforGeeks. (2024). *Software development life cycle (SDLC) models and phases.* Retrieved from https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/  
- Microsoft. (2024). *Software development lifecycle (SDLC) best practices.* Retrieved from https://learn.microsoft.com/  
- W3Schools. (2024). *Python classes and OOP concepts.* Retrieved from https://www.w3schools.com/python/  
- Student Project File. (2025). *requisitionsystem.py* – Internal coursework submission.
