def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using insertion sort.
    
    Args:
        arr (list): The input array to be sorted
        
    Returns:
        list: The sorted array in decreasing order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def get_array_from_user():
    try:
        user_input = input("\nEnter numbers separated by spaces: ")
        return [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return get_array_from_user()

def main():
    print("Welcome to the Insertion Sort Program!")
    print("This program sorts arrays in monotonically decreasing order using Insertion Sort Algorithm.")
    
    print("\nRunning predefined test cases...")
    test_cases = [
        [5, 2, 4, 6, 1, 3],
        [6, 5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]
    
    for arr in test_cases:
        print(f"\nOriginal array: {arr}")
        print(f"Sorted array (decreasing): {insertion_sort_decreasing(arr.copy())}")
    
    while True:
        choice = input("\nDo you want to use the Insertion Sort Algorithm? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the program. Goodbye!")
            break
            
        user_array = get_array_from_user()
        print(f"\nOriginal array: {user_array}")
        print(f"Sorted array (decreasing): {insertion_sort_decreasing(user_array)}")

main()
