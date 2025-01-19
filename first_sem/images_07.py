from images.images import load,save,visd
def mario_to_luigi():
    image = load('../sample_images/Mario.png')
    for line in image:
       for i in range(len(line)):
           if line[i] == (227,6, 19): #red pixel
               line[i] = (0, 191, 99) # green pixel

##print(image)
#save(image, 'Luigi.png')
#visd(image)

#exersice number 1
# from images import load, save, visd
def func_count_color(image_path):
    image = load(image_path)
    dict1 = {}
    for line in image:
        for i in range(len(line)):
            if line[i] not in dict1:
                dict1[line[i]] = 1
            else:
                dict1[line[i]] += 1 
    return dict1            

# print(func_count_color('Mario.png'))

#exersice number 2

def recolor(image_path, dict1):
    image = load(image_path)
    for line in image:
        for i in range(len(line)):
            if line[i] in dict1:
                line[i] = dict1[line[i]]
    return image
# print(recolor('Mario.png', {(0,0,0):(1,1,1)}))

# function number 4
def func4(image_path):
    image = load(image_path)
    count = 0
    for line in image:
        temp = 0
        for i in range(len(line)):
            if line[i] == (255, 255, 255):
                temp += 1
            else:
                if temp > count:
                    count = temp

    return count