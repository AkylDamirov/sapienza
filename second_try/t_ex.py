# Define the function func1(L, D) that takes a list L and a dictionary D as input and returns a new list.
#
# The dictionary is composed of integers as keys and lists as values.
#
# The returned list must contain the keys of the dictionary D with the following selection criteria:
#
# Assuming that x is an element of the list L, insert the maximum key that contains x in the corresponding list.
# If x is not contained in any list of the dictionary, then do not insert any key.
# The order of insertion of the keys follows the order of L.


def func1(L,D):
    result = []

    for i in L:
        max_key = None
        for k,v in D.items():
            if i in v:
                if max_key is None or k > max_key:
                    max_key = k

        if max_key is not None:
            result.append(max_key)
    return result
L = ['a', 'ciao', 4, 0]
D = {3: ['a', 0, 2, 3], 1: [9, 'ciao', 'hello', 3.2, 'a'], 10: ['a', 'ciao', -2]}
# print(func1(L, D))  # Output: [10, 10, 3]


# Define the function func2(L) that takes a list of strings as input and returns a string.
# The returned string is the string present in L that has the highest ratio between the sum of
# the Unicode values of the characters that compose it and the number of characters that compose it.
# In case of strings with the same ratio, the function returns the string with the greater length.
# You can use the ord function to know the Unicode value of any character.

def func2(L):
    max_string = ''
    max_ratio = 0

    for i in L:
        total_unicode = sum(ord(j) for j in i)
        ratio = total_unicode / len(i)

        if ratio > max_ratio or (ratio == max_ratio and len(i)>len(max_string)):
            max_string = i
            max_ratio = ratio
    return max_string

# print(func2(['zzz', 'abracadabra', 'apple', 'zzzzz', 'qwertyuiop']))

''' func3: 2 points
Define the function func3(L) that takes a list L composed of sets as input.
The function must return a new list containing all the sets obtained by
considering the union and intersection of pairs of sets in L.
The order of the returned list is obtained by considering the indices of
the pairs of sets in L used to generate the list.

Example: if L = [{1,2}, {2,3}, {1,3,4}] the returned list will be
  [{1,2,3}, {2}, {1,2,3,4}, {1}, {1,2,3,4}, {3}], because
    {1,2,3} and {2} are obtained from L[0] and L[1]
    {1,2,3,4} and {1} are obtained from L[0] and L[2]
    {1,2,3,4} and {3} are obtained from L[1] and L[2].
'''


def func3(L):
    new_list = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            new_list.append(L[i].union(L[j]))
            new_list.append(L[i].intersection(L[j]))
    return new_list

# print(func3([{1,2}, {2,3}, {1,3,4}]))


""" func4: 6 points
Define the function func4(input_filename, output_filename) that
takes two file names as parameters. The function reads the text file
input_filename.
Each line of the input_filename file contains a series of words separated
by spaces or tabs. For each of these lines, the function must write in the
output_filename file a new line with all the words of the corresponding line,
separated by a comma and a space and ordered with
the following criteria:
    - Increasing number of characters
    - in case of a tie, increasing number of uppercase letters
    - in case of a tie, decreasing number of vowels (no distinction between uppercase and lowercase)
    - in case of a tie, alphabetical order

The lines are written in the output_filename file ordered with the following criteria:
    - Increasing number of characters
    - in case of a tie, increasing total number of uppercase letters
    - in case of a tie, decreasing total number of vowels (no distinction between uppercase and lowercase)
    - in case of a tie, alphabetical order

The function returns the number of words written in the output_filename file.
"""

def sort1(key):
    vowels = set('euioaEUIOA')
    return (len(key), sum(1 for i in key if i.isupper()), -sum(1 for i in key if i in vowels), key)

def func4(input_filename: str, output_filename: str) -> int:
    file = open(input_filename, 'r')
    file2 = open(output_filename, 'w')
    list1 = []
    for i in file.readlines():
        sorted1 = sorted(i.split(), key=sort1)
        list1.append(sorted1)
    list1 = sorted(list1, key=sort1)
    count = 0
    for i in list1:
        for j in i:
            if j==i[-1]:
                file2.write(j)
            else:
                file2.write(f'{j}, ')
            count +=1
        file2.write('\n')
    file.close()
    file2.close()
    return count

# print(func4('test_file.txt', 'output.txt'))


""" func5: 7 points
Define the function func5(png_input: str) -> tuple[int, int] that takes as
input a string png_input that indicates the path to a png image.
The image has a black background and white rectangles and squares are drawn
on it, which do not touch or intersect and whose sides are horizontal or
vertical segments. See for example the image in func5/in_01.png.
The function must find the number of squares and the number of
rectangles present in the image.

The function returns the tuple (q, r) where q is the number of squares present
in the image and r is the number of rectangles present in the image. For
example, for the image func5/in_01.png, the function must return the pair (3, 2).

To load and save PNG files, you can use the load and save functions from
the images library.
"""

import images

def find_shape(image, visited, row, col, white):
    h,w = len(image), len(image[0])
    max_row, max_col = row, col
    while max_col < w and image[row][max_col] == white:
        max_col += 1
    while max_row < h and image[max_row][col] == white:
        max_row += 1

    for r in range(row, max_row):
        for c in range(col, max_col):
            visited[r][c] = True
    return max_col - col, max_row - row

def func5(png_input: str) -> tuple[int, int]:
    image = images.load(png_input)
    h, w = len(image), len(image[0])
    squares, rectangles = 0,0
    white = (255, 255, 255)
    visited = [[False] * w for _ in range(h)]

    for row in range(h):
        for col in range(w):
            if image[row][col]==white and not visited[row][col]:
                width, height = find_shape(image, visited, row, col, white)
                squares += width == height
                rectangles += width != height
    return squares, rectangles

"""
Ex1: 6 points
Define the function ex1(node: BinaryTree) -> str that receives as input
the root of a binary tree, as defined in the `BinaryTree` class of the
`tree.py` module. The input tree has strings as values. The function must
return the string resulting from the concatenation of all the values
associated with the nodes of the tree with the following rules:
  - concatenate only the values at even levels (the root is at level 0)
  - concatenate first the left subtree, then the current value, and
    finally the right subtree

Example:

        ______A______       level 0          ______A______
       |             |                      |             |
       B__        ___C___   level 1      __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F  level 2    _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                            level 3   H   I      J  K   L   M   N

  If the tree is the one on the left, the function must return the string "DAEF"

 If the tree is the one on the right, the function must return the string "DEAFG"
********************************************************************
NB: if you write an additional function, DO NOT define the recursive additional
function as an internal function but put it at the same level as ex1, as an
external function, otherwise you will not pass the recursive test!
"""
def additional(node, level=0):
    if node is None:
        return ''
    left_part = additional(node.left, level+1)
    right_part = additional(node.right, level+1)
    if level % 2 == 0:
        return left_part + node.value + right_part
    else:
        return left_part + right_part


def ex1(node):
    return additional(node)

"""
Ex2: 6 points

Define the function ex2(L: int, M: int) that is recursive or uses recursive
functions or methods, which takes two integers L and M as input. The function
must return a list of strings. The list contains all combinations of strings
obtained by concatenating either "_" or "|" with the following rules:
- The strings must all have exactly L characters.
- M indicates that the generated string must contain exactly M "|" characters.
  M is always less than or equal to L.

For example, if L = 5, M = 3:

"_____" is NOT valid because it does not contain any "|" characters and should have contained M=3.
"|||" is NOT valid because it contains only 3 characters instead of L=5.
"|__|_" is NOT valid because it contains only 2 "|" characters.
"|_|_|" is valid.
"||__|" is valid because it is 5 characters long and contains 3 "|".

The list must be sorted in alphabetical order.

If L = 5, M = 3 the sorted list is:

['__|||', '_|_||', '_||_|', '_|||_', '|__||', '|_|_|', '|_||_', '||__|', '||_|_', '|||__']

********************************************************************
NB: if you write an additional function, DO NOT define the recursive additional
function as an internal function but put it at the same level as ex2, as an
external function, otherwise you will not pass the recursive test!
********************************************************************
"""

def generate_combinations(L, M, current='', count=0):
    if len(current)==L:
        return [current] if count == M else []
    with_bar = generate_combinations(L, M, current+'|', count+1) if count < M else []
    with_underscore = generate_combinations(L, M, current+'_', count)
    return with_bar + with_underscore

def ex2(L: int, M: int):
    return sorted(generate_combinations(L, M))


