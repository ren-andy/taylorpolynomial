# ./src/poly.py
# Author: Andy Ren (ren-andy)

import re
import math
import mpmath
import numpy
import matplotlib.pyplot as plotter
from fractions import Fraction


# Polynomial class
class poly:
    """Class which instantiates a regular or Taylor's polynomial."""

    # Initializes polynomial
    def __init__(self, *varargs):
        """ Initializes polynomial based on parameters passed"""
        self.polynomial = []  # Technically the coefficient array
        self.monomial = []  # Array which includes all monomials
        if len(varargs) == 1:  # Regular polynomial
            self.equation = varargs
            self.degree = 0
            self.center = 0
            self._string_to_coefficients(self.polynomial, *varargs)
        elif len(varargs) == 3:  # Taylor polynomial
            self.function = varargs[0]
            self.center = varargs[1]
            self.degree = varargs[2]
            self.equation = ''
            # Generate taylor polynomial
            self._generate_poly_coefficients(self.function, self.center,
                                             self.degree)

    # If taylor polynomial is needed
    # @classmethod
    # def init_taylor_poly(cls, function_name, center, degree):
    #    return cls(function_name, center, degree)

    # If regular polynomial is needed
    # @classmethod
    # def init_reg_poly(cls, *equation):
    #    return cls(*equation)

    def _string_to_coefficients(self, *varargs):
        """Private method which converts passed strings to coefficient."""
        coefficients = []
        for i in varargs:
            coefficients.append(re.search('[0-9]*', i))
        self.polynomial = varargs

    def _coefficient_to_string(self):
        """Private method which converts coefficient array to readable string."""
        temp_monomial = []
        for i, coefficient in enumerate(self.polynomial):
            if i == 0 and coefficient != 0:  # Special 0th degree term case
                temp_monomial.append(
                    str(Fraction(coefficient).limit_denominator()))
                self.monomial.append(
                    str(Fraction(coefficient).limit_denominator()))
            elif i == 1 and coefficient != 0:  # Presents 1st degree term withou "^1"
                temp_monomial.append(
                    str(Fraction(coefficient).limit_denominator()) +
                    self._adjust_poly_center())
                self.monomial.append(
                    str(Fraction(coefficient).limit_denominator()) +
                    self._adjust_poly_center())
            elif coefficient == 0:  # Removes 0 terms
                self.monomial.append(str(0))
                continue
            else:
                temp_monomial.append(
                    str(Fraction(coefficient).limit_denominator()) +
                    self._adjust_poly_center() + "^" + str(i))
                self.monomial.append(
                    str(Fraction(coefficient).limit_denominator()) +
                    self._adjust_poly_center() + "^" + str(i))
        self.equation = "+".join(temp_monomial)
        self.equation = self.equation.replace(
            "+-", "-")  # Replace any "+- terms due to negative coeff

    def _adjust_poly_center(self):
        """Private method which adjusts poly center if it isn't at x=0."""
        if self.center > 0:
            return "(x-" + str(self.center) + ")"
        elif self.center < 0:
            return "(x+" + str(-self.center) + ")"
        else:
            return "x"

    def _generate_poly_coefficients(self, function, center, degree):
        """Generates coefficients for taylor polynomial based on given degree and center."""
        for i in range(0, degree + 1):
            # Each "i" term contains the function's ith derivative value at x=center,
            # divded by the ith factorial.
            # This is because when taking the ith derivative of the Taylor polynomial-
            # power rule results in additional terms being multiplied into the ith coefficient (i.e 1*2*3*4...*i)
            # (Note: the ith coefficient becomes a constant term)
            # These multiples need to be cancelled out-
            # so that the constant term is the "function"'s actual derivative value, hence dividing by i! factorial.
            self.polynomial.append(
                round(mpmath.diff(function, center, i), 6) / factorial(i))
            #poly_instance = list(mpmath.diffs(mpmath.sin, 0, 5))
            #poly_instance = mpmath.taylor(mpmath.sin, center, 5)
            # print(self.polynomial)

    def _operation(self, operation):
        """Performs operations on polynomial"""
        if (operation == 'derivative'):
            for i, coefficient in enumerate(self.polynomial):
                coefficient *= i
            self.polynomial.pop(0)
        elif (operation == 'integral'):
            C = 8 
            for i, coefficient in enumerate(self.polynomial):
                coefficient *= 1/(i+1)
            self.polynomial.insert(0, +C) # Inserts a dummy +C
        elif (operation == 'add'):
            pass
        elif (operation == 'subtract'):
            pass

    def solve(self, x):
        """Solves the polynomial based on passed x argument."""
        result = 0
        if self.center == 0:
            for i, coefficient in enumerate(self.polynomial):
                result += coefficient * x**i
        else:
            for i, coefficient in enumerate(self.polynomial):
                result += coefficient * (x - self.center)**i
        return result

    def graph(self, function, range):
        """Graphs the Taylor polynomial and compares it with its actual function."""
        vector_function = numpy.vectorize(self.solve)

        x = numpy.linspace(-range, range, 10000)
        y = vector_function(x)  # y = polynomial.solve(x) works too
        f = function(x)

        plotter.grid(True, which='both')
        plotter.axhline(y=0, color='k')
        plotter.axvline(x=0, color='k')

        plotter.plot(x, f, label=function.__name__+"(x)")
        plotter.plot(x, y, label="Degree: " + str(self.degree))
        plotter.ylim([-range, range])
        plotter.legend()
        plotter.show()

    def get_degree(self):
        """ Returns degree of polynomial."""
        return self.degree

    def __str__(self):
        """Returns polynomial as a string"""
        self._coefficient_to_string()
        return self.equation

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        """Usage: <poly_instance>[i]"""
        return self.monomial[index]

    def __len__(self):
        return len(self.polynomial)


def factorial(n):
    """Calculates factorial of numerical argument n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing function
#def main():
    #test = poly(sin, 0, 10)
    #print(str(test))
    # print(test[5])
    # print(test.monomial)
    #print(test.solve(1))
    #test2 = taylor_poly(sin, 0, 100)
    # print(test.solve(10))
    # test2.graph(sin)
