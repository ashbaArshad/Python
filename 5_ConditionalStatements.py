#CONDITIONAL STATEMENTS
    #checkpoint that checks a condition
        #True -> runs the code
        #False -> skip it

#1. if statement

    # defines the  first condition 
    # if true -> do this
    # otherwise do nothing
    
    # Rules
        # only one if
        # starts with if
        # required if you are using conditional statements  
        # can standalone


    # Indentation
        # adding spaces at the beginning of a line to show
        # that the line belongs to a code block
        # use 4 spaces -> PEP8 STYLE GUIDE

score = 100
if score >= 90:
    print("A")
    print("GOOD JOB!")        

 
#2. Else Statement

    # runs only if all previous conditions are false

    #RULES
        # comes at the end
        # no conditions
        # optional
        # cannot standalone
        # only one else

score = 50
if score >= 90:
    print("A")
    print("GOOD JOB!")  
else:
    print("F")


#3. elif statement

    # asks a follow up question
    # only runs if previous conditions were false

    # RULES
        # comes after if
        # can use multiple elif
        # needs condition
        # optional
        # cannot standalone       

score = 85
if score >= 90:
    print("A")
    print("GOOD JOB!")  
elif score >= 80:
    print("B")
else:
    print("F")

    #BRANCHING ELIF
score = 67
if score >= 90:
    print("A")
    print("GOOD JOB!")  
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


#4. NESTED IF

    #if statement inside another if
    #if the first is true then check the second

score = 95
submitted_project = False
if score >= 90:
    if submitted_project:
        print("A+")
        print("GOOD JOB!")  
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#CONNECTING CONDITIONS
score = 55
submitted_project = True
if score >= 90 and submitted_project:
    print("A+")
    print("GOOD JOB!")  
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")


#5. INDEPENDENT IFS

    # each if is checked separately
    #all conditions are tested even if one is already true
score = 95
submitted_project = True

if score >= 90:
    print("High  Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is sumbitted")
else:
    print("Project is not sumbitted")


#6. TERNARY INLINE IF

    # quick and short
    # (do this) if condition else (do this)
    #must include else
    #cannot be used with elif
    #only for simple logic



score = 60
print("A") if score >= 90 else print("F")

grade = "A" if score >= 90 else "F"
print(grade)

score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

    #simple logic -> inline if
    #complex logic -> classical if


#7. MATCH CASE

    # evaluate a value against multiple values
    # runs the code of the first match
    # similar to switch statement in c++
    # easy to read and write 
    # can be used only for matching values
    #only works with python 3.10+
    #for flexible and complex logic use classical if elif
    #boolean or logical operators can not be used
    #to match multiple values in a case we can use pipe "|"

    # convert the full country names into
    # 2 letter abbreviations
country = "USA"
match country:
    case "United States" | "USA":
        print("US")   
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country")

#CHALLANGE

#1.Validate the quality and correctness of email values
#   -must not be empty
#   -must contain "." and "@"
#   -must contain exactly one "@" symbol
#   -must end with .com, .org or .net
#   -must not be longer than 254 characters
#   -must start and end with a letter or digit

email = "xyz@gmail.com"

email = email.strip(); #cleaning white spaces
#must not be empty
if email == "":
    print("Email cannot be empty")
#must contain . and @
elif "." not in email and "@" not in email:
    print("Email must contain . and @")
#must contain only one @
elif email.count("@") != 1:
    print("Email must contain exactly one @")
#must end with .com, .org or .net
elif not email.endswith((".com", ".org", ".net")):
    print("Email must end with .com, .org or .net")
#must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
#must start and end with a letter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email Is Valid!")

  #do you want to stop if a condition fails?
    #use if elif
  #do you want to check all conditions before stopping
    #use independent ifs   

#2. Validate the quality and correctness of password values
#   -must not be empty
#   -must be atleast 8 characters
#   -must include atleast one uppercase
#   -must include atleast one lowercase
#   -must not be the same as email
#   -must not contain any spaces
#   -must start and end with a letter or digit

password = "saccsajA"
valid = True


#must not be empty
if password == "":
    valid = False
    print("Password must not be empty")

#must be atleast 8 characters long
if len(password) < 8:
    valid = False
    print("Password must be atleast 8 characters long")

#must include atleast one uppercase
if not any(ch.isupper() for ch in password):
    valid = False
    print("Password must contain atleast one uppercase letter")

#must include atleast one lowercase
if not any(ch.islower() for ch in password):
    valid = False
    print("Password must contain atleast one lower letter")

#must not be the same as email
if password == email:
    valid = False
    print("Password must not be the same as email")

#must not contain any spaces
if password != password.strip():
    valid = False
    print("Password must not contain any spaces")

#must start and end with a letter or digit
if not (password[0].isalnum() and password[-1].isalnum()):
    valid = False
    print("Password must start and end with a letter or digit")

if valid == True:
    print("Password is valid!!")
