**IT5016 -- Software Development Fundamentals**

**Assessment 3: Combined Report (Parts A & B)**

**Name:** Ammara Naseem\
**Student ID:** 20251562\
**Course Code:** IT5016

**GitHub Repository Links**

Below are the links to my GitHub repositories that contain all the code
files I developed during this course.

<https://github.com/amnaseem92-hub/IT5016-SDF/tree/main>

<https://github.com/amnaseem92-hub/IT5016-SDF/tree/main/IT5016-Assessment2_PartA>

https://github.com/amnaseem92-hub/IT5016-SDF/tree/main/IT5016-Assessment2_PartB

**Abstract**

This report presents an integrated overview of software development
principles and their application through Python programming. It combines
theoretical aspects of the Software Development Lifecycle (SDLC) with
the practical design of a requisition management system prototype and
foundational Python functions. The report discusses the planning,
design, and implementation of Python-based solutions emphasizing
modularity, input validation, and logical workflows. Through the
application of structured programming concepts and object-oriented
design, the project highlights how software engineering principles
enhance code clarity, maintainability, and scalability. This analysis
connects technical development practices with professional standards to
demonstrate a comprehensive understanding of functional software design
using Python.

**1. Introduction**

The purpose of this assessment was to integrate fundamental programming
concepts with core software development processes. The project was
divided into two major components: the first part focused on basic
Python function development, while the second part emphasized the
application of SDLC principles in designing a functional requisition
management system. The tasks aimed to strengthen understanding of
structured programming, modular function design, reusability, and user
interaction through a clear, step-by-step approach to problem-solving.

**2. System Overview**

The system was designed using Python to simulate real-world programming
practices and demonstrate the relationship between functional design and
structured logic.

**2.1 Part A -- Python Function Tasks**

Part A introduced essential programming tasks focused on defining and
calling functions. These tasks covered single and multiple parameters,
return values, and default arguments. Students created small programs
such as greetings, arithmetic functions, and problem-solving tasks to
develop strong foundations in modular design. The logic emphasized
reusability and readability by separating computation and user
interaction.

**2.2 Part B -- Requisition Management System**

Part B focused on developing a small-scale automated requisition system
to simulate a real-world workflow. The system allowed staff to enter
requisition details, calculate totals, and determine approval status
automatically based on defined conditions. It used object-oriented
design principles such as encapsulation and class-level variables to
manage global data like requisition counters. The solution also featured
user input validation, dynamic approval logic, and statistical analysis
of requisition outcomes.

**3. Application of the Software Development Lifecycle (SDLC)**

The SDLC framework was systematically applied throughout the design and
development stages of this project.

**3.1 Planning**

The planning phase involved identifying the main objectives---creating
modular, interactive Python applications that demonstrate best practices
in software design. Project requirements such as user input handling,
automated ID generation, and approval mechanisms were clearly defined.

**3.2 Analysis**

During the analysis stage, the problem was broken down into smaller
components. Functional requirements were established for each task, such
as input, processing, and output steps. Logical data flows were analyzed
to ensure efficiency and correctness.

**3.3 Design**

In the design phase, each function was structured to perform a single,
well-defined operation. For instance, in the requisition system, one
function collected staff information, another calculated totals, and
another handled approvals. The program followed modular principles,
allowing each component to be developed and tested independently.

**3.4 Implementation**

The implementation stage involved translating the designs into Python
code. Python's simplicity and readability helped maintain consistent
syntax and structure. Exception handling and loops were added to enhance
user interaction and prevent invalid input. The project showcased good
programming practices such as using global counters, class methods, and
reusability across functions.

**3.5 Testing**

Testing was conducted by running the system with different inputs to
ensure expected outcomes. Edge cases, such as invalid numeric input or
large requisition totals, were also evaluated to confirm program
robustness.

**3.6 Deployment**

Although this was a prototype, deployment considerations included how
the program could later be expanded with databases, file I/O, and web
integration. The system design supports scalability for future
development.

**4. Application of Software Design Principles**

**4.1 Modularity**

Each Python function and class in the project was designed to perform
one specific task. This modularity allowed easier debugging, testing,
and reusability.

**4.2 Encapsulation**

The requisition system used a class-based approach to encapsulate staff
data, requisition totals, and approval logic. This kept related data and
functions organized within a single logical unit.

**4.3 Reusability**

Functions such as staff_info, requisitions_total, and
requisition_approval were reusable across multiple scenarios.
Reusability reduces redundancy and promotes cleaner, maintainable code.

**4.4 Input Validation**

User input was validated to prevent invalid data entry. For example,
numeric fields like quantity and price were restricted to valid positive
numbers, ensuring program stability.

**4.5 Automation Logic**

The system automatically approved requisitions below a specified amount,
while pending approvals required manual review. This logical automation
simulated real-world workflows, improving efficiency and reducing human
error.

**5. Workflow Representation**

The general workflow of the requisition management system can be
summarized as follows:

1.  Staff enters requisition information (date, staff ID, staff name).

2.  System generates a unique requisition ID.

3.  User inputs item names and prices.

4.  Program calculates total cost.

5.  If total < \$500 -> automatically approved; otherwise, status = pending.

6.  Manager reviews pending requests and updates status accordingly.

7.  The system displays a summary of all requisitions with statistical data.

This logical sequence reflects the structured problem-solving process
aligned with SDLC methodology.

**6. Research Discussion**

Python programming, combined with SDLC methodology, encourages
disciplined software design and continuous improvement. The functions
created in this project reflect modern best practices such as modular
design and code reuse.

According to the Python Software Foundation (2024), Python promotes
clarity and readability, which are essential in educational and
enterprise software projects. Similarly, W3Schools (2024) emphasizes
modular function structures as a best practice in maintainable
programming. Real Python (2023) highlights the role of exception
handling and user input validation in professional applications, which
this project integrated effectively. Microsoft Learn (2024) also
supports class-based development for scalable system design, aligning
with the approach used in the requisition management system.

**7. Conclusion**

This assessment successfully demonstrated how theoretical and practical
programming concepts can be integrated through Python development. The
project not only strengthened understanding of SDLC phases but also
showcased good software design practices such as modularity,
encapsulation, and automation. The requisition management system
prototype, though simple, reflects the foundations of a scalable
business solution. This practical implementation highlights the
importance of structured design, clarity, and maintainability in
developing effective software systems.

**8. References**

Microsoft Learn. (2024). *Introduction to Python development*. Retrieved
from <https://learn.microsoft.com/en-us/training/modules/python-introduction/>

Python Software Foundation. (2024). *Python documentation*. Retrieved
from <https://docs.python.org/3/>

Real Python. (2023). *Python best practices for clean and maintainable
code*. Retrieved from <https://realpython.com/>

TutorialsPoint. (2024). *Python programming tutorial*. Retrieved from
<https://www.tutorialspoint.com/python/>

W3Schools. (2024). *Python functions and object-oriented programming*.
Retrieved from <https://www.w3schools.com/python/>