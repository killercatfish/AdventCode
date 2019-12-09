WIDTH = 25
HEIGHT = 6

def get_input(file_name):
    input = []

    with open(f'../input/{file_name}.txt'.format(file_name, 'wb')) as f:
        # with open("input/day5_test_input.txt") as f:
        #     input = f.split(',')
        for line in f:
            l = line.strip()
            # print(l)
            layer = []
            counter = 1
            for d in l:
                layer.append(int(d))
                if counter % WIDTH == 0: #150 is the width x height
                    input.append(layer)
                    layer = []
                counter += 1

    return input

input = get_input('day_8_input')

print(input)
layers = []
counter = 1
layer = []
for i in input:
    layer.append(i)
    if counter % HEIGHT == 0:
        layers.append(layer)
        layer = []
    counter += 1
#
# for i in layers:
#     for j in i:
#         print(j)
#     print('\n\n')

# print(len(layers))

message = []
for y in range(HEIGHT):
    message.append([])
    for x in range(WIDTH):
        message[y].append(0)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print("\n***(" + str(x) + ", " + str(y) + ")***\n")
        # print(layers[0][y][x])
        for i in range(len(layers)):
            # print(layers[i][y][x])
            if layers[i][y][x] != 2:
                message[y][x] = layers[i][y][x]
                break

for i in message:
    print(i)
    print('\n')
'''
Test code for scanning through lines
'''
# for i in message:
#     print(i)
#     print('\n')
#
# layer_z = ""
#
# for y in range(HEIGHT):
#     for x in range(WIDTH):
#         # print("\n***(" + str(x) + ", " + str(y) + ")***\n")
#         # print(layers[0][y][x])
#         layer_z += str(layers[0][y][x])
#         message
#     layer_z += '\n'
#
# check_layer = ""
#
# for i in layers[0]:
#     layer = [str(p) for p in i]
#     layer = "".join(layer)
#     check_layer += layer
#     check_layer += '\n'
#
# print(check_layer)
# print('\n')
# print(layer_z)
#
# print(check_layer == layer_z)



#
#
# LAYERS = int(len(input))
#
# input_layers =[]
#
# for i in input:
#     layer = []
#     row = []
#     for p in range(len(i)):
#         row.append(i[p])
#         if p % WIDTH == 0 and p != 0:
#             layer.append(row)
#             row = []
#     input_layers.append(layer)
#
# for l in input_layers:
#     for r in l:
#         print(r)
#     print("\n\n")




#
# print(LAYERS)
# print(input)
#
# pixel_color = []
#
# for p in range(WIDTH * HEIGHT):
#     for l in range(LAYERS):
#         # print(input[l][p])
#         if input[l][p] != 2:
#             pixel_color.append(input[l][p])
#             break
#
# layers_text = []
# for i in input:
#     layer = [str(p) for p in i]
#     layer = "".join(layer)
#     print(layer, end="\n")
#
# # print(layers_text)
#
#
#
# print(pixel_color)
# image = ""
#
# for p in range(len(pixel_color)):
#     if p % WIDTH == 0:
#         image += '\n'
#     image += str(pixel_color[p])
#
# print(image)
#




from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (WIDTH, HEIGHT), "black") # create a new black image
pixels = img.load() # create the pixel map
counter = 0
for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        if(message[j][i] == 0):
            pixels[i,j] = (0, 0, 0) # set the colour accordingly
        else:
            pixels[i, j] = (255, 255, 255)  # set the colour accordingly
        counter += 1

img.show()
size = (WIDTH * 10, HEIGHT * 10)
out = img.resize(size)
out.show()
