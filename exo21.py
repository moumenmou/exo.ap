def length(lst):
    """
    Returns the number of elements in the list.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    int: The number of elements in the list.
    """
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of the list.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    float: The mean of the list.
    
    Raises:
    ValueError: If the list is empty.
    """
    if len(lst) == 0:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    int or float: The range of the list (max - min).
    
    Raises:
    ValueError: If the list is empty.
    """
    if len(lst) == 0:
        raise ValueError("Cannot calculate range of an empty list.")
    return max(lst) - min(lst)

sample_list = [1, 2, 3, 4, 5]

print(f"Length of the list: {length(sample_list)}")  # Output: 5

try:
    print(f"Mean of the list: {mean(sample_list)}")  # Output: 3.0
except ValueError as e:
    print(e)

try:
    print(f"Range of the list: {range_of_list(sample_list)}")  # Output: 4
except ValueError as e:
    print(e)

empty_list = []
try:
    print(f"Mean of the empty list: {mean(empty_list)}")
except ValueError as e:
    print(e)  

try:
    print(f"Range of the empty list: {range_of_list(empty_list)}")
except ValueError as e:
    print(e)  
