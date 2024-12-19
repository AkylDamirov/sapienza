""" func1: 6 points
Write a recursive function func1(list) that, given a list of elements,
returns a dictionary where the keys are the elements of the list and the
values represent the number of occurrences of each element.

NOTE: It is possible to call recursive functions, but they cannot be
internal (recursive functions can only be defined at the top level of the
module and cannot be defined within other functions or classes).
"""


def func1(l):
    if not l:
        return {}
    element = l[0]
    rest_count = func1(l[1:])
    if element in rest_count:
        rest_count[element] += 1

    else:
        rest_count[element] = 1
    return rest_count


""" func2: 9 points

Write a recursive function func2(directory), or a function that uses a 
recursive function internally, that takes a string 'directory' representing 
the path to a directory.

The function must recursively explore the directory tree rooted at 'directory' 
and return a dictionary.
The keys of the dictionary are the paths of subdirectories of 'directory', 
in the form of a string.

The value associated with a directory's key is a set of strings with the 
names of '.txt' files in the directory whose content starts and ends with 
the same character.

If a directory does not contain any .txt files with such a characteristic, 
then that directory does not appear in the dictionary.

If the function is called on 'func2/A', it returns:

{'func2/A/B': {'b.txt'}, 'func2/A/C': {'c.txt'}}

NOTE: Using os.walk is prohibited. You can use:
  os.listdir, os.path.isfile, os.path.exists, etc. To concatenate paths, 
  use the concatenation operation with the '/' character

NOTE: It is strongly recommended to break down the exercise into sub-problems 
by dividing into functions for each sub-problem.

NOTE: It is possible to call recursive functions, but they cannot be 
internal (recursive functions can only be defined at the top level of the 
module and cannot be defined within other functions or classes).
"""

from os.path import isdir, isfile, join
from os import listdir


def check_txt_file(file_path):
    """Checks if the content of the file starts and ends with the same character."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            return len(content) > 0 and content[0] == content[-1]
    except Exception:
        return False


def func2(root):
    """Recursively explores a directory and returns the specified dictionary."""
    dict1 = {}

    for i in listdir(root):
        path = join(root, i)  # Create the full path

        # If it's a .txt file, check its content
        if isfile(path) and i.endswith('.txt') and check_txt_file(path):
            # Add this file to the current directory's set in the dictionary
            if root not in dict1:
                dict1[root] = set()
            dict1[root].add(i)

        # If it's a directory, recursively process it
        elif isdir(path):
            sub_dict = func2(path)
            # Merge results from the subdirectory into the main dictionary
            dict1.update(sub_dict)

    return dict1


""" func3: 5 points 

The Greatest Common Divisor (GCD) of two positive integers is the largest 
integer that divides both numbers without leaving a remainder.

The procedure to calculate the GCD follows these steps:

- Take two numbers, a and b.
- Check if the second number (b) is equal to 0:
    - If yes, the GCD is the first number (a).
    - If no, calculate the remainder of a divided by b (a%b).
- Repeat the procedure with the new values:
    - Replace a with the value of b.
    - Replace b with the value of the calculated remainder (a%b).
    - Continue until b becomes 0. At that point, the GCD is the current 
      value of a.

Write a recursive function or a function using recursive functions that 
calculates the GCD of two numbers. Assume a and b are non-negative integers.

Example: Finding the GCD of 48 and 18:

1. 48 % 18 = 12 (the remainder of 48 divided by 18 is 12).
2. Now calculate the GCD of 18 and 12: 18 % 12 = 6.
3. Now calculate the GCD of 12 and 6: 12 % 6 = 0.
4. The remainder is 0, so the GCD is 6.

NOTE: It is possible to call recursive functions, but they cannot be 
internal (recursive functions can only be defined at the top level of the 
module and cannot be defined within other functions or classes).
"""


def func3(a: int, b: int) -> int:
    if b==0:
        return a
    return func3(b, a%b)