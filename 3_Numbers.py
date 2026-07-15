import math #importing math module
import random #importing random module

#3 types of numerics
    #int -> whole numbers -> 5,-10,100
    #float ->decimal point ->3.15,100.0,-15.7
    #omplex -> real+imaginary -> 2+1j

#Categories

#1. Types And Conversions
    #a. type()
    #b. int()
    #c. float()
    #complex()

x = 5
y = 3.16
z = 2 + 3j

#a. type()
print(type(x))
print(type(y))
print(type(z))

#b. int()
    #converts compatible type into int
x = "23"
print(type(x))
x = int(x)
print(type(x))
x = 3.15
print(int(x))

#c. float()
    #converts compatible type into float
x = 3
print(float(x))

#d. complex()
    #syntax -> complex(real,img) output-> complex
    #creates a complex numer using real and imaginary parts
x = 3
y = 4
print(complex(x,y))

#2. Math Operators
    #a. 3 + 2 (addition)
    #b. 3 - 2 (subtraction)
    #c. 3 * 2 (multiplication)
    #d. 3 / 2 (division)
    #e. 3 // 2 (floor divison -> divides and rounds down)
    #f. 3 % 2 (modulus -> reminder )
    #g. 3 ** 2 (exponentiation -> raises the num to the power of another num)

print(3 + 2) #a.(addition)
print(8 - 5) #b.(subtraction)
print(5 * 3) #c.(multiplication)
print(7 / 2) #d.(division)
print(7 // 2) #e.(floor divison -> divides and rounds down)
print(10 % 5) #f.(modulus -> reminder )
print(2 ** 2) #g.(exponentiation -> raises the num to the power of another num)

    #shortcuts
x = 2
x += 3  #x = x + 3
print(x)

#3. ROUNDING
    #a. abs()
    #b. round()
    #c. ceil()
    #d. floor()
    #e. trunc()

#a. abs()
    #returns the  absolute non-negative value of a number
x = 2 - 10
print(x)
print(abs(x))

#b. round()
    #rounds to the nearest whole number
    #ties like .5 goes to the nearest even number
price = 35.53982384
print(round(price))
    #round(num,ndigits)
    #rounds the number to the specified number of decimal places
print(round(price,2))

#c. ceil()
    #rounds to the ceiling value
    #part of math module so need to import math module at the start
print(math.ceil(price))

#d. floor()
    #rounds to the ceiling value
    #part of math module 
print(math.floor(price))

#e. trunc()
    #cuts of the decimal part and keeps the whole number(no rounding)
    #part of math module 
print(math.trunc(price))
    #same as int()
print(int(price))
    #int() vs trunc()
    #if you are not already using math module then use int()
    #but if you're already using math then use trunc() makes your intent clear

#4. ADVANCED MATH
    #all part of math module
    #a. sqrt()
    #b. sin()
    #c. cos()
    #d. log()

#5. RANDOM
    #from random module
    #a. random()
    #b. randint()

#a. random()
    #returns a random float between 0.0 and 1.0
print(random.random())

#b. randiant()
    #synatx-> randiant(start,end) output->  int
    #returns a random whole number from start to end(both included)
print(random.randint(1,100))
    #used to generate test(dummy) data for age,id,price etc

#6. Validation
    #a. is_integar()
    #b. isinstance()

#a. is_integar()
    #syntax-> x.is_integar() output-> bool 
    #checks if the float has no decimal part(is a whole number)
x = 0.7
print(x.is_integer())
x = 7.0
print(x.is_integer())

#b. isinstance()
    #checks if the belongs to a certain data type
    #syntax-> isinstance(value,type) output-> bool
x = 70
print(isinstance(x,int))
x = 4.1
print(isinstance(x,float))

#Challange 
#genrate a random number from 1 to 100
#and check if it is an even number

x = random.randint(1, 100)
print(f"Number = {x}")
print(f"Even Number : {x % 2 == 0}")