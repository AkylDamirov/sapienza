# file = open('text.txt', 'r', encoding='utf8')
# without read() you will read lines
# without split() in the loop you will read single letter
# for index, line in enumerate(file.read().split()):
#    print(index, line)

# read only one line
# print(file.readline())
# file.close()

# with its alternative to open() and close()
# with open('text.txt', 'r', encoding='utf8') as file:
#    for i in file:
#        print(i)

#to reser cursor file.seek(0)

# ----------------------------------------

# problem: write a program that reads the contents of a text
# file and outputs the number of lines, words and letters
# found

# ----------------------------------------

file = open('../text.txt', 'r', encoding='utf8')
def func(file):
    number_of_lines = len(file.readlines())
    file.seek(0)
    number_of_words = len(file.read().split())
    number_of_letters = 0
    file.seek(0)
    for i in file.read():
        if i.isalpha():
            number_of_letters +=1

    return f'number of lines: {number_of_lines} \n number of words: {number_of_words} ' \
           f'\n number of letters: {number_of_letters}'

# print(func(file))
file.close()


# ----------------------------------------

# problem: write a function that takes the name of a text file
# and produces a censored copy in which all the 'banned
# words' have been bleeped out with asterisks

# ----------------------------------------

def func2(new_name, file):
    file = open('../text.txt', 'r', encoding='utf8')
    content = file.readlines()
    modified = [line.replace('bitch', '*****') for line in content]

    file = open(new_name, 'w', encoding='utf8')
    file.writelines(modified)

    file.close()

# func2('new_log', file)







