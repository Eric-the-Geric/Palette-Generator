from sklearn.cluster import KMeans
from PIL import Image, ImageEnhance
import numpy as np

def rgb_to_hex(pixel):
    return '#{:02x}{:02x}{:02x}'.format(int(pixel[0]), int(pixel[1]), int(pixel[2]))

def clustering(image, n_values):
    kmeans = KMeans(n_clusters=n_values, random_state=0, n_init="auto")
    kmeans.fit(image)
    return process_to_pixels(kmeans.cluster_centers_)

def get_image(path):
    image = Image.open(path)
    np_image = np.asarray(image)
    pixel_list = np_image.reshape([np_image.shape[0]*np_image.shape[1], np_image.shape[2]])
    return pixel_list

def get_image_contrast(path):
    image = Image.open(path)
    enhancer = ImageEnhance.Contrast(image)
    factor = 1.3
    image = enhancer.enhance(factor)
    np_image = np.asarray(image)
    pixel_list = np_image.reshape([np_image.shape[0]*np_image.shape[1], np_image.shape[2]])
    return pixel_list

def process_to_pixels(centroids):
    processed_centroids = np.round(centroids)%255
    return processed_centroids


def kmeans_clustering_algorithm(path, n_values):
    image_normal = get_image(path) # gets a list of pixels
    image_bright = get_image_contrast(path)
    centroids_normal = clustering(image_normal, n_values)
    centroids_bright = clustering(image_bright, n_values)
    sorted_centroids_normal = np.array(sorted(centroids_normal, key=lambda x: (x[0]+x[1]+x[2])/3))
    sorted_centroids_bright = np.array(sorted(centroids_bright, key=lambda x: (x[0]+x[1]+x[2])/3))

    most_frequent_hex_n = [rgb_to_hex(p) for p in sorted_centroids_normal]
    most_frequent_hex_b = [rgb_to_hex(p) for p in sorted_centroids_bright]

    polybar_colours = ["background =",
                        "background-alt =",
                        "disabled=",
                        "primary =",
                        "secondary =",
                        "alert =",
                        "foreground ="]

    alacritty_colours = [
                        "black =", #0, 0, 0
                        "blue =", #0,0, 255
                        "cyan =", #0, 255, 255
                        "green =", #0, 255, 0
                        "magenta =", # 255,0,255
                        "yellow =" , # 255, 255, 0 
                        "red =", # 255, 0,0 
                        "white ="] # 255, 255, 255

    list_of_variables = [
            "set $blue",
            "set $gray",
            "set $darkgray",
            "set $purple",
            "set $red",
            "set $yellow",
            "set $green",
            "set $bg",
            "set $aqua",
            ]
    new_config_i3 = [s+ " " + m + "\n" for s, m in zip(list_of_variables, most_frequent_hex_b)]
    coni3 = "".join(new_config_i3)

    new_config_n = [s+ " " + f'"{m}"'.replace("#","0x") + "\n" for s, m in zip(alacritty_colours, most_frequent_hex_n)]
    new_config_b = [s+ " " + f'"{m}"'.replace("#","0x") + "\n" for s, m in zip(alacritty_colours, most_frequent_hex_b)]
    con_n = "".join(new_config_n)
    con_n = "[colors.normal]\n" + con_n
    con_b = "".join(new_config_b)
    con_b = "[colors.bright]\n" + con_b

    con_alac = con_n + "\n" + con_b
    
    new_config_pb = [s+" " +m+ "\n" for s, m in zip(polybar_colours, most_frequent_hex_n)]
    con_pb = "".join(new_config_pb)
    con_pb = "[colors]\n" + con_pb
    configuration_updates = {"i3":
                             {"config": coni3},
                             "alacritty": 
                             {"config": con_alac},
                             "polybar":
                              {"config": con_pb},
                              }
    return configuration_updates


if __name__ == "__main__":
   con = kmeans_clustering_algorithm("/home/eric/Photos/wallapers/wp2560314-1147628006.jpg", 9)
   print(con["i3"]["config"])
  # with open("/home/eric/.config/alacritty/colourme.toml", "w") as f:
  #     f.write(con)

