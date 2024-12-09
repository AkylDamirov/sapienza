'''func1: 4 marks
Define the function func1(int_list, m, n) that takes as its
input a list of integers int_list and two integer m and n.
The function returns a dictionary in which the keys are the
integers of the int_list not included in the range [m, n]
included and the corresponding values are the number of
repetition of the key in the int_list.

Example:
    func1([4, 4, 10, 4, 2, 1, 2], 4, 8) should return the dictionary
    {1: 1, 2: 2, 10: 1}
'''

def func1(int_list, m, n):
    dict1 = {}
    for i in int_list:
        if i > n or i < m:
            dict1[i] = int_list.count(i)
    return dict1


# print(func1([4, 4, 10, 4, 2, 1, 2], 4, 8))

''' func2: 4 marks
Define a function func2(str1, str2) that takes as input two strings of
the same length and constructs a new string str3 obtained by
considering, for each pair of characters in str1 and str2 in position i,
the highest one in alphabetical order. The input strings str1 and str2
are made of lower case alphabetical characters. The function returns the
constructed string, all uppercase.

Example:
    func2('plane', 'react') must return the string 'PEACE'

'''
def func2(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str3 = ''
    for i in range(len(str1)):
        if str1[i]<str2[i]:
            str3 += str1[i]
        else:
            str3 += str2[i]
    return str3.upper()
#
# print(func2('plane', 'react'))

''' func3: 4 marks
Define a function func3(L0, L1) that receives 2 lists L0 and L1.
The first list L0 contains strings S0, S1, ... Sn-1,
the second list L1 contains positive integers I0, I1, ... In-1.
The function returns a string obtaining by concatenating each string
Sj repeated Ij times.
For example, if L0 = ['ab', 'o o'] and L1 = [2, 3] the function returns:
'ababo oo oo o'.
'''

def func3(L0, L1):
    new_string = ''
    for i in range(len(L0)):
        new_string += L0[i]*L1[i]
    return new_string

# print(func3(['ab', 'o o'],[2, 3] ))

""" func4: 6 marks
Define a function func4(D) that receives as input a dictionary, in which
each key is a string and the corrisponding value is a collection
(a set, a dictionary, a list, ...).
The function returns a list of lists, in which each sublist S corresponds
to an item of the input dictionary and contains the following:
- as first item I0, the key of the corresponding dictionary item
- as second item I1, the value of the corresponding dictionary item
The sublists are sorted by the length of the second item I1 in each sublists,
in reversed order (from the longest to the shortest).
If the two sublists have a second item with the same length, they are sorted
based on the value of the first item I0 (alphabetically, or numerically).
For example, if D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
the function returns: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
"""

def func4(D):
    list1 = []
    for i,v in D.items():
        list1.append([i,v])
    list1.sort(key=lambda x: (-len(x[1]), x[0]))
    return list1


# print(func4({"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}))


""" func5: 6 marks
Write a function func5(list_A, list_B) that takes two lists with the
same number of strings as input.
The function returns a third list of strings.
Each string in position i in the result list
contains the characters in common between the two strings
in position i in list_A and list_B, all in lower case,
in alphabetical order, and ignoring the case they had
in the strings in list_A and list_B.
The characters in common between the two strings in the two
lists can be in whatever position inside the strings.
The strings in list_A and list_B cannot contain repeating
characters, whatever their case.

For example, if list_A = ["aBd", "baC", "cAb"] and
list_B = ["bcE", "dca", "eDf"], the function returns:
["b", "ac", ""]
"""

def func5(list_A, list_B):
    new_list = []

    for i in range(len(list_A)):
        str_A = list_A[i].lower()
        str_B = list_B[i].lower()

        common = []
        for char in str_A:
            if char in str_B and char not in common:
                common.append(char)
        new_list.append(''.join(sorted(common)))
    return new_list



# print(func5(["aBd", "baC", "cAb"], ["bcE", "dca", "eDf"]))

""" func6: 6 marks
Write a function func6(a_dictionary) that takes a dictionary as
parameter, in which:
- the keys are single alphabetical characters
- the items are lists of positive integers

The function returns the character for which the corresponding
list of integers sums to the highest value. If multiple characters
sum to the same maximum value, the first one in alphabetical order
is returned.

For example, func2({"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]})
returns "b", as the list [4, 2, 3] sums to the highest value among all
the lists in the dictionary.
"""


def func6(a_dictionary):
    highest_sum = ''
    sum1 = 0
    for i, v in a_dictionary.items():
        if sum(v) > sum1 or (sum(v) == sum1 and i < highest_sum):
            highest_sum = i
            sum1 = sum(v)

    return highest_sum

# print(func6({"a" : [3, 2, 2], "b" : [4, 2, 3], "c" : [-4, 2, 2]}))










