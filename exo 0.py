import math

# Ask the user for input
people = int(input("How many people need a ride? "))
taxi_capacity = int(input("How many people can fit in one taxi? "))

# Calculate the number of taxis required
taxis_needed = math.ceil(people / taxi_capacity)

# Output the result
print(f"You will need {taxis_needed} taxis to transport {people} people.")