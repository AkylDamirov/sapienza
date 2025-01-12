#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

################################################################################
################################################################################
################################################################################

""" Operations to perform BEFORE EVERYTHING:
 1) Save the file as program.py
 2) Assign the variables below with your
    FIRST NAME, LAST NAME, STUDENT ID NUMBER

To pass the exam, it is necessary to:
    - obtain a score greater than or equal to 18

The final grade is the sum of the marks from the problems solved.

IMPORTANT: set DEBUG = True in `grade.py` to increase the debug level
and identify where an exercise generates an error.
Remember that to test and evaluate recursion, DEBUG must be set to False.

To quickly comment/uncomment code, use Control + 1!
"""
name = "test"
surname = "test"
student_id = "1231231"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 marks
Define the function func1(L, k) that gets as input a list of integers
L and an integer k. The function removes from L all values that can be
evenly divided by k (i.e., those for which the remainder of the division
by k is zero).
The function returns the number of elements removed from L.
Example: If L is [1, 3, 4, 6, 5, 2, 4, 7, 8, 4, 9] and k=2, L
should be modified IN-PLACE as [1, 3, 5, 7, 9], and the number of 
removed elements is 6, as 4, 6, 2, 4, 8, 4 can be evenly divided
by 2.
'''


def func1(L, k):
    count = 0
    to_delete = []
    for i in L:
        if i % k == 0:
            to_delete.append(i)
            count += 1
    for i in to_delete:
        if i in L:
            L.remove(i)
    return count


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 3 marks
Define the function func2(dicts) that takes a list of dictionaries as input.
Each dictionary has an integer as its key and a single string as its value.
It is necessary to compute a unique dictionary that contains all the keys
from all dictionaries with their associated values. In the case of a key
repetition, the value in the resulting dictionary is a list containing
all the strings for that key; otherwise, it is a list with just one string.
Each list in the unique dictionary must be sorted first by the length of
the strings in descending order and, in the case of ties, alphabetically.
For example, if dicts = [{1:'iac', 2:'andrea',3:'mau', 5:'angelo'},
            {2:'sterbini', 3:'mancini',1:'masi', 5:'spognardi'}]

func2(dicts) should return

{1: ['masi', 'iac'], 2: ['sterbini', 'andrea'], 3: ['mancini', 'mau'],
 5: ['spognardi', 'angelo']}
'''


def sort1(key):
    return (-len(key), key)


def func2(dicts):
    new_dict = {}
    for j in range(len(dicts)):
        for i, v in dicts[j].items():
            if i not in new_dict:
                new_dict[i] = [v]
            else:
                new_dict[i].append(v)
                new_dict[i] = sorted(new_dict[i], key=sort1)

    return new_dict


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 marks
Define the function func3(L) that takes as input a list of integer lists L
like L = [[1, 1, 0], [1, 0, 1, 1], [1, 2], [1, 1, 0, 0]].
The function returns the "maximum" inner list in L.
To determine the "maximum" for each inner list, calculate the product 
of the length of the list and the sum of its elements.
In the example above, the "maximum" list is [1, 0, 1, 1]
because its value is 4*3, i.e., 4 elements multiplied by the sum of the 
elements (3).

The other values were:
L =    [[1, 1, 0], [1, 0, 1, 1], [1, 2], [1, 1, 0, 0]]
values   6              12        6          8

In case of a tie, simply follow the order of the original L list.
'''


def func3(L):
    max_sum = 0
    max_list = []
    for i in L:
        if sum(i) * len(i) > max_sum:
            max_list = i
            max_sum = sum(i) * len(i)
    return max_list


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Define the function func4(input_filename, output_filename) that
takes two file names as parameters. The function reads the text file 
input_filename and returns the number of lines in the file.
For each line of the file, calculate the sum of the numerical 
representation of EVERY character in that line.

In the file func4/func4_test1.txt, the first line
cat bat    rat
has a sum of 1120 by summing ALL the characters in the line.

So the file will have "sums" for each line:
sums = [1120, 934, 836]
      line 0   1     2

and the function returns 3 (3 lines).

The function also writes a text file at the output_filename location
that contains the indices ordering "sums" in increasing order,
one index per line.

In the file func4/func4_out1.txt, it should write:
2
1
0

because index 2 is written first since its associated sum 836
is the smallest, and so on, meaning:

|  index |  sums |
|      2 |   836 |
|      1 |   934 |
|      0 |  1120 |
"""


def func4(input_filename, output_filename):
    file = open(input_filename)
    list1 = []
    lines = 0
    for i in file.readlines():
        sum1 = 0
        for j in i:
            sum1 += ord(j)
        list1.append(sum1)
        lines += 1
    file.close()
    file2 = open(output_filename, 'w')
    sorted_indices = sorted(range(len(list1)), key=lambda i: list1[i])
    for i in sorted_indices:
        file2.write(str(i) + '\n')
    file2.close()
    return lines


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5:  7 marks
Define the function func5(pngfile) that takes a string pngfile
as input, representing the path to a PNG image.
The pngfile file contains an image with a black background, featuring 
crosses of any color. Each cross is 3x3 pixels in size.
Example:
..x.....
.xxxo...
..xooo..
....o...
........

In the example, there is a cross of color 'x' and another of color 'o'.

Assume that two crosses of the same color are separated by at least one
pixel of another color, meaning they do not touch horizontally, vertically,
or diagonally. Assume that the image pixels belong to a cross or the background.
The function must count the number of crosses present for each color 
and return a dictionary where the keys are the colors of the crosses 
in the image, and the values are the number of crosses of that color.

Example: see func5/in_01.png; if the input is that image, the function 
returns {(0, 200, 0): 2, (200, 0, 0): 1} because there are 2 green crosses 
(0, 200, 0) and 1 red cross (200, 0, 0).
"""

import images
from images import load


def func5(png_input):
    image = load(png_input)
    dict1 = {}
    for line in range(len(image)):
        for i in range(len(image[line])):
            try:
                if image[line][i] == image[line - 1][i] and \
                        image[line][i] == image[line + 1][i] and \
                        image[line][i] == image[line][i - 1] and \
                        image[line][i] == image[line][i + 1] and image[line][i] != (0, 0, 0):
                    if image[line][i] in dict1:
                        dict1[image[line][i]] += 1
                    else:
                        dict1[image[line][i]] = 1
            except:
                continue

    return dict1


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks (3+3)

Define the function ex1(node, j, k), recursive or using another
recursive function, which takes as input the root node 'node' of a binary 
tree made of BinaryTree nodes, as defined in the tree.py module. The 
function also takes:
- j: an integer indicating the minimum level of nodes to consider
- k: an integer indicating the maximum level of nodes to consider
Assume j <= k. The function ex1 returns a tuple of integers:
- the height of the tree (ignoring j and k) (+3 marks)
- the TOTAL NUMBER OF NODES between j and k INCLUSIVE (+3 marks)

Example: if j = 1 and k = 2

        root     
    ______25______            level = 0
   |             | 
   8__        ___2___         level = 1
      |      |       | 
      3      9       1        level = 2

   expected = (3, 5) # height, total nodes between j and k inclusive

since the tree has height 3 (one maximum path is 25->2->1)
and the total number of nodes between those levels is 5, 
as 3, 8, 2, 9, 1 are the 5 nodes between those levels.
Assume the root is at level 0.
*********************************************************************
TIP: You can create 2 independent and separate recursive functions:
one to calculate the depth and another to sum the nodes between j and k.
********************************************************************
NB: If you write an additional function, DO NOT define the additional 
recursive function as an internal function; instead, place it at the 
same level as ex, otherwise, you won't pass the recursive test!
"""

from tree import BinaryTree


def height(node):
    if node is None:
        return -1
    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


def count_nodes(node, curr_level, j, k):
    if node is None:
        return 0
    if curr_level < j:
        return count_nodes(node.left, curr_level + 1, j, k) + \
            count_nodes(node.right, curr_level + 1, j, k)
    elif curr_level > k:
        return 0

    return 1 + count_nodes(node.left, curr_level + 1, j, k) + \
        count_nodes(node.right, curr_level + 1, j, k)


def ex1(node, j, k):
    height1 = height(node) + 1
    size1 = count_nodes(node, 0, j, k)
    return (height1, size1)


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex 2: 6 points

Define the function ex2(path, list_extensions) which receives as arguments:
- path: a string representing the path of a directory
- list_extensions: a list of strings representing file extensions.
The function must recursively explore the directory 'path'
and all its subdirectories and return a dictionary that has as keys the extensions
and as values the set of directories containing that type of file.
If an extension never occurs, it should not be included in the dictionary.

WARNING: it is forbidden to use the os.walk function.
NOTE: you can use the functions os.listdir, os.path.isdir, os.path.isfile ...
NOTE: use the '/' character to separate paths, which works on both Windows and Linux

Example:
    directory = 'ex2/A'
    extensions = ['txt', 'pdf', 'png', 'gif', 'py']
    expected = {'txt': {'ex2/A/C', 'ex2/A', 'ex2/A/B'},
                'pdf': {'ex2/A/C', 'ex2/A'},
                'png': {'ex2/A/C'},
                'gif': {'ex2/A/C'}}
"""
import os
from os.path import isdir, isfile, join
from os import listdir


def ex2(path, list_extensions):
    dict1 = {}
    for i in list_extensions:
        dict1[i] = set()
    for i in listdir(path):
        current_path = join(path, i)
        if not isdir(current_path):
            for j in list_extensions:
                if i.endswith(j):
                    # dict1.update({j:{path}})
                    dict1[j].add(path)
        else:
            sub_dict = ex2(current_path, list_extensions)
            for i in list_extensions:
                if i in sub_dict:
                    dict1[i].update(sub_dict[i])

    for i, v in dict1.items():
        if dict1[i]:
            dict1[i] = set(v)
        else:
            dict1[i] = {}

    return {ext: dict1[ext] for ext in dict1 if dict1[ext]}


