# 1. Write a function that gets an image as input and returns a dictionary in which the keys are the colors in
# the image and the corresponding values are the number of pixels in the image with the corresponding color
# (namely, a dictionary with the frequencies for each color of the image)

# def func1(img):
#     image = load(img)
#     dict1 = {}
#     for line in image:
#         for i in line:
#             if i not in dict1:
#                 dict1[i] = 0
#             else:
#                 dict1[i] += 1
#     return dict1
#
# print(func1('sample_images/image01.png'))

# 2. Write a function recolor that, given an image and a dictionary as input, modifies in place the image according
# to the values in the input dictionary, which has keys and values as tuples of colors. The function should change
# each image pixel with a key in the dictionary with the corresponding value.
# Example : if d = {(255,0,0):(0,255,0)}, then the call recolor(image, d)
# must modify any red pixel of image with a green pixel, making the image loaded from the file
# image04.png to become as the image in image05.png

# def func2(img, d):
#     image = load(img)
#     for line in image:
#         for i in range(len(line)):
#             if line[i] in d:
#                 line[i] = d[line[i]]
#     save(image, 'test_image.png')
#
#
#
# func2('sample_images/image04.png', {(255,0,0):(0,255,0)})

# 3. Write a function that, given an image as input, returns the number of pixels intersecting a vertical line
# with a horizontal line. Assume that:
# • the image has a black background
# • that the vertical and horizontal lines are as long as the height and width of the image, respectively
# • that the lines are not drawn close to each other and to the borders.

# def func3(image):
#     image = load(image)
#     counter = 0
#     for line in range(len(image)):
#         for i in range(len(image[line])):
#             try:
#                 if image[line][i] == image[line][i+1] and image[line][i] == image[line][i-1] \
#                     and image[line][i] == image[line-1][i] and image[line][i] == image[line+1][i] and \
#                         image[line][i] == (255, 255, 255):
#                     counter += 1
#             except:
#                 continue
#     return counter
#
# print(func3('./sample_images/image09.png'))

# 4. Write a function that takes as input the string representing name of a png file and returns an integer.
# The image is black with some white horizontal segments that never intersect. The function has to return
# the number of pixels of the longest white segment in the image. An example is the image in image02.png, for
# which the function should return the value 33.

# def func4(image):
#     image = load(image)
#     max_length = 0
#     for line in range(len(image)):
#         counter = 0
#         list1 = []
#         for i in range(len(image[line])):
#             if image[line][i] == (255,255,255):
#                 counter += 1
#             else:
#                 list1.append(counter)
#                 counter = 0
#         if list1:
#             if max(list1) > max_length:
#                 max_length = max(list1)
#     return max_length
#
# print(func4('./sample_images/image02.png'))

# 5. Write a function that takes the string representing a png file’s name and returns an integer as input.
# The image is black with some white vertical segmentes, never intersecting. The function has to return
# the number of pixels of the longest white segment in the image. An example is the image in image06.png,
# for which the function should return the value 33.

# def func5(image):
#     image = load(image)
#     max_length = 0
#     dict1 = {}
#     for line in range(len(image)):
#         for i in range(len(image[line])):
#             if image[line][i] == (255, 255, 255):
#                 if i not in dict1:
#                     dict1[i] = 1
#                 else:
#                     dict1[i] += 1
#
#     for i,v in dict1.items():
#         if v > max_length:
#             max_length = v
#     return max_length
#
#
# print(func5('./sample_images/image06.png'))

# 6. Write a function that takes the string representing a png file’s name and returns an integer as input.
# The image is a black image with some white segments that join vertically and horizontally but never intersect.
# The function has to return the number of pixels of the longest white segment in the image. Examples are the images
# in image07.png image08.png for which the function should return the values 115 and 148, respectively.















