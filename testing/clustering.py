from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_hex(pixel):
    return '#{:02x}{:02x}{:02x}'.format(int(pixel[0]), int(pixel[1]), int(pixel[2]))

def clustering(kmeans, image):
    kmeans.fit(image)
    return kmeans.cluster_centers_

def get_image(path):
    image = Image.open(path)
    image.load()
    np_image = np.asarray(image)
    pixel_list = np_image.reshape([np_image.shape[0]*np_image.shape[1], np_image.shape[2]])
    return pixel_list

def process_to_pixels(centroids):
    processed_centroids = np.round(centroids)%255
    return processed_centroids


def kmeans_clustering_algorithm(path, n_values):
    kmeans = KMeans(n_clusters=n_values, random_state=0, n_init="auto")
    #path = "/home/eric/Photos/wallapers/UcRt14.jpeg" #demon slayer for testing
    image = get_image(path) # gets a list of pixels
    centroids = clustering(kmeans, image)
    centroids = process_to_pixels(centroids)
    sorted_centroids = np.array(sorted(centroids, key=lambda x: (x[0]+x[1]+x[2])/3))
    most_frequent_hex = [rgb_to_hex(p) for p in sorted_centroids]
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
#return sorted_centroids

    


if __name__ == "__main__":
   con = kmeans_clustering_algorithm("/home/eric/Photos/wallapers/wp2560314-1147628006.jpg", 9)

