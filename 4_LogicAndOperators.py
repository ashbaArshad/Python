#BOOLEAN EXPRESSIONS

#1. VALUES
    #a. True
    #b. False

print(True)
print(False)


#2. FUNCTIONS
    #a. bool()
    #b. any()
    #c. all()
    #d. isinstance()

#a. bool()

    #bool(value)
    #if value is non zero or non empty -> True
    #if value is empty or zero -> False
print(bool(123)) # -> True
print(bool("HI")) # -> True
print(bool()) # -> False
print(bool(0)) # -> False
print(bool("")) # -> False
print(bool(None)) # -> False

#b. any()

    #returns True if atleast one value is True
    #input -> list output -> bool
email = ""
phone = "0378 2713932"
username = ""
    # allows registeration 
    # if any field is filled 
print(any([email,phone,username])) #True

phone = ""
print(any([email,phone,username])) #False

#c. all()

    #returns True if all values are True
    #input -> list output -> bool
email = ""
phone = "0378 2713932"
username = ""
    # allows registeration 
    # if only all fields are filled 
print(all([email,phone,username])) #False

email = "xyz.gmail.com"
username = "xyz"
print(any([email,phone,username])) #True

#d. isinstance()
    
    #checks if a value belongs to a certain data type
    #isinstance(value, datatype) output -> bool
print(isinstance(123,int)) #True
print(isinstance(True,int)) #False
print(isinstance("123",str)) #True


#3. COMPARISON OPERATORS
    #compares two values and returns true or false 
        #based on the result
    #a. == (Equal To)
    #b. != (Not Equal To)
    #c. < (Less Than)
    #d. > (Greater Than)
    #e. <= (Less Than or Equal)
    #f. >= (Greater Than or Equal)

    #syntax -> value operator value  output -> bool
    #value can also e function, variable or expression
print(7 == 7) #True
print(7 != 7) #False
print(7 < 9) #True
print(7 > 9) #False
print(7 <= 0) #False
print(9 >=6) #True

    #strings can be comared too
    #alphabetically
print("a" < "b") #True
    #case sensitive
print("a" == "A") #False

    #CHAINED COMPARISON
        #evaluates from left to right
        # checking each condition one by one
print(6 < 7 < 8) #True
print(9 < 7 < 8) #False

    #like between operator in sql
    #is age between 18 and 30?
age  = 25
print(18 <= age <= 30) #True
age  = 33
print(18 <= age <= 30) #False


#4. LOGICAL OPERATORS
    #a. and
    #b. or
    #c. not

#a. and
     
    # all conditions must be TRUE
print(5 < 7 and  6 == 6) #True
print(8 < 7 and  6 == 6) #False
print(5 < 7 and  6 == 6 and 5 >= 3) #True

    #checkin user credential before login
email = True
password = False
print(email == True and password == True)

#b. or
    #atleast one condition is TRUE
print(5 < 7 or  6 == 6) #True
print(8 < 7 or  6 == 6) #True
print(8 < 7 or  6 != 6) #False
print(5 < 7 or 6 == 6 or 5 >= 3) #True

    #check if the system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

#c. not

    #reverses True <-> False
    #true to false
    #false to true
print ( 3 > 2) #True
print (not 3 > 2) #False
print ( 3 > 4) #False
print (not 3 > 4) #True
print(not not False) #False

    #and operator has higher priority than or operator
    #which means and will b exeuted first

#      2nd      1st
#       |        |
5 == 5 or 8 > 5 and 6 < 4
#         True  and False
#               |
#True  or      False
#       |
#      True

#use paranthesis() to control the order

#      1st        2nd
#       |          |
(5 == 5 or 8 > 5) and 6 < 4
# True  or True      
#        |
#        True     and 6 < 4
#                  | 
#                 False

    #allow access only if the user is logged in
    #or they are guest
    #but they must not be banned
is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest ) and not is_banned) #False
is_banned = False
print((is_logged_in or is_guest ) and not is_banned) #True
is_logged_in = False
print((is_logged_in or is_guest ) and not is_banned) #False


#5. MEMBERSHIP OPERATORS
    #a. in
    #b. not in  

#a. in

    #checks if a value is inside another value
    #like string, list, tuple or sequence
print("o" in "python") #True
print("i" in "python") #False
print(3 in [1,2,3]) #True



#b. not in

    #checks if a value is not inside another value
    #like string, list, tuple or sequence
print("o" not in "python") #False
print("i" not in "python") #True
print(3 not in [1,2,3]) #False

    #security check : ensure the domain is not in banned list
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains) #True

domain = "spam.com"
print(domain not in banned_domains) #False


#6. IDENTITY OPERATORS
    #a. is
    #b. is not

#a. is

    #checks if two variables refer to the same object
    #in memory
    #compares id in memory not actual values

#same values different objects
a = ["a", "b", "c"]
b = ["a", "b", "c"]
print(a == b) #True
print( a is b) # False

#same values
#simple same values will share the same object
a = 5
b = 5
print(a == b) #True
print( a is b) #True

#two variables pointing to the same object
a = ["a", "b", "c"]
b = a
print(a == b) #True
print( a is b) # True

#b. is not

    #checks if two variables do not refer to the same object
    #in memory
    #compares id in memory not actual values

#same values different objects
a = ["a", "b", "c"]
b = ["a", "b", "c"]
print(a == b) #True
print( a is not b) # True

#same values
#simple same values will share the same object
a = 5
b = 5
print(a == b) #True
print( a is not b) #False

#two variables pointing to the same object
a = ["a", "b", "c"]
b = a
print(a == b) #True
print( a is not b) # False

    #make sure the  email exists and it is not empty
email = None
print(email is not None and email != "") #False
    #why ot comparison operators?
    #best practice to use is and is not with None

#CHALLANGES

#1. Check if the username's is not empty and 
# the age is greater than or equal to 18
username = ""
age = 25
print((username is not None and username != "") and age >= 18)
username = "ash"
print((username is not None and username != "") and age >= 18)
username = None
print((username is not None and username != "") and age >= 18)
age = 17
username = "ash"
print((username is not None and username != "") and age >= 18)

#2. Check if the password is atleast 8 characters long 
#does not contain spaces
password = "123 903"
print(len(password) >= 8 and " " not in password)
password = "123903vssd"
print(len(password) >= 8 and " " not in password)
password = "123903"
print(len(password) >= 8 and " " not in password)

#3. Check if a user's email is not empty, contains @
#and ends with .com
email = "xyz@gmail.com"
print((email is not None and email != "") 
      and "@" in email 
      and email.endswith(".com"))


email = ""
print((email is not None and email != "") 
      and "@" in email 
      and email.endswith(".com"))

email = None
print((email is not None and email != "") 
      and "@" in email 
      and email.endswith(".com"))

email = "xyzgmail.com"
print((email is not None and email != "") 
      and "@" in email 
      and email.endswith(".com"))

email = "xyz@gmail.commm"
print((email is not None and email != "") 
      and "@" in email 
      and email.endswith(".com"))


#4. Check if a username is a string, is not none and is longer than 5 characters
username = "ashfdw"
print(isinstance(username, str) 
      and username is not None 
      and len(username) > 5)

username = "ash"
print(isinstance(username, str) 
      and username is not None 
      and len(username) > 5)

username = None
print(isinstance(username, str) 
      and username is not None 
      and len(username) > 5)

username = 123
print(isinstance(username, str) 
      and username is not None 
      and len(username) > 5)

#5. Check if the user is either an admin or moderator
#and either they are not banned or they've verified their email

is_admin = True
is_moderator = False
is_banned = True
is_email_verified = True

print((is_admin or is_moderator) 
      and (not is_banned or is_email_verified))

is_email_verified = False

print((is_admin or is_moderator) 
      and (not is_banned or is_email_verified))






















