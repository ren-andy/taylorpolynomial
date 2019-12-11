# main.py
# Author: Andy Ren (ren-andy)

import math
import mpmath
import numpy
import matplotlib.pyplot as plotter
import src.poly as p
#import src.taylor_poly as tp


def sin(x):
    """Use numpy.sin when using <polynomial instance>.graph()"""
    return mpmath.sin(x)


def cos(x):
    """Use numpy.cos when using <polynomial instance>.graph()"""
    return mpmath.cos(x)


def numpy_ln_plus_1(x):
    return numpy.log(x+1)


def ln_plus_1(x):
    """Use numpy_ln_plus_1 when using <polynomial instance>.graph()"""
    return ln(x, -1)


def ln(x, a=0):
    """Use numpy.log when using <polynomial instance>.graph()"""
    return mpmath.log(x-a)


def exp(x):
    """Use numpy.exp when using <polynomial instance>.graph()"""
    return mpmath.exp(x)


# Class instance test_poly set to generate a Taylor polynomial of cos to the degree 18 at x=0
def main():
    # Format: test_poly = p.poly(function, center, order/degree)
    test_poly = p.poly(cos, 0, 18)

    # Format: test_poly.graph(function, domain/range)
    # Use numpy.function instead of mpmath!
    test_poly.graph(numpy.cos, 18)


if __name__ == "__main__":
    main()
