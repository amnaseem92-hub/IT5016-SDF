print("Kia Ora, this is a parking meter")

# set parking time
#park_time = 4

park_time = int(input("Enter your parking time: "))

print(f"Park time is {park_time} hours.")

# set rate and cost
first_3_hours_rate = 4
extra_hours_rate = 2
cost = 0

if park_time > 3:
    # first 3 hours at $4/hr
    cost = 3 * first_3_hours_rate
    
    # remaining hours at $2/hr
    extra_hours = park_time - 3
    # cost += extra_hours * extra_hours_rate
    cost = cost + (extra_hours * extra_hours_rate)
else:
    # if 3 hours or less
    cost = park_time * first_3_hours_rate

print(f"The cost of the parking is ${cost}")