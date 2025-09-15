count = 0   # Global variable
def increment():
    global count   # Declare 'count' as global so we can modify it
    count += 1
    print(f"Count inside function: {count}")
increment()
increment()
print(f"Count outside function: {count}")
   