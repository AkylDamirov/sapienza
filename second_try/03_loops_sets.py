# 1. Write a program that gets a list of strings and returns a new list. For each string in the original
# list the new list contains an int obtained summing up the digits found in that string.
# Example: if the original list is ['c4sd43', 'roger', 'M00n35', 'E5591'] the function should return the list [11, 0, 8, 20].


# def func1(list1):
#     new_string = []
#     for i in list1:
#         digits = 0
#         for j in i:
#             if j.isdigit():
#                 digits += int(j)
#         new_string.append(digits)
#     return new_string
#
# print(func1(['c4sd43', 'roger', 'M00n35', 'E5591']))

# 2. Write a program that gets a list of strings made of 0s and 1s and returns a new list. For each string in the original
# list the new list contains the int corresponding to the binary representation of that string.
# Example: if the original list is ['101', '1110', '1', '10001'] the function should return the list [5, 14, 1, 17].

# def func2(list1):
#     new_list = []
#     for i in list1:
#         summ = 0
#         for ind, j in enumerate(i[::-1]):
#             if j == '0':
#                 continue
#             else:
#                 summ += 2**ind
#         new_list.append(summ)
#     return new_list
#
# print(func2(['101', '1110', '1', '10001']))

# 3. Write a program that gets a list of strings and a list of ints and returns a string. The new string is obtained
# taking, for each string of the first list, the character at the index in the corresponding int of the second list.
# Example: if the first list is ['cabbage', 'television', 'music', 'bartender'] and the scond list is [3, 2, 2, 2],
# the function should return the string 'best'.

# def func3(list1, list2):
#     str1 = ""
#     for i in range(len(list1)):
#         str1 += list1[i][list2[i]]
#     return str1
#
# print(func3(['cabbage', 'television', 'music', 'bartender'],[3, 2, 2, 2] ))


# 4. Write a program that gets two lowercase strings and prints:
# • a set with the characters that are in both the strings
# • a set with the characters that are in one but not both the strings
# • a set with the characters that are in none of the strings.

# def func4(str1, str2):
#     first1_set = set()
#     second_set = set()
#     third = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
#              'j', 'k', 'l',
#              'z', 'x', 'c', 'v', 'b', 'n', 'm'}
#     for i in str1:
#         if i in str2 and i not in first1_set:
#             first1_set.add(i)
#         elif i not in str2 and i not in second_set:
#             second_set.add(i)
#         if i in third:
#             third.add(i)
#     for i in str2:
#         if i not in str1:
#             second_set.add(i)
#         if i in third:
#             third.remove(i)
#     return first1_set, second_set, third
#
#
# print(func4('test', 'qwerty'))

# 5. Write a program that gets a list of strings and returns a new list without duplicates.
# def func5(list1):
#     new = []
#     for i in list1:
#         if i not in new:
#             new.append(i)
#     return new






