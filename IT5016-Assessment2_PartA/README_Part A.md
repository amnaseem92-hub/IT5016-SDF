# Python Requisition System  
### IT5016 – Software Development Fundamentals  

---

## 1. Introduction  
This document explains the development process, design logic, and applied software engineering principles behind the Python Requisition System. The project was designed as a structured implementation of the Software Development Lifecycle (SDLC), progressing through the stages of planning, analysis, design, implementation, testing, and deployment.  

The Requisition System automates the process of creating, submitting, and approving staff requisitions. It provides functionality for staff information management, cost calculation, and automated approval status generation. Development was carried out in incremental phases across four main Python tasks (`Task1.py` – `Task4.py`), culminating in a complete class-based program (`requisitionsystem.py`).

---

## 2. System Overview  
The final program enables staff to enter requisition details, compute the total value, and automatically determine whether approval is granted or pending. Managerial users can review pending requests and make final decisions. The system records all submissions for statistical reporting.  

Each file contributed to the development as follows:  
- **Task 1 – `staff_info()`**: Captures date, staff ID, and staff name; generates a unique requisition ID.  
- **Task 2 – `requisitions_total()`**: Collects item names and prices; calculates cumulative total.  
- **Task 3 – `requisition_approval()`**: Applies conditional logic to approve or hold requests based on cost thresholds.  
- **Task 4 – `display_requisitions()`**: Presents formatted requisition information to the user.  
- **`requisitionsystem.py`**: Integrates all functions within a class structure and adds features for manager response and statistical summaries.  

---

## 3. Application of Software Design Principles  

### 3.1 Modularity and Separation of Concerns  
Each Python script addresses a distinct responsibility, illustrating the *Single Responsibility Principle (SRP)*. For example, the staff-information module (`Task1.py`) focuses solely on input capture, while the total-computation module (`Task2.py`) manages financial aggregation. This separation simplifies maintenance and promotes clear code readability.  

### 3.2 Reusability and Extensibility  
Functions were written to return values that can be reused by other modules. For instance, `staff_info()` returns a tuple of staff details that is later passed into `requisitions_total()`. This design encourages code reuse and facilitates the addition of new modules—such as database or web interfaces—without modifying the core logic.  

### 3.3 Encapsulation and Data Abstraction  
In the consolidated version (`requisitionsystem.py`), a class named `RequisitionSystem` encapsulates related data and methods. The class hides implementation details while exposing essential methods like `requisitions_details()` and `requisition_approval()`. This object-oriented structure maintains data integrity and enhances maintainability.  

### 3.4 Input Validation and Error Handling  
To ensure data reliability, the program employs defensive programming techniques. Numeric conversions are wrapped in exception handling blocks to prevent runtime errors:  
```python
try:
    price = float(input(f"Enter price for {item_name}: $"))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
```  
Such validation ensures accurate user interaction and supports robust system behaviour.

### 3.5 Logic Automation and Decision Control  
The system demonstrates algorithmic decision-making through conditional statements.  
```python
if total < 500:
    status = "Approved"
else:
    status = "Pending"
```  
This rule automates the approval process and enforces organizational policy consistently, demonstrating how business rules can be embedded in program logic.  

### 3.6 Iterative Development under SDLC  
The project embodies SDLC principles. Each stage built upon the previous one:  
| SDLC Stage | Application in Project |
|-------------|------------------------|
| **Planning** | Defined the need for requisition automation. |
| **Analysis** | Identified system inputs, outputs, and conditions. |
| **Design** | Outlined program structure and data flow. |
| **Implementation** | Developed and tested modules incrementally. |
| **Testing** | Conducted functional and error-handling validation. |
| **Deployment** | Released a working console-based application. |

---

## 4. Development Process Summary  

The following text-based diagram represents the logical integration of modules:  

```
+-------------------+
|   Task1.py        | --> Staff information & requisition ID
+-------------------+
          |
          v
+-------------------+
|   Task2.py        | --> Item entry & total calculation
+-------------------+
          |
          v
+-------------------+
|   Task3.py        | --> Approval status logic
+-------------------+
          |
          v
+-------------------+
|   Task4.py        | --> Output and summary display
+-------------------+
          |
          v
+---------------------------+
|  requisitionsystem.py     | --> Full integration & statistics
+---------------------------+
```

This workflow demonstrates incremental construction—a key feature of iterative SDLC development. Each task was fully verified before moving to the next phase to reduce dependency errors.

---

## 5. Research Discussion  
The project applies foundational concepts from both software engineering and object-oriented programming research. The design reflects best practices in modularity, abstraction, and encapsulation, as recommended in current academic and industry guidelines (Microsoft, 2024; GeeksforGeeks, 2024).  

From a software-engineering perspective, this project exemplifies how small-scale applications can model professional SDLC practices. The use of incremental tasks mirrors agile methodologies, enabling refinement through continuous feedback. Research also supports the approach of using error-resilient input handling and function reuse as effective techniques for improving code reliability and maintainability.

---

## 6. Conclusion  
The Python Requisition System demonstrates the effective use of SDLC methodology in a small-scale academic project. By following a structured design process, applying modular and object-oriented principles, and enforcing validation mechanisms, the software achieves clarity, scalability, and robustness. The project reflects the developer’s understanding of software architecture, systematic design, and research-informed practice in modern software development.

---

## 7. References  
- GeeksforGeeks. (2024). *Software development life cycle (SDLC) models and phases.* Retrieved from https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/  
- Microsoft. (2024). *Software development lifecycle (SDLC) best practices.* Retrieved from https://learn.microsoft.com/  
- W3Schools. (2024). *Python functions and classes.* Retrieved from https://www.w3schools.com/python/  
- Student Project Files. (2025). *Task1.py, Task2.py, Task3.py, Task4.py, requisitionsystem.py.* Internal repository.
