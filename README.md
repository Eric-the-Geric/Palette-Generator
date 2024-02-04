
# Palette-Generator
An extremely simple colour palette generator
- takes the the current wallpaper nitrogen is using
- extracts the colour palette using a the least frequent colours
- regenerates the i3 config using the colour palette 

## requirements
- grep
- nitrogen
- i3

# Todo
- super slow so need to optimize. probably just redo it in C
- impliment a clustering (like k means clustering) and use a modified version of TF-IDF to extract representative pixels
- make is so you can choose which config file to use
- turn the script into an executable so i can call it whenever
