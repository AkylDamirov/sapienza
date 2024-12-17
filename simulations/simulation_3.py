""" func1: 6 marks

Define a function func1(img_in) that takes as input
a string containing the path to a file with an image in
PNG format.
The function should return the number of pixels in the image
whose red channel is strictly greater than 150.
To read/write images you must use the load/save functions in
the "images" module we saw in the classes.
"""

import images


def func1(img_in):
    count = 0
    image = images.load(img_in)
    for line in image:
        for i in range(len(line)):
            if line[i][0] > 150:
                count += 1

    return count



""" func2: 8 marks

Define a function that, given the path to a file (img_in) containing 
an image, generates another image obtained by incrementing the
the blue channel of the input image by a the input parameter val. 
If the result of the increment exceeds 255, the module will be applied
to brng it again in the range [0, 255]. For example, 240+100 -> 85.
The resulting image is saved to the file whose path is in img_out.
The function returns the number of pixels whose blue channel
exceeded 255.
To read/write images you must use the load/save functions in
the "images" module we saw in the classes.
"""

import images


def func2(img_in, img_out, val):
    img = images.load(img_in)
    width = len(img[1])
    height = len(img)
    count = 0

    for i in range(height):
        for j in range(width):
            R = img[i][j][0]
            G = img[i][j][1]
            B = img[i][j][2]
            img[i][j] = (R, G, (B + val) % 256)

            if B + val > 255:
                count += 1
    images.save(img, img_out)
    return count


def func3(input_pngfile):
    image = images.load(input_pngfile)
    height = len(image)
    width = len(image[0])
    result = []

    for i in range(height):
        x_start = -1
        x_end = -1

        for j in range(width):
            if image[i][j] == (255, 255, 255):
                if x_start == -1:
                    x_start = j
                x_end = j
            elif x_start != -1:
                break

        if x_start != -1:
            result.append((i, x_start, x_end))

    return result


''' func4: 8 marks

Define a function func4 that takes as input the path to an RGB image
"input_file_name".
The function counts and returns the number of image non-black pixels that are
preceded and followed by black pixels (i.e., given a pixel P,
there is one black pixel that precedes it and one that follows it).
If the non-black pixel is on the right edge of the image, 
only the preceding pixel is considered. 
Similarly, if the non-black pixel is on the left edge
of the image, only the pixel following it is considered.
In addition, the function creates and saves an RGB image with the same width and height
of the input image, in which only the counted pixels are copied.
To read/write images you must use the load/save functions in
the "images" module we saw in the classes.

For example, if B represents a black pixel and * represents
a non-black pixel, given the image:

BB*BBB*
*BB*BB
B*BB**B*
BBBBB*B
*BBB**BB

The function returns 8 and saves the image:

BB*BBB*
*BBB*BBB
B*BBBBB*
BBBBB*B
*BBBBBBB
'''

import images


def func4(input_file_name, output_file_name):
    black = (0, 0, 0)
    img = images.load(input_file_name)
    newim = []
    counter = 0
    for r, row in enumerate(img):
        newrow = []
        if row[0] != black and row[1] == black:
            newrow.append(row[0])
            counter += 1
        else:
            newrow.append(black)
        for p in range(1, len(row) - 1):
            pixel = row[p]
            if pixel != black and row[p - 1] == black and row[p + 1] == black:
                newrow.append(pixel)
                counter += 1
            else:
                newrow.append(black)
        if row[-1] != black and row[-2] == black:
            newrow.append(row[-1])
            counter += 1
        else:
            newrow.append(black)
        newim.append(newrow)
    images.save(newim, output_file_name)
    return counter

