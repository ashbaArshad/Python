#1. TYPES (conversion)
    #a. type()
    #b. str()
name = "Ashba"
print(type(name))

age = 25
print(type(age))
print("Your age is " + str(age))

age = age + 5
age = str(age)
print(type(age))

#2. MATH
    #a. len()
    #b. count()

#a. len
password = "2kdsfsvsfu"
if len(password) < 8:
    print("Your password is too short") 

#b. count() -> var.count(substring)
    #-> counts how many times the substring appears and it is case sensitive
text = """
 Python is easy to learn.
 Python is powerful.
 Many people love python.
"""

print(text.count("Python"))

#3. TRANSFORMATIONS
    #a. replace()
    #b. 'H'+'i'
    #c. f{} f-string
    #d. split()
    #e. 'ha'*2 string repitation
    #f. Extraction-> indexing and slicing
        #cat[0]
        #cat[1:3]

#a. replace() -> replace(old,new)
    #usecase-> clean numeric formats
price = "1234,5"
print(price.replace(",","."))

phone = "123/456/89"
print(phone.replace("/","-"))

    #can also be used to remove unwanted parts by replacing it with empty string
    #usecase -> clean phone numbers
phone = "123/456/89"
print(phone.replace("/",""))

    #usecase -> clean numeric formats 
price = "$1,299.99"
print(price.replace("$","").replace(",","")) #chained method

    #CHALLANGE
#CONVERT THE MESSY PHONE NUMBER INTO A CLEAN NUMBER FORMAT WITH ONLY DIGITS
#+49 (176) 123-4567 -> 00491761234567
phone = "+49 (176) 123-4567"
print(
    phone.replace("+","00").
    replace("(", "").
    replace(")","").
    replace("-","").
    replace(" ",""))

#b. + ->string + string 
    #-> joins two strings

first_name = "Maria"
last_name = "Scotts"
print(first_name + " " + last_name)

    #usecase ->  build file paths
folder = "C:/Users/Baraa"
file = "report.csv"
print(folder + "/" + file)

#c. f-string f{}
    #-> f stands for formatted, to format and build strings 
    #lets u easily put variables and expressions directly inside string value

name = "Ashba"
age = 25
isStudent = True
    #without f-string
print("My name is " + name + ", I am " + str(age) + ", and student status is " + str(isStudent) + ".")
    #with f-string
print(f"My name is {name}, I am {age}, and student status is {isStudent}.")
    #can also add expressions
print(f"2 + 3 = {2+3}")
    #print curly brackets
print(f"{{this is me}}")

#d. split()
    #break a string value into smaller pieces
    #syntax -> split(separator) output -> list of strings

stamp = "2026-09-20 14:30"
print(stamp.split(" "))

stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))

#e. 'ha'*2 string repitation
    #-> repeat specific value multiple times
    #synatx ->'string' * number output-> string
print("ha" * 3)
    #usecase -> style your logs
print("=" * 50)

#f. indexing and slicing
    # h  e  l  l  o
    # 0  1  2  3  4 ->positive index
    #-5 -4 -3 -2 -1 ->negative index
    #slicing [start:end] ->start included , end not included
    #[0:3] -> hel 
    #[-5:-2] -> hel
    #open ended slicing 
    #[1: ] -> ello
    #[start:end:step(optional)]
    #[0:4:2] -> [0]h[2]l ->skip every second character
    #by default [0:4:1] -> does not any character
    #syntax -> 'string'[index]

#indexin
text = "python"
    #extract the first character
print(text[0])
print(text[-6])
    #extract the last character
print(text[5])
print(text[-1])
    #extract h
print(text[3])
print(text[-3])

#slicing
date = "2026-05-12"
    #extract the year
print(date[0:4])
print(date[:4]) #open ended slicing
    #extract the month
print(date[5:7])
    #extract the day
print(date[8:])
print(date[-2:]) 
    #use positive indexes when u need to extra something from the start
    #use negative indexes when u need to extra something from the end

#4. CLEANING
    #clean white spaces
        #a. lstrip()
        #b. rstrip()
        #c. strip()
    #clean cases -> Case Conversion
        #d. lower()
        #e. upper()

#cleaning spaces
#a. lstrip()
    #removes spaces from left side
text = " engineering".lstrip()
print(text)

#b. rstrip()
    #removes spaces from right side
text = "engineering ".rstrip()
print(text)

#c. strip()
    #removes spaces from both sides
text = " engineering ".strip()
print(text)
    #only removes spaces at the start or end not in the middle
    #can also remove any character not just spaces
text = "###engineering###".strip("#")
print(text)
    #usecase-> detect extra spaces by calculating length
text = "  ENGINEERING"
print(len(text))
print(len(text.strip()))
print(len(text) - len(text.strip()))
print(len(text) == len(text.strip()))

#Case Conversion
    #use case -> standardize data
text = "python PROGRAMMING"
#d. lower()
    #converts the whole string to lower case
print(text.lower())
#e. upper()
    #converts the whole string to upper case
print(text.upper())
    #usecase-> clean data for matching
search = "EMAIL"
data = "email"
print(search.lower() == data.lower())
    #bestcase clean before searching

search = "EMAIL".lower().strip()
data = " emAil".lower().strip()
print(search == data)

#5. SEARCH
    #a. startswith()
    #b. endswith()
    #c. find()
    #d. 'a'in'cat'

#a. startswith()
    #check if the string begins with specific word
    #syntax -> startswith("substring") ->output: bool
    # check country code is Pakistan
phone = "+92 123 432798"
print(phone.startswith("+92")) 

#b. endswith()
    #check if the string ends with specific word
    #syntax -> endswith("substring") ->output: bool
    # check if the email domain is gmail
email = "xyz@gmail.com"
print(email.endswith("gmail.com"))
    #check the extension of file
file = 'data.csv'
print(file.endswith(".csv"))

#d. 'a'in'cat'
    #check if a word exists in the string
    #syntax-> 'substring'in'string output : bool
    #validate email look for @
email = "xyzgmail.com"
print("@" in email)
    #check if the url is an api endpoint
url = "https://api.company.com/v1/data"
print("/api" in url)

#c. find()
    #find is great when combined with other methods to add dynamics
    #returns the starting position of a word in  string
    #syntax-> find(substring) output-> number(index)

    #extract only phone number without country code
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-234-16784"


print(phone1[4:]) 
print(phone2[3:]) #hardcoding does'nt always work

#by searching the first - in number 
print(phone1.find("-"))
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

#6. Validation
    #a. isalpha()
    #b. isnumeric()

#a. isalpha()
    #checks if the string has only letters 
    #output -> bool

    #check if the country name contains only letters
country = "USA1r"
print(country.isalpha())

#b. isnumeric()
    #checks if the string has only numbers 
    #output -> bool

    #check if the phone number is clean
phone = "00233454324"
print(phone.isnumeric())