\# Task c) Clean Code Refactoring



For task c), I created a feature branch named `clean-code-mergesort`.

On this branch, I refactored `mergesort.py` according to the Clean Code rules from the lecture.



The functionality of the program is still the same: it demonstrates merge sort on an example list and visualizes the values before and after sorting.



\## Clean Code improvements



1\. Renamed `mergeSort` to `merge\_sort` to follow Python snake\_case naming.

2\. Removed the unclear helper function `ASSIGNMENT`.

3\. Replaced short variable names such as `l`, `r` and `i` with meaningful names.

4\. Simplified the base case of the recursion.

5\. Added type hints to all functions.

6\. Added docstrings to explain the purpose, arguments and return values.

7\. Moved the import statement to the top of the file.

8\. Moved the executable code into a `main()` function.

9\. Added the `if \_\_name\_\_ == "\_\_main\_\_"` guard.

10\. Extracted the repeated plotting code into a reusable function.

11\. Added plot titles, axis labels and a grid.



