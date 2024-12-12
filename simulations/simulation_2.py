'''func1: 4 marks

Define the function func1(file_in) that takes as input a string indicating
the path to a text file and returns a list of strings. The function opens the
text file and extracts all words, converting them all to lowercase. The
function returns a list of unique words found in the text file,
sorted in alphabetical order.
Words are sequences of characters (alphabetical and non-alphabetical)
separated by any number of spaces, tabs or newlines.

Example:
if file_in points to 'txt/in_01.txt', the function returns
expected = ['bat', 'car', 'cat', 'condor', 'rat']

'''

def func1(file_in):
    file = open(file_in, 'r', encoding='utf8')
    list1 = []
    for i in file.read().lower().split():
        if i not in list1:
            list1.append(i)
    file.close()
    list1.sort()
    return list1

# print(func1('/Users/admin/PycharmProjects/pythonProject/sapienza/in_01.txt'))

''' func2: 4 marks
Define the function func2(file_in_a)
that takes as input 1 string pointing to a text file.

The function opens the text files and looks for
sequences of any number of consecutive spaces.
Sequences of spaces cannot span multiple lines.
That is, a sequence of consecutive spaces will interrupt
when a newline character is reached.
The function returns the longest sequence of consecutive
spaces found in the file.

Example:
for input 'txt/in_01.txt' the function returns 
'''

def func2(file_in_a):
    longest = 0
    count = 0
    file = open(file_in_a, 'r', encoding='utf8')
    for i in file.read():
        if i == ' ':
            count += 1
        else:
            if count > longest:
                longest = count
            count = 0
    file.close()
    return longest


# print(func2('/Users/admin/PycharmProjects/pythonProject/sapienza/in_01.txt'))

'''func3: 6 marks
Implement the func3(list_s, list_i, filepath): 
that takes as arguments: 
- a list of lists of strings, called list_s 
- a list of lists of integers, called list_i 
- a string filepath, indicating the path of a text file the function must write.
The inner lists of list_s and list_i have the same number of elements.
The function returns an integer.

For each list of words in list_s, the function writes a line in filepath.  
The writing order of the words on each line is specified 
by the corresponding list of integers in list_i, which should be 
considered as the positions of the words to read from the lists 
and write to the file.

The function returns the total number of words written to the out file.

Example if:
lists = [["monkey", "cat",], 
         ["panda", "alligator"], 
         ["zoo", 'zuu','zotero']] 
listi=  [[1, 0],	# first the word at position 1 then 0
         [0, 1],	# first the word at position 0 then 1
         [2, 1, 0]]	# first the word at position 2 then 1 then 0
the return value is 7 and the file out contains:

cat monkey
panda alligator
zotero zuu zoo
'''


def func3(list_s, list_i, filepath):
    word_count = 0
    with open(filepath, 'w', encoding='utf8') as f:
        for words, indices in zip(list_s, list_i):
            for index in indices:
                f.write(words[index] + ' ')
                word_count += 1
            f.write('\n')
    return word_count

""" func4: 6 marks

Write a function func4(list_A) that takes a list of tuples.
In each tuple, the first item is a string, the second item is a list
of integers.
The function returns a dictionary, in which:
- each key K is one of the strings in the tuples in list_A;
- the corresponding value V is the list obtained by merging
  the lists in the tuples of list_A having K as first item, sorted
  in ascending order; V cannot contain duplicates.

For example, if list_A = [("cat", [7, 3]), ("dog", [1, 4]), ("cat", [2, 7])]
the function returns {"cat":[2, 3, 7], "dog": [1, 4]}
"""


def func4(list_A):
    dict1 = {}
    for i in list_A:
        if i[0] not in dict1:
            dict1[i[0]] = i[1]
        elif i[0] in dict1:
            for j in i[1]:
                if j not in dict1[i[0]]:
                    dict1[i[0]].append(j)
    for i,v in dict1.items():
        v.sort()
    return dict1


""" func5: 6 marks

Write a function that reads an input file filein and writes a file fileout.
All the words read from the file input are written in the file in output in one
single line, separated by a comma followed by one space and sorted by their
lengths in decreasing order, in case of a tie, by the number of vowels in
increasing order and, finally, in alphabetical order.
The function returns the number of words found in filein.
"""


def func5(filein, fileout):
    file1 = open(filein, 'r', encoding='utf8')
    list1 = []
    for i in file1.read().split():
        list1.append(i)
    list1.sort(key=lambda x: (-len(x), sum(c in 'aeiouAEIOU' for c in x),x))
    file1.close()
    file2 = open(fileout, 'w', encoding='utf8')
    for i in list1:
        file2.write(i + ', ')
    file2.close()
    return len(list1)


''' func6: 8 marks

Write a function func5(folderpath) that reads the content of a given folder,
including all files and subfolders within it, recursively.

The function should return a dictionary with the following keys and values:
- "file_paths": A list of file paths (as strings) for all files
  in the folder and its subfolders, sorted by the length of each path.
  If paths have the same length, they should be sorted alphabetically.
- "subfolder_paths": A list of paths (as strings) for all subfolders
  in the folder and its subfolders, sorted by the length of each path.
  If paths have the same length, they should be sorted alphabetically.

If the folder contains no files, "file_paths" should be an empty list.
If the folder contains no subfolders, "subfolder_paths" should be an empty list.

YOU CANNOT USE THE FUNCTION os.walk()

Hint:
- You can use the os.listdir() function to get a list of items in a folder.
- To create the full path for each item, join the folder path and item name with +'/'+.
- To check if an item is a file or a folder, use os.path.isfile() or os.path.isdir().

Example:

Suppose the folder contains the following structure:
- A file at "folder/b.txt"
- A file at "folder/subfolder/abc.txt"
- A file at "folder/a.txt"
- A subfolder at "folder/subfolder"
- A subfolder at "folder/subfolder/nested_folder"

The function will return:

{
  "file_paths": ["folder/a.txt", "folder/b.txt", "folder/subfolder/abc.txt"],
  "subfolder_paths": ["folder/subfolder", "folder/subfolder/nested_folder"]
}
'''

from os import listdir
from os.path import isfile, isdir, join


def my_key(x):
    return (len(x), x)


def func6(folderpath):
    dict1 = {'file_paths': [],
             'subfolder_paths': []}
    for i in listdir(folderpath):
        item_path = join(folderpath, i)
        if isfile(item_path):
            dict1['file_paths'].append(item_path)
        elif isdir(item_path):
            dict1['subfolder_paths'].append(item_path)

            subresult = func6(item_path)
            dict1['file_paths'] += subresult['file_paths']
            dict1['subfolder_paths'] += subresult['subfolder_paths']

    dict1['file_paths'] = sorted(dict1['file_paths'], key=my_key)
    dict1['subfolder_paths'] = sorted(dict1['subfolder_paths'], key=my_key)

    return dict1