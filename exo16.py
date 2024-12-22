
numbers = [1, 2, 3, 4, 5]

while True:
 
    index = int(input("Enter an index to update (or -1 to stop): "))
    
    
    if index == -1:
        break
    
   
    if index < 0 or index >= len(numbers):
        print("Invalid index. Please try again.")
        continue
    
 
    new_value = int(input(f"Enter a new value for position {index}: "))
    
   
    numbers[index] = new_value
    
    
    print("Updated list:", numbers)

print("Final list:", numbers)
