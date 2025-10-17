# IT5016 - Software Development Fundamentals  
## Week 2 Lab Session - Python Scenarios (1-9)

**Student Name:** Ammara Naseem  
**Student ID:** 20251562  

---

## Overview
This repository includes nine independent Python scripts created as part of the Week 2 Lab Session for the IT5016 Software Development Fundamentals course.  
Each scenario demonstrates essential Python programming concepts such as **conditional statements**, **loops**, **input handling**, and **basic validation logic**.

The collection of exercises progressively builds problem-solving skills by applying programming logic to real-life examples like grading, ATM withdrawal, and password verification.

---

## Scenario Summaries

### Scenario 1 - Even or Odd and Divisible by 5
**File:** 'Week2_LabSession_Scen1.py'  
This program asks the user to input a number and checks whether it is **even or odd** and whether it is **divisible by 5**.  
It uses nested 'if' statements and demonstrates logical operators ('%' and 'and') for multiple condition checks:contentReference[oaicite:0]{index=0}.

**Concepts Used:**  
- Arithmetic operators  
- Conditional branching ('if-else')  
- Boolean logic  

---

### Scenario 2 - Grade Evaluation System
**File:** 'Week2_LabSession_Scen2.py'  
The user enters a numeric score, and the program assigns a grade (A-F) based on score ranges.  
It also validates that the score lies within 0-100, displaying appropriate feedback for invalid entries:contentReference[oaicite:1]{index=1}.

**Concepts Used:**  
- Multi-branch 'if-elif-else' statements  
- Range validation  
- Conditional ordering  

---

### Scenario 3 - Voting Eligibility Checker
**File:** 'Week2_LabSession_Scen3.py'  
This script determines voting eligibility and identifies senior citizens based on the user's age.  
It ensures input validation to avoid negative or unrealistic age values

**Concepts Used:**  
- Comparison operators  
- Logical conjunction ('and')  
- Hierarchical decision logic  

---

### Scenario 4 - Temperature Conversion and Weather Description
**File:** 'Week2_LabSession_Scen4.py'  
Converts Fahrenheit input to Celsius and classifies the day as **hot**, **warm**, or **cold**.  
It also flags extreme conditions when temperature values are outside reasonable limits

**Concepts Used:**  
- Mathematical conversion formula  
- Conditional evaluation  
- Sequential control structure  

---

### Scenario 5 - ATM Withdrawal Simulation
**File:** 'Week2_LabSession_Scen5.py'  
Simulates an ATM machine validating PIN and withdrawal conditions.  
The program checks for sufficient balance, validates denominations, and displays updated balance after a successful transaction

**Concepts Used:**  
- Nested conditionals  
- Input validation  
- Arithmetic updates on variables  

---

### Scenario 6 - Password Retry Mechanism
**File:** 'Week2_LabSession_Scen6.py'  
Implements a password-based access system with a limited number of attempts.  
If the user fails ten times, access is denied; successful entry immediately grants access

**Concepts Used:**  
- While loops  
- Decrementing counters  
- Conditional termination using 'break'  

---

### Scenario 7 - Enhanced Password Lockout System
**File:** 'Week2_LabSession_Scen7.py'  
An advanced version of Scenario 6 that locks the user out for 10 seconds after three failed attempts.  
The script uses 'time.sleep()' to introduce a delay, adding realism to authentication systems

**Concepts Used:**  
- Loops with counters  
- Time-based control ('time.sleep()')  
- Condition-triggered events  

---

### Scenario 8 - Positive Number Validator
**File:** 'Week2_LabSession_Scen8.py'  
Prompts users until they enter a **positive number**. Once valid input is received, it evaluates divisibility conditions.  
The loop continues until criteria are met, ensuring correct user behavior

**Concepts Used:**  
- While loop for input validation  
- Logical conditions with 'and'  
- Defensive programming  

---

### Scenario 9 - Grade and Feedback System
**File:** 'Week2_LabSession_Scen9.py'  
Extends Scenario 2 by adding qualitative feedback such as "Excellent", "Good", or "Satisfactory" based on grade ranges.  
Handles invalid inputs and displays motivational feedback messages

**Concepts Used:**  
- Conditional nesting  
- Range checks  
- String output formatting  

---

## Programming Principles Demonstrated

| Principle | Explanation |
|------------|-------------|
| **Input Validation** | Ensures user inputs are within acceptable limits before processing. |
| **Iteration** | Repeatedly asks for inputs or retries until a condition is met. |
| **Selection** | Uses 'if-elif-else' to choose different outcomes based on logic. |
| **Code Readability** | Uses clear indentation, spacing, and descriptive variable names. |
| **Error Prevention** | Handles unrealistic inputs (negative values, incorrect PINs, etc.). |

---

## Learning Reflection
Developing these scenarios improved understanding of **flow control** and **decision-making** in Python.  
Each exercise reinforced how loops and conditions work together to manage user-driven programs.  
Additionally, introducing real-world elements like ATM systems and authentication helped bridge theoretical logic with practical applications.

---

## References
- Python Software Foundation. (2024). *Python 3 Documentation.* Retrieved from https://docs.python.org/3/  
- W3Schools. (2024). *Python Conditional Statements and Loops.* Retrieved from https://www.w3schools.com/python/python_conditions.asp  
- Real Python. (2023). *Practical Examples of Loops and Conditionals in Python.* Retrieved from https://realpython.com/  

---

*This README file is created as part of the IT5016 Week 2 Lab Session and reflects independent coding work by Ammara Naseem.*