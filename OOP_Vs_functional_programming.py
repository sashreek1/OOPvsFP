# Here we will define an object called calculator
# that will contain all our methods required for the basic computation
class Calculator :

    # one major difference between initialising functions to initialising methods is the requirement of the 'self' keyword
    # The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class
    def add (self):
        num1 = int(input("Enter 1st number to calculate : "))
        num2 = int(input("Enter 2nd number to calculate : "))
        print(num1+num2)

    def subtract(self):
        num1 = int(input("Enter 1st number to calculate : "))
        num2 = int(input("Enter 2nd number to calculate : "))
        print(num1-num2)

    def multiply(self):
        num1 = int(input("Enter 1st number to calculate : "))
        num2 = int(input("Enter 2nd number to calculate : "))
        print(num1*num2)

    def divide(self):
        num1 = int(input("Enter 1st number to calculate : "))
        num2 = int(input("Enter 2nd number to calculate : "))
        print(num1/num2)

    def power(self):
        num1 = int(input("Enter 1st number to calculate : "))
        num2 = int(input("Enter 2nd number to calculate : "))
        print(num1**num2)

    def square(self):
        num1 = int(input("Enter 1st number to calculate : "))
        print(num1**2)

    def sqrt(self):
        num1 = int(input("Enter 1st number to calculate : "))
        print(num1**(1/2))

# From here we will now define functions
# to do the exact same thing as the corresponding methods defined above

def add():
    num1 = int(input("Enter 1st number to calculate : "))
    num2 = int(input("Enter 2nd number to calculate : "))
    print(num1 + num2)


def subtract():
    num1 = int(input("Enter 1st number to calculate : "))
    num2 = int(input("Enter 2nd number to calculate : "))
    print(num1 - num2)


def multiply():
    num1 = int(input("Enter 1st number to calculate : "))
    num2 = int(input("Enter 2nd number to calculate : "))
    print(num1 * num2)


def divide():
    num1 = int(input("Enter 1st number to calculate : "))
    num2 = int(input("Enter 2nd number to calculate : "))
    print(num1 / num2)


def power():
    num1 = int(input("Enter 1st number to calculate : "))
    num2 = int(input("Enter 2nd number to calculate : "))
    print(num1 ** num2)


def square():
    num1 = int(input("Enter 1st number to calculate : "))
    print(num1 ** 2)


def sqrt():
    num1 = int(input("Enter 1st number to calculate : "))
    print(num1 ** (1 / 2))


# Here we will define a main function to run an operation using both OOP and Functional programming
def main():

    calc = Calculator()

    function_list = ['',"add()",'subtract()','multiply()','divide()','power()','square()','sqrt()','quit()']
    method_list = ['',"calc.add()",'calc.subtract()','calc.multiply()','calc.divide()','calc.power()','calc.square()','calc.sqrt()','quit()']
    option = input("""Enter an operation : 
1) Add
2) Subtract
3) Multiply
4) Divide
5) Raise to the power
6) square
7) square root
8) quit

""")
    option = int(option)
    print("running command using OOP code : \n")
    eval(method_list[option])
    print("running command using Functional programming code : \n")
    eval(function_list[option])

while True:
    main()