
numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")


def handle_choice(choice):
    if choice == 1:
      
        try:
            element = int(input("Enter the element to append: "))
            numbers.append(element)
            print(f"Updated list: {numbers}")
        except ValueError:
            print("Invalid input! Please enter an integer.")
    
    elif choice == 2:
  
        try:
            element = int(input("Enter the element to insert: "))
            position = int(input(f"Enter the position (0 to {len(numbers)}): "))
            if position < 0 or position > len(numbers):
                print(f"Invalid position! Must be between 0 and {len(numbers)}.")
            else:
                numbers.insert(position, element)
                print(f"Updated list: {numbers}")
        except ValueError:
            print("Invalid input! Please enter valid integers for element and position.")
    
    elif choice == 3:
      
        try:
            position = int(input(f"Enter the index to pop (0 to {len(numbers)-1}): "))
            if position < 0 or position >= len(numbers):
                print(f"Invalid index! Must be between 0 and {len(numbers)-1}.")
            else:
                popped_element = numbers.pop(position)
                print(f"Popped element: {popped_element}")
                print(f"Updated list: {numbers}")
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except IndexError:
            print("Pop failed: index out of range.")
    
    elif choice == 4:
       
        try:
            element = int(input("Enter the element to remove: "))
            numbers.remove(element)
            print(f"Updated list: {numbers}")
        except ValueError:
            print(f"Element {element} not found in the list.")

    elif choice == 5:
        print("Exiting program.")
        return False
    
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
    
    return True


while True:
    display_menu()
    
    try:
        user_choice = int(input("Enter your choice (1-5): "))
        if not handle_choice(user_choice):
            break
    except ValueError:
        print("Invalid input! Please enter a valid choice (1-5).")

