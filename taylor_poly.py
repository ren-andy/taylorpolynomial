import re 
import math
import scipy
import scipy.misc
import mpmath


# Polynomial class
class poly:
    # Initializes polynomial
    def __init__(self, *varargs):
        """ Initializes polynomial based on parameters passed, see @classmethods."""
        self.polynomial = []
        if(len(varargs) == 1):
            self.polynomial = self._string_to_coefficients(self.polynomial, *varargs)
        else: 
            self.function_name = varargs[0]
            self.center = varargs[1]
            self.degree = varargs[2]
            self.polynomial = self._generate_poly_coefficients(self.polynomial, self.function_name, self.center, self.degree)

    # If taylor polynomial is needed
    #@classmethod 
    #def init_taylor_poly(cls, function_name, center, degree):
    #    return cls(function_name, center, degree)

    # If regular polynomial is needed 
    #@classmethod
    #def init_reg_poly(cls, *equation):
    #    return cls(*equation)
   
    # Private string to coefficient conversion method
    def _string_to_coefficients(self, *varargs):
        coefficients = []
        for i in varargs: 
            coefficients.append(re.search('[0-9]*',i))
        return varargs

    # Private coefficient to string conversion method
    def _coefficient_to_string(self, poly_instance):
        equation = ''
        monomial = []
        for i, coefficient in enumerate(poly_instance): 
            if i == 0 and coefficient !=0:
                monomial.append(str(coefficient))
            elif i == 1 and coefficient != 0:
                monomial.append(str(coefficient) + "x")
            elif coefficient == 0:
                continue
            else:
                monomial.append(str(coefficient) + "x^" + str(i))       
        equation = "+".join(monomial)
        return equation

    def _remove_zeroes(self, poly_instance):
        poly_instance = filter(lambda i: i != 0, poly_instance)
        return poly_instance
    
    # generates coefficients based on degree 
    def _generate_poly_coefficients(self, poly_instance, function_name, center, degree):
            #poly_instance.append(0)
            temp = 3
            for i in range(0, degree+1):  
                print(i)
                #poly_instance.append(round(scipy.misc.derivative(function_name, center, dx=1e-6, n=i, order = temp)))
                poly_instance.append(round(mpmath.diff(mpmath.cos, center, i)))
                #poly_instance = list(mpmath.diffs(mpmath.sin, 0, 5))
                #poly_instance = mpmath.taylor(mpmath.sin, center, 5)
                temp = temp+4
                print (poly_instance)
            return poly_instance

    # Performs operations on array 
    def _operation(self, function, operation, value):
        if(operation == 'derivative'):
            # slope = f(x+h)-f(x)/h, provided as "h" is infinitely small 
            h = 0.00000000001
            result = (function(value + h) - function(value)) / h
        elif(operation == 'integral'):
            pass
        return result

    # Solves the polynomial based on an x value
    def solve(self, poly_instance, x):
        result = 0 
        return result

    # Radius of convergence
    def radius_of_convergence(self):
        pass

    def __str__(self):
        #return str(self.polynomial)
        return self._coefficient_to_string(self.polynomial)

    def __repr__(self):
        #return self.polynomial
        return str(self)
        
    def __getitem__(self, index):
        return self.polynomial[index]

    def __len__(self):
        return len(self.polynomial)

    #print function 


# Taylor polynomial class
class taylor_poly:
    def __init__(self, function_name, center, degree):
        self.poly_instance = poly(function_name, center, degree)
        self.poly_instance.polynomial = self.poly_instance._generate_poly_coefficients(self.poly_instance.polynomial, function_name, center, degree)

def sin(x):
    return math.sin(x)

def main():
    test = poly(sin, 0, 10)
    print(str(test))

main()



