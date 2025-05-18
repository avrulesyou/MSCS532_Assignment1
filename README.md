# Insertion Sort Implementation

This repository contains a Python implementation of the Insertion Sort Algorithm that sorts arrays in monotonically decreasing order.

## Features
- Sorts arrays in monotonically decreasing order using Insertion Sort Algorithm
- Handles duplicate elements
- Interactive user interface for sorting custom arrays
- Efficient implementation with O(n²) time complexity
- Predefined test cases to demonstrate functionality

## Program Flow
1. Displays welcome message
2. Automatically runs three predefined test cases:
   - Random array
   - Already sorted array
   - Array with duplicate elements
3. Asks user if they want to use the Insertion Sort Algorithm
4. If user chooses to continue:
   - Accepts user input for custom arrays
   - Displays sorted result
   - Repeats until user chooses to exit

## Usage
Run the program using Python:
```bash
python insertion_sort.py
```

## Example Output
```
Welcome to the Insertion Sort Program!
This program sorts arrays in monotonically decreasing order using Insertion Sort Algorithm.

Running predefined test cases...

Original array: [5, 2, 4, 6, 1, 3]
Sorted array (decreasing): [6, 5, 4, 3, 2, 1]

Original array: [6, 5, 4, 3, 2, 1]
Sorted array (decreasing): [6, 5, 4, 3, 2, 1]

Original array: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Sorted array (decreasing): [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

Do you want to use the Insertion Sort Algorithm? (yes/no): yes

Enter numbers separated by spaces: 99 77 55 9999 1 45 2 33 66 77 1 8 9 2 1 4 7571557 2 25 1452 4 654 665412 65 54 785 21

Original array: [99, 77, 55, 9999, 1, 45, 2, 33, 66, 77, 1, 8, 9, 2, 1, 4, 7571557, 2, 25, 1452, 4, 654, 665412, 65, 54, 785, 21]
Sorted array (decreasing): [7571557, 665412, 9999, 1452, 785, 654, 99, 77, 77, 66, 65, 55, 54, 45, 33, 25, 21, 9, 8, 4, 4, 2, 2, 2, 1, 1, 1]

Do you want to use the Insertion Sort Algorithm? (yes/no): no
Thank you for using the program. Goodbye!
```

## Implementation Details
- The algorithm uses a simple insertion sort approach
- Time Complexity: Worst-case and Average-case : O(n²) Best-case: O(n)
- Space Complexity: O(1)

## Author
Abhishek Vishwakarma

