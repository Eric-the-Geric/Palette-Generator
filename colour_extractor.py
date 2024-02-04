from PIL import Image
#import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sns
#import sys
def rgb_to_hex(pixel):
    return '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])

def colour_palette(path="/home/eric/Photos/wallapers/background.png", n_values=9):
    image = Image.open(path, "r")
    pixel_values = list(image.getdata())
    pixel_set = set(pixel_values)

    pixel_freq: dict[tuple:int] = {tup:0 for tup in pixel_set}



    for pixel in pixel_values:
        pixel_freq[pixel]+=1

    sorted_list = sorted(pixel_freq.items(), key = lambda x: x[1], reverse=True)
    most_frequent = sorted_list[-n_values:]
    colours = [pix for pix, count in most_frequent]
    brightness = [((t[0]+t[1]+t[2])/3, i) for i, t in enumerate(colours)]
    sorted_brightness = sorted(brightness, key=lambda x: x[0])
    sorted_colours = [colours[i] for b, i in sorted_brightness]
    most_frequent_hex = [rgb_to_hex(p) for p in sorted_colours]
    list_of_variables = [
            "set $bg",
            "set $gray",
            "set $darkgray",
            "set $red",
            "set $green",
            "set $yellow",
            "set $blue",
            "set $purple",
            "set $aqua",
            ]
    new_config = [s+ " " + m + "\n" for s, m in zip(list_of_variables, most_frequent_hex)]
    con = "".join(new_config)
    return con
   # for s, m in zip(list_of_variables,most_frequent_hex):
   #     print(s, m)
    
    #print(most_frequent_pixels)
    #colours = []
    #for i in range(9):
    #    if i%2 == 0:
    #        colours.append(most_frequent_pixels[i])
    #print(colours)

   # pixel_freq.clear()
   # 
   # for key, value in sorted_list:
   #     pixel_freq[key] = value


   # palette = np.array(sorted_colours)[np.newaxis, :, :]
   # plt.imshow(palette)
   # plt.axis('off')
   # plt.show()
   # plt.savefig('test.png')

if __name__=="__main__":
    colour_palette(n_values=9)
