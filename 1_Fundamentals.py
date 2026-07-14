#This is a comment

#Multiline Comment
#1.hello

#Functions
#3 types
#1. Built In -> print()
#2. Third Party Liraries ->Pandas
#3. User Defined

#Print()
print("Hello World")
print('hello')
print(2345)

#ESCAPE SEQUENCES
#1.\" Escape Double Quote
print("Hello \"Pyton\"")

#2.\' Escape Single Quote
print("Hello \'Python\'")

#3.\\ Escape Backslash
print("Hello \\Python\\")

#4.\n Escape Newline
print("Hello\nPython")

#5.\t Escape Tab ->adds tab space
print("Hello\tPython")

#Challange
#USE PRINT TO CREATE THIS OUTPUT ONLY ALLOWED TO USE ONE PRINT()
"""
Your Learning Path:
    -Python Basics
    -Data Engineering
    -AI
"""
#SOL 1
print("Your Learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

#SOL2
print("""Your Learning Path:
      \t-Python Basics
      \t-Data Engineering
      \t-AI""")

#VARIABLES
#-> a name you create to store a value

print("My name is Ashba")
print("Ashba is learning Python")
print("Ashba wants to become a Python expert")

user = "Ashba"
language = "Python"

print("My name is", user)
print(user, "is learning", language)
print(user, "wants to become a", language, "expert")

user = "Maria"
language = "Javascript"

print("My name is", user)
print(user, "is learning", language)
print(user, "wants to become a", language, "expert")

#CHALLANGE
#PRINT THE FOLLOWING OUTPUT MAKE IT DYNAMIC
"""
info@datawithbaraa.com
support@datawithbaraa.com
www.datawithbaraa.com
"""

#SOLTION
name = "datawithbaraa.com"
print("info@"+name)
print("support@"+name)
print("www."+name)

#INPUT
#-> function to get input from users

name = input("Enter Your Name: ") #dynamic value
country = "Germany" #static value
print("You are", name, "from", country)

#Datatypes
#python automatically detects datatypes
#dynamic datatypes: can change anytime

#3 categories
#no value ->NoneType
#single value ->int, str, bool, float, complex
#multi value -> set, tuple, dict, list

#values are objects of dataclass type

a = 10 #int
b = 3.15 #float
c = "Hello" #str
d = 'Hi' #str
e = "1234" #str
f = True #bool -> case sensitive
g = False #bool
h = None #Nonetype
i = "" #str - blank ->same as none
j = " " #str - emptyspace ->not same as none

#FUNCTIONS VS METHODS

#FUCTIONS -> independent block of code
#syntax ->func_name(value)

#METHODS -> functions belong to objects/classes
#syntax -> value.method_name()

text = "hi"
number = 10

#functions
print(type(text))
print(type(number))

print(len(text))
#print(len(number))

#methods
print(text.upper())
print(number.bit_length())

#CHALLANGE
"""
CREATE FIVE VARIABLES EACH WITH DIFFERENT DATA TYPE
1.YOUR AGE
2.YOUR HEIGHT(WITH DECIMALS)
3.YOUR NAME
4. ARE U A STUDENT
5. SOMETHING WITH NO VALUE

THEN PRINT THE VALUES AND DATATYPES OF ALL VALUES
"""

name = "Ashba"
age = 25
height = 5.1
student = True
more = None

print("NAME :", name, "DATATYPE :", type(name))
print("HEIGHT :",height, "DATATYPE :", type(height))
print("AGE :",age, "LENGTH :", "DATATYPE :", type(age))
print("STUDENT :", student,  "DATATYPE :", type(student))
print("MORE INFO :",more, "DATATYPE :", type(more))