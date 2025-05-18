def insertion_sort_decreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


def main():
    test_cases = [
        [5, 2, 4, 6, 1, 3]
    ]
    
    for arr in test_cases:
        print(f"Sorted array (decreasing): {insertion_sort_decreasing(arr.copy())}")
    

main() 