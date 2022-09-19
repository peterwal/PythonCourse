import colorgram

all_rgbs = []

class ColorExtractor:

    def __init__(self):
        self.all_rgbs = []

    def extract_and_return_rgb(self, color_count):
        """extract colors from picture and return rgb values"""
        # using colorgram extract 6 colors from a picture
        colors = colorgram.extract("hirst.jpg", color_count)

        for color in range(color_count):
            current_color = colors[color]
            rgb = current_color.rgb
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            color = (r, g, b)
            global all_rgbs
            all_rgbs.append(color)
        return all_rgbs
