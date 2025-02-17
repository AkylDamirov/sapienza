#-------------------------------------WORKING WITH SORTING--------------------------------------------------

'''
You have a list of student names. Sort them based on the following criteria:

1. Shorter names first (increasing order of length).
2. If two names have the same length, sort by the number of vowels (more vowels first).
3. If still tied, sort by the number of uppercase letters (more uppercase first).
4. If still tied, sort alphabetically.
input:
students = ["Alice", "BOB", "Eve", "Oscar", "Charlie", "UMAR", "Zara"]
Expected Output:
['Eve', 'BOB', 'UMAR', 'Alice', 'Oscar', 'Zara', 'Charlie']
'''

students = ["Alice", "BOB", "Eve", "Oscar", "Charlie", "UMAR", "Zara"]
def sort1(key):
    vowels = set('euioaEUIOA')
    return (len(key), -sum(1 for i in key if i in vowels), -sum(1 for i in key if i.isupper()), key)

sorted_words = sorted(students, key=sort1)
# print(sorted_words)

'''
Exercise 2: Sorting Sentences
You have a list of sentences. Sort them by:
1. Number of words (fewer words first).
2. If tied, sort by the number of uppercase letters (more uppercase first).
3. If still tied, sort alphabetically.
input
sentences = ["HELLO world", "Python is fun", "AI", "MACHINE LEARNING is great", "I love coding"]
output:
['AI', 'HELLO world', 'I love coding', 'Python is fun', 'MACHINE LEARNING is great']
'''

sentences = ["HELLO world", "Python is fun", "AI", "MACHINE LEARNING is great", "I love coding"]
def sort2(key):
    return (len(key), sum(1 for i in key if i.isupper()), key)

sorted_words = sorted(sentences, key=sort2)
# print(sorted_words)


'''
Exercise 3: Sorting City Names
You have a list of city names. Sort them based on:

1. Cities with more unique letters first.
2. If tied, sort by fewer vowels.
3. If still tied, sort alphabetically.
input:
cities = ["Oslo", "Berlin", "Tokyo", "Amsterdam", "Kyoto"]
output:
['Amsterdam', 'Berlin', 'Tokyo', 'Kyoto', 'Oslo']
'''

cities = ["Oslo", "Berlin", "Tokyo", "Amsterdam", "Kyoto"]
def sort3(key):
    vowels = set('euioaEUIOA')
    return (-len(set(key)), -sum(1 for i in key if i in vowels), key)

sorted_cities = sorted(cities, key=sort3)
# print(sorted_cities)

'''
Exercise 4: Sorting File Names
You have a list of filenames. Sort them based on:

1. Shorter filenames first.
2. If two files have the same length, sort by the number of digits in the name (more digits first).
3. If still tied, sort alphabetically.
input:
files = ["file10.txt", "doc3.pdf", "notes.txt", "data99.csv", "a1.doc"]
output:
['a1.doc', 'doc3.pdf', 'notes.txt', 'file10.txt', 'data99.csv']
'''

files = ["file10.txt", "doc3.pdf", "notes.txt", "data99.csv", "a1.doc"]
def sort4(key):
    return (len(key), sum(1 for i in key if i.isdigit()), key)

sorted_files = sorted(files, key=sort4)
# print(sorted_files)

'''
Exercise 5: Sorting Products by Price
You have a list of products represented as tuples (name, price, rating). Sort them by:
1. Cheaper price first.
2. If prices are the same, sort by higher rating first.
3. If still tied, sort alphabetically.
input:
products = [("Laptop", 1000, 4.5), ("Smartphone", 700, 4.7), ("Tablet", 700, 4.6), ("Monitor", 200, 4.3)]
output:
[('Monitor', 200, 4.3), ('Tablet', 700, 4.6), ('Smartphone', 700, 4.7), ('Laptop', 1000, 4.5)]
'''

products = [("Laptop", 1000, 4.5), ("Smartphone", 700, 4.7), ("Tablet", 700, 4.6), ("Monitor", 200, 4.3)]

def sort5(key):
    return (key[1], -key[2], key)

sorted_products = sorted(products, key=sort5)
# print(sorted_products)

'''
Bonus Challenge: Sorting Book Titles
You have a list of book titles. Sort them based on:
1. Number of words (more words first).
2. If tied, sort by total number of characters (longer first).
3. If still tied, sort alphabetically.
Example Input:
books = ["The Great Gatsby", "Moby Dick", "1984", "War and Peace", "A Brief History of Time"]
Expected Output:
['A Brief History of Time', 'War and Peace', 'The Great Gatsby', 'Moby Dick', '1984']
'''

books = ["The Great Gatsby", "Moby Dick", "1984", "War and Peace", "A Brief History of Time"]
def sort6(key):
    return (-len(key), sum(1 for i in key if i.isalpha()),key)

sorted_books = sorted(books, key=sort6)
# print(sorted_books)

#-------------------------------------WORKING WITH FILES--------------------------------------------------
'''
6. Finding and Replacing Words
Write a function replace_word(file, old_word, new_word) that
replaces all occurrences of old_word with new_word in a given file.
Test it by replacing "Python" with "Machine Learning" in sample.txt.
'''


def replace_word(file, old_word, new_word):
    file = open(file, 'r')
    file2 = open('test_file.txt', 'w')
    for j in file.readlines():
        for i in j.split():
            if i == old_word:
                file2.write(f'{new_word} ')
            else:
                file2.write(f'{i} ')
        file2.write('\n')
    file.close()
    file2.close()
    return 'done'

# print(replace_word('gbb', 'Python', 'Machine Learning'))

'''
2. Processing CSV Files
Create a CSV file data.csv with the following content:
Name, Age, Country
Alice, 24, USA
Bob, 30, Canada
Charlie, 28, UK
Write a Python script to read the CSV file and print each row as a dictionary:
[
    {'Name': 'Alice', 'Age': '24', 'Country': 'USA'},
    {'Name': 'Bob', 'Age': '30', 'Country': 'Canada'},
    {'Name': 'Charlie', 'Age': '28', 'Country': 'UK'}
]
'''
import csv
def csv_func(file):
    list1 = []
    with open(file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list1.append(row)
    return list1
#
# print(csv_func('data2.csv'))



# file = open('test_file.txt')
# for i in file:
#     print(i, end='')

#-------------------------------------WORKING WITH IMAGES--------------------------------------------------
'''
Flip an image
Flip the image horizontally, vertically, and both.
'''
from images import load, save, visd

image = 'Mario.png'

def flip_vertically(image):
    image = load(image)
    save(image[::-1], 'new_image.png')

# print(flip_vertically(image))

def flip_horizontaly(image):
    image = load(image)
    flipped = [row[::-1] for row in image]
    save(flipped, 'new_image.png')

# print(flip_horizontaly(image))
'''
6. Write a function that takes the string representing a png file’s name and returns an integer as input.
The image is a black image with some white segments that join vertically and horizontally but never intersect.
The function has to return the number of pixels of the longest white segment in the image.
Examples are the images in image07.png image08.png for which the function should return the values 115 and 148, respectively.
'''
from images import load
def follow_segment(image, r, c):
    to_visit = [(r,c)]
    count = 0
    while len(to_visit) > 0:
        r, c = to_visit.pop()
        image[r][c] = (0,0,0)
        count += 1
        if r>0 and image[r-1][c] == (255, 255, 255):
            to_visit.append((r-1, c))
        if r<len(image)-1 and image[r+1][c] == (255, 255, 255):
            to_visit.append((r+1, c))
        if c>0 and image[r][c-1] == (255, 255, 255):
            to_visit.append((r, c-1))
        if c<len(image[0])-1 and image[r][c+1] == (255, 255, 255):
            to_visit.append((r, c+1))
    return count


def longest_white_segment(image):
    image = load(image)
    max_len = 0
    length = 0
    for r, row in enumerate(image):
        for c, col in enumerate(row):
            if col == (255, 255, 255):
                length = follow_segment(image, r, c)
                if length > max_len:
                    max_len = length
    return max_len

# print(longest_white_segment('sample_images/image07.png'))
#-------------------------------------WORKING WITH RECURSION--------------------------------------------------
'''
Factorial Calculation
Write a recursive function to compute the factorial of a number n.
Example: factorial(5) → 120
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

'''
Sum of Digits

Write a function that calculates the sum of the digits of a given number.
Example: sum_digits(123) → 6
'''
#solution:
# We take the last digit of 𝑛
# n using n % 10 and recursively call the function on the remaining digits using n // 10. The base case is when n is 0.
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n//10)

# print(sum_digits(123))

'''
Power Function
Implement a recursive function to compute 𝑎^𝑏 (exponentiation).
Example: power(2, 3) → 8
'''
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n-1)

# print(power(2,3))

'''
Fibonacci Sequence
Implement a recursive function to compute the n-th Fibonacci number.
Example: fibonacci(6) → 8
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))

'''
Reverse a String
Write a recursive function to reverse a string.
Example: reverse("hello") → "olleh"
'''
def reverse(n):
    if len(n)<=1:
        return n
    return n[-1] + reverse(n[:-1])

# print(reverse("hello"))


'''
Check for Palindrome
Write a recursive function to check if a given string is a palindrome.
Example: is_palindrome("racecar") → True
'''
def is_palindrome(n):
    if len(n)<=1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome(n[1:-1])

# print(is_palindrome('racecar'))

'''
Greatest Common Divisor (GCD)
Implement a recursive function to find the GCD of two numbers using the Euclidean algorithm.
Example: gcd(48, 18) → 6
'''
def gcd(m, n):
    if n==0:
        return m
    return gcd(n, m%n)

# print(gcd(48, 18))
'''
Permutations of a String
Write a recursive function to generate all permutations of a given string.
Example: permutations("abc") → ["abc", "acb", "bac", "bca", "cab", "cba"]
'''
def generate_permutations(n):
    if len(n)==0:
        return ['']
    permutations = []
    for i in range(len(n)):
        remaining = n[:i] + n[i+1:]
        for p in generate_permutations(remaining):
            permutations.append(n[i] + p)
    return permutations

# print(generate_permutations('abc'))

'''
write a function that counts the number of odd and even values in a list of positive integers provided as input.
the function is recursive or makes use a recursive function and returns a tuple (odd, even).

for example, count_odd_even([7, 3, 4, 9, 2, 1, 6])
returns (4, 3)
'''

def count_odd_even(values_list):
    if not values_list:
        return (0,0)
    first, *rest = values_list
    if first % 2 == 0:
        odd_count, even_count = count_odd_even(rest)
        return (odd_count, even_count+1)
    else:
        odd_count, even_count = count_odd_even(rest)
        return (odd_count+1, even_count)


# print(count_odd_even([7, 3, 4, 9, 2, 1, 6]))

"""

Write a recursive function that gets a string as input
representing the name of a directory and returns the
number of files ending wiht ".py" in the directory and anyt
of its subdirectory.

"""
import os
def count_py(directory):
    counter = 0
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            counter += count_py(path)
        elif os.path.isfile(path) and file.endswith('.py'):
            counter += 1
    return counter

# print(count_py('.'))

#-------------------------------------WORKING WITH BINARY TREE--------------------------------------------------

class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def count_nodes(root):
    if root.left is None and root.right is None:
        return 1
    counter = 1
    if root.left:
        counter += count_nodes(root.left)
    if root.right:
        counter += count_nodes(root.right)
    return counter

def count_leaves(root):
    if root.left is None and root.right is None:
        return 1
    counter = 0
    if root.left:
        counter += count_leaves(root.left)
    if root.right:
        counter += count_leaves(root.right)
    return counter

def sum_of_tree(root):
    if root.left is None and root.right is None:
        return root.value
    partial_sum = root.value
    if root.left:
        partial_sum += sum_of_tree(root.left)
    if root.right:
        partial_sum += sum_of_tree(root.right)
    return partial_sum

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.right), height(root.left))

# root = BinaryNode(5)
# node = BinaryNode(3)
# root.left = node
# node = BinaryNode(7)
# root.right = node
# node  = BinaryNode(1)
# root.left.left = node
# node = BinaryNode(4)
# root.right.left = node
# node = BinaryNode(9)
# root.left.right = node
# root.right.left.right = BinaryNode(8)

# print(count_nodes(root))
# print(count_leaves(root))
# print(sum_of_tree(root))
# print(height(root))


'''
write 3 recursvive functions to pre-, in-, and post-visit a binary tree, providing the result as a list.
use the provided BinTree class that implements binary trees.
given the following tree:
          a
        /   \
       b     c
      / \   /
     d   e f
        /
       g

pre-visit = ["a", "b", "d", "e", "g", "c", "f"]
in-visit = ["d", "b", "g", "e", "a", "f", "c"]
post-visit = ["d", "g", "e", "b", "f", "c", "a"]
'''
from bintree import BinTree
# root = BinTree('a')
# root.left = BinTree('b')
# root.right = BinTree('c')
# root.left.left = BinTree('d')
# root.right.left = BinTree('f')
# root.left.right = BinTree('e')
# root.left.right.left = BinTree('g')

# pre-visit = ["a", "b", "d", "e", "g", "c", "f"]
def pre_visit(T):
    res = []
    def pre_order(root):
        if not root:
            return
        res.append(root.value)
        pre_order(root.left)
        pre_order(root.right)
    pre_order(T)
    return res


# in-visit = ["d", "b", "g", "e", "a", "f", "c"]
def in_visit(T):
    res = []
    def in_order(root):
        if not root:
            return
        in_order(root.left)
        res.append(root.value)
        in_order(root.right)
    in_order(T)
    return res



# post-visit = ["d", "g", "e", "b", "f", "c", "a"]
def post_visit(T):
    res = []
    def post_order(root):
        if root is None:
            return
        post_order(root.left)
        post_order(root.right)
        res.append(root.value)
    post_order(T)
    return res


# print(pre_visit(root))
# print(in_visit(root))
# print(post_visit(root))

# -------------------


from bintree import BinTree as bt
# root = bt.fromList([7, [4, None, [6, [3, None, [2, None, None]], None]],\
#                     [1, [2, [9, None, None], [3, None, [8, None, None]]], [6, None, None]]])


def even_nodes(root):
    ## If the root is just a leaf, return 1 if it is even 0 if it is odd
    if root.left is None and root.right is None:
        return 1 if root.value % 2 == 0 else 0

    # if the root has at least one child, ask every child the number
    # of even nodes, sum the returned numbers together and add 1 if the
    # root is even, 0 if it is odd
    ret = 1 if root.value % 2 == 0 else 0
    if root.left is not None:
        ret += even_nodes(root.left)
    if root.right is not None:
        ret += even_nodes(root.right)
    return ret

# print(even_nodes(root))


def freq_nodes(root):
    ret = {root.value: 1}
    if root.left is None and root.right is None:
        return ret
    if root.left is not None:
        d = freq_nodes(root.left)
        if root.value in d:
            d[root.value] += 1
        else:
            d[root.value] = 1
        ret = d
    if root.right is not None:
        d = freq_nodes(root.right)
        for k,v in d.items():
            if k in ret:
                ret[k] += v
            else:
                ret[k] = v
    return ret

# root = bt.fromList([7, [4, None, [6, [3, None, [2, None, None]], None]],\
#                     [1, [2, [9, None, None], [3, None, [8, None, None]]], [6, None, None]]])

# print(freq_nodes(root))


"""
Write a recursive function that gets the root of a binary tree as a BinTree
object, defined in the BinTree.py file. The function should return the sum
of all the values of the nodes that are in a even level of the tree,
considering that the root is at level 0.
"""

def sum_even_levels(root, level=0):
    if level % 2 == 0:
        ret = root.value
    else:
        ret = 0
    if root.left is not None:
        ret += sum_even_levels(root.left, level + 1)
    if root.right is not None:
        ret += sum_even_levels(root.right, level + 1)
    return ret


#-------------------------------------WORKING WITH EX TASKS--------------------------------------------------

'''Define the function ex1(string, l), recursive or using recursive functions
or methods, that takes as input a string and an integer l and returns
the set with all the possible anagrams of length l without any double
character that can be built with the characters in string.
If l is bigger than the length of the string, the returned set is empty.

Example:
    ex1('aabca', 4) should return the set
    {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}'''

def anagrams_no_repetition(string, l):
    result = set()
    if l == 1:
        return set(string)
    for i,c in enumerate(string):
        substring = string[:i] + string[i+1:]
        partial_anagrams = anagrams_no_repetition(substring, l-1)
        for partial in partial_anagrams:
            if c != partial[0]:
                result.add(c + partial)
    return result

# print(anagrams_no_repetition('aabca', 4))




'''
    Define the function es5(set, k) that is recursive (or makes use of functions or 
    recursive method(s)) that:
    - receives as arguments a set of strings and an integer k>0 
    - finds the different strings that can be obtained by concatenating k copies of 
    the original strings (the same string can be used multiple times in concatenations). 
    - returns as the result the set of strings found.
    Examples: set={'a','bb','c'}
    1) es5(set, 1) returns the set {'a','bb','c'}
    2) es5(set, 2) returns the set {'aa','abb','ac','bba','bbbb','bbc','ca','cbb','cc'}
    3) es5(set, 3) returns the set
    {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac', 'abbbb', 'acbb', 'cbbc', 
    'bbbba', 'bbabb', 'cbba', 'cac', 'bbac', 'acc', 'aabb', 'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 
    'bbcbb', 'cabb', 'bbcc}

'''

def es5(set1, k):
    if k == 1:
        return set1
    result = set()
    for i in set1:
        val = es5(set1, k-1)
        for partial in val:
            result.add(i+partial)
    return result

# print(es5({'a','bb','c'}, 2))





























