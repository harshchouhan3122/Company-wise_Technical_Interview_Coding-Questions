#  Example to show Method Overriding

'''
Method Overriding:
Method overriding occurs when a subclass provides a specific implementation for a method 
that is already defined in its superclass. The overridden method in the subclass has the 
same name, return type, and parameters as the method in the superclass. When an object 
of the subclass calls the overridden method, the subclass's implementation is executed 
instead of the superclass's.'''

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Example usage
animal = Animal()
animal.sound()  # Output: Generic animal sound

dog = Dog()
dog.sound()  # Output: Bark
