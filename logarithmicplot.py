import math

import svg


def draw_logarithmic_plot(width, height, title, data, maxpower, filename):

    """
    Create a logarithmic plot as an SVG file from the data and other values supplied as arguments.
    Save SVG file to specified filename.
    """

    topmargin = 64
    bottommargin = 32
    leftmargin = 86
    rightmargin = 32

    graph_height = height - topmargin - bottommargin
    graph_width = width - leftmargin - rightmargin
    pixels_per_unit_x = graph_width / (len(data) - 1)
    pixels_per_unit_y = graph_height / maxpower

    s = svg.SVG()

    s.create(width, height)

    s.fill("#FFFFFF")

    # header text and border lines
    s.text(width/2, 38, "sans-serif", 16, "#000000", "#000000", "middle", title)
    s.line("#808080", 2, leftmargin, topmargin, leftmargin, height - bottommargin)
    s.line("#808080", 2, leftmargin, height - bottommargin, width - rightmargin, height - bottommargin)

    # y axis indexes and values
    y = height - bottommargin

    for power in range(0, maxpower + 1):

         s.line("#808080", 1, leftmargin - 8, y, leftmargin, y)
         s.text(leftmargin - 12, y + 4, "sans-serif", 10, "#000000", "#000000", "end", str(10 ** power))
         y -= pixels_per_unit_y

    # x axis indexes and values
    x = leftmargin

    for item in data:

         s.line("#808080", 1, x, height - bottommargin, x, height - bottommargin + 8)
         s.text(x, height - bottommargin + 24, "sans-serif", 10, "#000000", "#000000", "middle", str(item["label"]))

         y = height - bottommargin - (math.log10(item["data"]) * pixels_per_unit_y)
         s.circle("#0000FF", 0, "#0000FF", 3, x, y)

         x += pixels_per_unit_x

    # finish off
    s.finalize()

    s.save(filename)

    print("File saved")
