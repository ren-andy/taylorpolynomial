# taylor_poly.py
# may move poly class to its own doc
# remove taylor_poly class? 
# fix graph function 
# clean up main function 

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
        self.polynomial = [] # Technically the coefficient array
        self.monomial = [] # Array which includes all monomials
        if len(varargs) == 1: # Regular polynomial
            self.equation = varargs
            self.degree = 0
            self.center = 0 
            self.polynomial = self._string_to_coefficients(self.polynomial, *varargs)
        elif len(varargs) == 3: # Taylor polynomial 
            self.function_name = varargs[0]
            self.center = varargs[1]
            self.degree = varargs[2]
            self.equation = ''
            # Generate taylor polynomial
            self._generate_poly_coefficients(self.function_name, self.center, self.degree)

    # If taylor polynomial is needed
    #@classmethod 
    #def init_taylor_poly(cls, function_name, center, degree):
    #    return cls(function_name, center, degree)

    # If regular polynomial is needed 
    #@classmethod
    #def init_reg_poly(cls, *equation):
    #    return cls(*equation)
   
    def _string_to_coefficients(self, *varargs):
        """Private method which converts passed strings to coefficient."""
        coefficients = []
        for i in varargs: 
            coefficients.append(re.search('[0-9]*',i))
        return varargs

    def _coefficient_to_string(self):
        """Private method which converts coefficient array to readable string."""
        temp_monomial = []
        for i, coefficient in enumerate(self.polynomial): 
            if i == 0 and coefficient != 0: # Special 0th degree term case 
                temp_monomial.append(str(Fraction(coefficient).limit_denominator()))
                self.monomial.append(str(Fraction(coefficient).limit_denominator()))
            elif i == 1 and coefficient != 0: # Presents 1st degree term withou "^1" 
                temp_monomial.append(str(Fraction(coefficient).limit_denominator()) + self._adjust_poly_center())
                self.monomial.append(str(Fraction(coefficient).limit_denominator()) + self._adjust_poly_center())
            elif coefficient == 0: # Removes 0 terms 
                self.monomial.append(str(0))
                continue
            else:
                temp_monomial.append(str(Fraction(coefficient).limit_denominator()) + self._adjust_poly_center() +"^" + str(i))
                self.monomial.append(str(Fraction(coefficient).limit_denominator()) + self._adjust_poly_center() +"^" + str(i))       
        self.equation = "+".join(temp_monomial)
        self.equation = self.equation.replace("+-", "-") # Replace any +- terms due to negative coeff

    def _adjust_poly_center(self):
        """Private method which adjusts poly center if it isn't at x=0."""
        if self.center > 0:
            return "(x-" + str(self.center) + ")"
        elif self.center < 0: 
            return "(x+" + str(-self.center) + ")"
        else:
            return "x"
    
    def _generate_poly_coefficients(self, function_name, center, degree):
        """Generates coefficients for taylor polynomial based on given degree and center."""
        #print(function_name(1))
        #self.polynomial.append(function_name(self.center))
        for i in range(0, degree+1):  
            #print(i)
            self.polynomial.append(round(mpmath.diff(function_name, center, i), 6)/factorial(i))
            #poly_instance = list(mpmath.diffs(mpmath.sin, 0, 5))
            #poly_instance = mpmath.taylor(mpmath.sin, center, 5)
            #print(self.polynomial)

    # Performs operations on array 
    def _operation(self, function, operation, value):
        if(operation == 'derivative'):
            # slope = f(x+h)-f(x)/h, provided as "h" is infinitely small 
            h = 0.00000000001
            result = (function(value + h) - function(value)) / h
        elif(operation == 'integral'):
            pass
        elif(operation == 'add'):
            pass
        elif(operation == 'subtract'):
            pass
        return result

    def solve(self, x):
        """Solves the polynomial based on passed x argument."""
        result = 0 
        if self.center == 0:
            for i, coefficient in enumerate(self.polynomial):
                result += coefficient * x ** i
        else: 
            for i, coefficient in enumerate(self.polynomial):
                result += coefficient * (x - self.center) ** i   
        return result

    def get_degree(self):
        """ Returns degree of polynomial."""
        return self.degree

    def __str__(self):
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
            return n * factorial(n-1) 


# Taylor polynomial class <might remove> 
class taylor_poly:
    def __init__(self, function_name, center, degree):
        self.poly = poly(function_name, center, degree)

    def solve(self, x):
        """Solves the polynomial based on passed x argument."""
        return self.poly.solve(x)

    def graph(self, function):
        vector_function = numpy.vectorize(self.solve)

        x = numpy.linspace(-2, 2, 1000)
        y3 = vector_function(x) + x**101
        y1= x-x**3+x**5-x**7+x**9-x**11+x**13-x**15+x**17-x**19+x**21-x**23+x**25
        y2= self.solve(x)
        y = numpy.sin(x)

        plotter.plot(x, y, label="sin(x)")
        plotter.plot(x, y1, label= "Degree 26")
        plotter.plot(x, y2, label= "Degree " + str(self.poly.degree))
        plotter.plot(x, y3, label= "Degree 101")
        plotter.ylim([-2, 2])
        plotter.legend()
        plotter.show()

    def radius_of_convergence(self):
        """Returns the radius of convergence of the taylor polynomial."""
        pass


# Test functions <To be removed>    
def sin(x):
    return mpmath.sin(x)

def cos(x):
    return mpmath.cos(x)

def main():
    test = poly(sin, 0, 10)
    print(str(test))
    #print(test[5])
    #print(test.monomial)

    print(test.solve(1))

    #test2 = taylor_poly(sin, 0, 100)

    #print(test.solve(10))
    #test2.graph(sin)

main()



