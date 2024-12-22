
user_list = []

while True:

    try:
        number = int(input("Enter a number (or 0 to stop): "))
        
      
        if number == 0:
            break

       
        user_list.append(number)

   
        print(f"Current List: {user_list}")

      
        sorted_list = sorted(user_list)
        print(f"Sorted List: {sorted_list}")
    
    except ValueError:
        print("Please enter a valid integer.")

print("Program finished.")
