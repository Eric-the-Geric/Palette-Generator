import argparse
from colour_extractor import colour_palette
#from testing.clustering import kmeans_clustering_algorithm
from cluster_extractor import kmeans_clustering_algorithm

def main():
    parser = argparse.ArgumentParser(description='pull color palette from bg and pass to i3')
    parser.add_argument('-p', '--palette',
                        help='file to get the colour palette',
                        type=str
                        )
    parser.add_argument('-n', '--integer',
                        help='how many colours you want to extract',
                        type=int,
                        )
    parser.add_argument('-i', '--i3',
                        help='path to the i3 config',
                        type=str
                        )
    parser.add_argument('-a', '--alacritty',
                        help='path to the alacritty config',
                        type=str
                        )
    args = parser.parse_args()
    #print(args.string)
    #with args.file as file:
        #file.writelines(["testing123\n", args.string+"\n"])

    #new_text = colour_palette(path=args.palette, n_values=args.integer)
    #new_text = kmeans_clustering_algorithm(args.palette, args.integer)
    configurations = kmeans_clustering_algorithm(args.palette, args.integer)
    i3_conf = configurations["i3"]["config"]
    alac_conf = configurations["alacritty"]["config"]

    alacritty_path = args.alacritty
    i3_path = args.i3
    start_mark = "#>>>>>colours>>>>>\n"
    end_mark =  "#<<<<<colours<<<<<"
    i3_conf= start_mark + i3_conf + end_mark 

    with open(i3_path, 'r') as  file:
        content = file.read()


    start_index = content.find(start_mark)
    end_index = content.find(end_mark, start_index)
    if start_index != -1 and end_index != -1:
        content = content[:start_index] + i3_conf+ content[end_index + len(end_mark):]

    # Write the modified content back to the file
    with open(i3_path, 'w') as file:
        file.write(content)

    with open(alacritty_path, 'w') as f:
        f.write(alac_conf)


if __name__ == "__main__":
    main()

