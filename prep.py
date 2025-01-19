# def merge_dicts_with_lists(dicts):
#     new_dict = {}
#     for dict in dicts:
#         for i,v in dict.items():
#             if i not in new_dict:
#                 new_dict[i] = v
#             else:
#                 for j in v:
#                     if j not in new_dict[i]:
#                         new_dict[i].append(j)
#     return new_dict
#
# print(merge_dicts_with_lists([{ "a": [1, 2], "b": [3] }, { "a": [2, 4], "c": [5, 6] }]))

# sum(elements) * len(elements)
# def max_weighted_list(L):
#     max_weight = None
#     max_s = 0
#     for i in L:
#         if sum(i)*len(i)>max_s:
#             max_weight = i
#             max_s = sum(i)*len(i)
#     return max_weight
#
# print(max_weighted_list([[1, 1, 0], [1, 0, 1, 1], [1, 2], [1, 1, 0, 0]]))


# def word_frequency(input_filename, output_filename):
#     file = open(input_filename)
#     dict1 = {}
#     for i in file.read().split():
#         if i not in dict1:
#             dict1[i] = 1
#         else:
#             dict1[i] += 1
#     file.close()
#     sorted_words = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
#     file2.txt = open(output_filename, 'w')
#     uniq_words = 0
#     for i,v in sorted_words:
#         file2.txt.writelines(f'{i}: {v}\n')
#         uniq_words += 1
#     file2.txt.close()
#     return uniq_words
#
#
# print(word_frequency('text.txt', '3131.txt'))


# from images.images import load, save, visd
# def detect_colors(image_path):
#     image = load(image_path)
#     dict1 = {}
#     for line in image:
#         for i in line:
#             if i != (0,0,0) and i not in dict1:
#                 dict1[i] = 1
#             elif i != (0,0,0) and i in dict1:
#                 dict1[i] += 1
#     return dict1
# print(detect_colors('images/Mario.png'))
# from os import listdir
# from os.path import isdir, isfile, join
#
# def directory_search(path, keyword):
#     list1 = []
#     for i in listdir(path):
#         current_path = join(path, i)
#         if current_path.endswith('txt'):
#             file = open(current_path)
#             for j in file.read().split():
#                 if j == keyword:
#                     list1.append(current_path)
#         elif isdir(current_path):
#             rec = directory_search(current_path, keyword)
#             if rec not in list1 and rec:
#                 list1.append(rec)
#     return list1
#
# print(directory_search('.', 'hello'))

# def longest_line(input_filename):
#     file = open(input_filename)
#     max_length = 0
#     max_line = ''
#     for i in file.readlines():
#         counter = 0
#         for j in i:
#             counter += 1
#         if counter > max_length:
#             max_line = i
#             max_length = counter
#     file.close()
#     return max_line
#
# print(longest_line('test1.txt'))

from os import listdir
from os.path import isfile, isdir, join

# def count_files(path):
#     counter = 0
#     for i in listdir(path):
#         current_path = join(path, i)
#         if isfile(current_path):
#             counter += 1
#         elif isdir(current_path):
#             counter += count_files(current_path)
#     return counter
#
# print(count_files('.'))


# def path_to_files(path):
#     files = []
#     for i in listdir(path):
#         current_path = join(path, i)
#         if isfile(current_path):
#             files.append(current_path)
#         elif isdir(current_path):
#             sub = path_to_files(current_path)
#             files.extend(sub)
#     return files
#
# print(path_to_files('.'))

# def replace_words(input_filename, output_filename, word_map):
#     file = open(input_filename)
#     file2 = open(output_filename, 'w')
#     changed = 0
#     for j in file.readlines():
#         for i in j.split():
#             if i not in word_map:
#                 file2.write(f'{str(i)} ')
#             else:
#                 file2.write(f'{str(word_map[i])} ')
#                 changed += 1
#         file2.write('\n')
#     file.close()
#     file2.close()
#     return f'changed words: {changed}'
#
# print(replace_words("test1.txt", "output.txt", {"hello": "hi", "world": "Earth"}))

# def sum_numbers(input_filename):
#     file = open(input_filename)
#     sum1 = 0
#     for i in file.read().split():
#         if i.isdigit():
#             sum1 += int(i)
#     file.close()
#     return sum1
#
# print(sum_numbers('test1.txt'))

# def find_duplicates(input_filename, output_filename):
#     file = open(input_filename)
#     list1 = []
#     for i in file.read().split():
#         list1.append(i)
#     new_list = []
#     for i in list1:
#         if i not in new_list and list1.count(i) > 1:
#             new_list.append(i)
#     file.close()
#     file2 = open(output_filename, 'w')
#     for i in new_list:
#         file2.write(f'{i}\n')
#     file2.close()
#     return new_list
#
# print(find_duplicates('test1.txt', 'output.txt'))














