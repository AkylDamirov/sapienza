from images import load, save, visd


def func4(image_path):
    image = load(image_path)
    count = 0
    for line in image:
        temp = 0
        for i in range(len(line)):
            if line[i] == (255, 255, 255):
                temp +=1
            else:
                if temp>count:
                    count = temp       
        
    return count         

print(func4('../sample_images/image02.png'))