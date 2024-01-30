# Method Overloading

'''
Method Overloading:
Unlike some other languages (such as Java or C++), Python does not support method 
overloading in the traditional sense, where multiple methods with the same name 
but different parameter types or numbers are defined within the same class.

However, Python allows a form of method overloading through default parameter 
values and variable-length argument lists. You can create a single method that 
handles different cases based on the number or type of arguments provided.'''


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(2))         # Output: 2
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9
