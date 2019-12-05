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

# Polynomial class
class poly:
    """Class which instantiates a regular or Taylor's polynomial."""
    # Initializes polynomial
    def __init__(self, *varargs):
        """ Initializes polynomial based on parameters passed"""
        self.polynomial = []
        if len(varargs) == 1:
            self.equation = varargs
            self.polynomial = self._string_to_coefficients(self.polynomial, *varargs)
        elif len(varargs) == 3: 
            self.function_name = varargs[0]
            self.center = varargs[1]
            self.degree = varargs[2]
            self.equation = ''
            self.monomial = [] # Array which includes all monomials
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
                temp_monomial.append(str(coefficient))
                self.monomial.append(str(coefficient))
            elif i == 1 and coefficient != 0: # Presents 1st degree term withou "^1" 
                temp_monomial.append(str(coefficient) + "x")
                self.monomial.append(str(coefficient) + "x")
            elif coefficient == 0: # Removes 0 terms 
                self.monomial.append(str(0))
                continue
            else:
                temp_monomial.append(str(coefficient) + "x^" + str(i))
                self.monomial.append(str(coefficient) + "x^" + str(i))       
        self.equation = "+".join(temp_monomial)
        self.equation = self.equation.replace("+-", "-")

    #def _remove_zeroes(self, poly_instance):
    #    poly_instance = filter(lambda i: i != 0, poly_instance)
    #    return poly_instance
    
    def _generate_poly_coefficients(self, function_name, center, degree):
        """Generates coefficients for taylor polynomial based on given degree and center."""
        for i in range(0, degree+1):  
            #print(i)
            self.polynomial.append(round(mpmath.diff(function_name, center, i)))
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
        for i, coefficient in enumerate(self.polynomial):
            result += coefficient * x ** i 
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


# Taylor polynomial class <might remove> 
class taylor_poly:
    def __init__(self, function_name, center, degree):
        self.poly_instance = poly(function_name, center, degree)

    def solve(self, x):
        """Solves the polynomial based on passed x argument."""
        self.poly_instance.solve(x)

    def radius_of_convergence(self):
        """Returns the radius of convergence of the taylor polynomial."""
        pass

def graph_polynomial(poly, function):
    vector_function = numpy.vectorize(poly.solve)

    x = numpy.linspace(-2, 2, 1000)
    y3 = vector_function(x) + x**101
    y1= x-x**3+x**5-x**7+x**9-x**11+x**13-x**15+x**17-x**19+x**21-x**23+x**25
    y2= poly.solve(x)
    y = numpy.sin(x)

    plotter.plot(x, y, label="sin(x)")
    plotter.plot(x, y1, label= "Degree 26")
    plotter.plot(x, y2, label= "Degree " + str(poly.degree))
    plotter.plot(x, y3, label= "Degree 101")
    plotter.ylim([-2, 2])
    plotter.legend()
    plotter.show()
    
def sin(x):
    return mpmath.sin(x)

def cos(x):
    return mpmath.cos(x)

def main():
    test = poly(sin, 0, 100)
    print(str(test))
    print(test[10])

    #print(test.solve(10))
    graph_polynomial(test, sin)

main()



