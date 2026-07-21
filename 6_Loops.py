#LOOP
    #control the flow of code
    #repeat a block of code over and over until a 
    #condition is met

#1. FOR LOOP

    #go through a group of items one by one 
    #to do something for each item

#for loop variale in sequence->ierator:
for  i in (1,2,3,4,5):
    print(f"ROUND : {i}")

    #rule:
        #use the same word
            #variable -> singular
            #sequence -> plural

items = (1,2,3,4,5) #sequence
for item in items:
    print(f"ROUND : {item}")

    #sequences you can loop
        #tuple -> (1,2,3,4,5)
        #list -> [1,2,3,4,5]
        #string -> "analytics"
        #range -> 
            # range(stop) range(5)
            #range(start,end) range(1,5)
                #by default start is 0  
                #start is included end is not included
            #range(start, end, step)
                #by default step is 1
                #step 2 increments of 2
                #range(0,10,2) -> 0,2,4,6,8
        #any object that is iterable can be used
            #like dict, file etc

#tuple
items = (1,2,3,4,5) 
for item in items:
    print(f"ROUND : {item}")
#list
items = [1,2,3,4,5,"hi"]
for item in items:
    print(f"ROUND : {item}")
#string
string = "python" 
for ch in string:
    print(f"ROUND : {ch}")
#range
    #range(stop)
for i in range(20):
    print(f"ROUND : {i}")

    #range(start,stop)
for i in range(1,6):
    print(f"ROUND : {i}")
        #range(start,stop,step)
for i in range(1,15,2): #odd numbers from 1 to 15
    print(f"ROUND : {i}")

#real world applications

    #we use for loops to o through values and aggregate
    #data like summing, counting averaging etc
scores = [80,50,60,75]
total = 0
for score in scores:
    total += score
    print("Current Total : ", total)
print("Final Total : ", total)

    #we use for loops to transform data like cleaning 
    # data before processing
files = [" report.csv" , "DATA.csv ", " final.txt"]
for file in files:
    #remove white spaces, convert to lowercase and only 
    # allow .csv files
    file = file.strip().lower().replace(".txt",".csv")
    print(f"Processing {file}")

    #order -> clean first transform second 

#Challange 
    #Print table of 7 from 1 to 10 uing for loop
    for i in range(1,11):
        print(f"7 x {i} = {i*7}")
    
    #Print a left-aligned pyramid of stars with 6 rows 
    # using for loop
    #*
    #**
    #***
    #****
    #*****
    #****** 
for i in range(1,7):
    print("*" * i)

#ADVANCED FOR LOOPS
    #1. Break Statement
    #2. Continue Statement
    #3. Pass Statement
    
#1. Break Statement
    #stops the loop immediately
    #jumps out and ends the loop right away
    #for critical risk ->cost, security integrity

names = ["john", "maria", "", "ashley"] 
for name in names:
    if name == "":
        print("Empty value detected!!")
        break
    print(f"Name = {name}")

#2. Continue Statement
    #skips one loop cycle without stopping the loop
    #skip this one and go next
    #for medium risk -> bad rows, empty files/data, skip 
    # special caseslk

for name in names:
    if name == "":
        print("Empty value detected!!")
        continue
    print(f"Name = {name}")

#3. Pass Statement
    #a placeholder where nothing happens
    #for now just keep going do nothing
    #to plan for a future
for name in names:
    if name == "":
        pass #todo : handle empty values
    print(f"Name = {name}")

#Real world applications break vs continue

#Task 
    #skip weekends in calendar loop
days = ['Mon', 'Sun', 'Wed', 'Tue']
    #avoid hardcoding values inside for or if
    # instead define them as variables 
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f"Workday : {day}")

#Task
    #scan emails to block unsafe data from entering your
    #system
emails = [
    'data@gmail.com',
    'ash@outlook.com',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL Injection : Hacker Attack')
        break #high risk
    print(f"Processing Email : {email}")

#Else in loop
    #runs a block of code only if the loop finishes naturally
    #loop completed without breaks
items = [1,3,4,7]
for item in items:
    print(item)
else:
    print("Loop completed!!")
    #here else is useless
    #the else runs no matter what so why not just write it 
    # after loop

    #use else with loops only when there's a break

#ELSE + BREAK
    #check for even numbers
items = [1,3,9,7]
for item in items:
    if item % 2 == 0:
        print("Even number found : ", item )
        break
    #else will run only if the loop is not interuppted
else:
    print("All numbers are odd!!")

#For-Else Usecases:
    #search and validate

#search and validate
    #check for missing names
names = ['Kamar', 'Ashley', None, 'Edward']
for name in names:
    if name is None:
        print("Found a missing name!")
        break
else:
    print("No missing names found!")

    #check if all files are csv
files = [
    'data1.csv',
    'employees.pdf',
    'report2.csv'
]
for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not csv")
        break
else: 
    print('All files are csv')

#CHALLANGE
    #check if any filename appears more than once
    #print "duplicate found" if a duplicate exists
    #otherwise print "all files are unique"

files = [
    'data.xlsx',
    'report.csv',
    'summary.docx',
    'report.csv',
    'data.csv'
]

for i in range(0, len(files)):
    if files[i] in files[i+1:]:
        print("Duplicate Found !!")
        print(f"{files[i]} is dupliate")
        break
else:
    print("No Duplicates Found")


#NESTED LOOP
    #loop inside another loop

for x in range(3):  #outer loop
    for y in range(2): #inner loop
        print(f"({x} , {y})")

for x in range(3):  #outer loop
    for y in range(2): #inner loop
        for z in range(2):
            print(f"({x} , {y}, {z})")

#NESTED LOOP USE CASES
    #Crossing / combining data
    #Navigate hierarchy 

    #Crossing / combining data
    #all possible combinations
colors = ['Red' , 'Blue', 'Green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")

    #Navigate hierarchy 
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


    #navigate through tables and columns
    #select count(*) from customers where id is null
tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for table in tables:
    for column in columns:
        print(f"SELECT count(*) FROM {table} where {column} is NULL")

#WHILE LOOP

    #for : iteratin over a sequence for i in range
    #while  iterating over a condition while condition is true
    #risk : unknown times

    #categories of while
        #1. while condition
        #2. while true (break)

#1. while condition
    #exits normally condition == false
    #safer + more readeable
    #counter , limited retries

count = 1 #initialization
while count <= 5: #condition
    print(count)
    count += 1 #update/increment

    #write a program that keeps asking 'Do you agree?'
    #unil the user types 'yes'
answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no) : ")
print("Thank You")


#2. while true (condition)
    #must have extra if+break
    #risk of infinite loop + more flexible
    #open-ended/waiting -> database, api, stream

#infinite loop 
#while(True):
#   print("I AM UNSTOPPALE")
while(True):
    answer = input("Do you agree?(yes/no) : ")
    if (answer == 'yes'):
        break
print("Thank You")

#FOR VS WHILE LOOP
#FOR 
    #loop over a fixed sequence
    #predefined condition
    #no of iterations is known
    #procssing data
    #simple, clear, safe
    #limited

#WHILE
    #loop while a condition is true
    #your condition
    #no of iterations is unknown
    #waiting for an external event
    #advanced, flexible
    #complex, risk

#CHALLANGE
    #write a program that keeps asking 'Do you agree?'
    #unil the user types 'yes'
    #BUT
        #allow upto 3 attempts
        #if user types 'yes' then print "Glad we are on the same page"
        #otherwise print "3 Strikes, You are out"
attempts = 0
while attempts < 3:
    answer = input("Do you agree?(yes/no) : ")
    if (answer == 'yes'):
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 Strikes, You are out")
       
