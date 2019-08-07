import math

import datagenerator
import logarithmicplot


def main():

    print("----------------------")
    print("| codedrome.com      |")
    print("| Logarithmic Plots  |")
    print("----------------------\n")

    data = datagenerator.generate_data()

    print_data(data)

    logarithmicplot.draw_logarithmic_plot(720, 540, "Logarithmic Plot", data, 6, "logarithmicplot1.svg")


def print_data(data):

    print("----------------------------\n| Label  | Data   | log10  |\n----------------------------")

    for item in data:

        print("| {:6s} | {:6d} | {:6.2f} |".format(item["label"], item["data"], math.log10(item["data"])))

    print("----------------------------")


main()
