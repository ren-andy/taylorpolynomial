import re 

# Polynomial class
class poly:
    def __init__(self, *varargs):
        self.polynomial = []
        for i in varargs:  
            self.polynomial.append(i)

    # Private string to coefficient conversion method
    def _string_to_coefficient(self, *varargs):
        coefficients = []
        for i in varargs: 
            coefficients.append(re.search('[0-9]*',i))
        pass
        return

    # Private coefficient to string conversion method
    def _coefficient_to_string(self, *varargs):
        pass  
    
    # Performs operations on array 
    def operation(self, operation=None, *numbers):
        #derivative??? 
        pass  
        return

    #print function 
    def __print__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        return len(self.polynomial)

    #print function 


# initializes taylor polynomial based on given function
class taylor_poly:
    def __init__(self, function_name, degree):
        pass

def main():
    test = poly(1, 2, 3)
    print(len(test))


main()



