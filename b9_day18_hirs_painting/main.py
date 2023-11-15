import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)

rgb_colors = []
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)