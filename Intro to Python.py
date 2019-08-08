# -*- coding: utf-8 -*-

print("Hello World")

a = 12;
b = "This is a string"
c = 12.5;

print(a,b,c)

#Mathematical Operation

num1 = 12
num2 = 4

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
result5 = num1 % num2

print(result1)
print(result2)
print(result3)
print(result4)
print(result4)

sen = "I Love Avengers. \n"
print(sen*5)

#Conditional Statements
marks = 90

if marks > 90:
    print("Excellent")
elif marks >80:
    print("Great")
elif marks >70:
    print("Good")
else:
        print("Can be done better")
        
no1 = 45
no2 = 5

if(no1 % no2 == 0):
    print("Divisible")
else:
    print("Not Divisible")
    
#-----------------------------------------------------------
    
#Loops

# While Loop

i = 1

while i<=10:
      print(i)
      i += 1
    
for i in range(1,11):
    print(i)
    
for i in range(1,6):
   for j in range(1,6):
       print(j, end = "")
   print()   
    
   
# Break
   
   for i in range(1,11):
       if i > 5:
           break
       print(i)
   
#Continue
       
   for i in range (1,11):
       if i >= 4 and i<= 7:
           continue
       print(i)

#---------------------------------------------------------------
       
#Python Lists

list1 = [12,12.8,"This is a String"]
print(list1)       

print(list1[0])

#Inserting elements in list
list1.append(50)

list1.insert(0,"String no. 1")

#Updating list
list1[1] = 20

#Delete element from list
list1.pop()

del list1[2]

#Check length of list
print(len(list1))

#Iterate through list
for index in range(0,len(list1)):
    print(list1[index])      
    
for item in list1:
    print (item)
   
#-----------------------------------------------------------------    

#TUPLES

tuple1 = (12,"This is a string",13.8,"Yes")
tuple2 = (50,90.2)

tuple3 = tuple1 + tuple2 

print(len(tuple3)) 

for i in range(0, len(tuple3)):
    print(tuple3[i])
    
for item in tuple3:
    print(item)    

#-------------------------------------------------------------------
    
#DICTIONARIES    

dict1 = {}

#Adding Elements    

dict1['apple'] = "Apple is a fruit"
dict1['orange'] = "Orange is a fruit"
dict1['python'] = "I saw Python"

#Print

print(dict1)
print(dict1['apple'])

print(dict1.get("apple"))
#-----------------------------------------------------------------

# DELETE ELEMENTS

del dict1['apple']

# LENGTH

print(len(dict1))
#----------------------------------------------------------------

ListofKeys = list(dict1.keys())

ListofValues = list(dict1.keys())
 
#---------------------------------------------------------------
# Iterate through whole

for key in dict1.keys();:
    print(dict1[key1])
    
for value in dict1.values():
    print(value)
    
#---------------------------------------------------------------
#Console I/O

inp = input("Enter a number:")
number1 = int(inp)

inp = input("Enter a number:")
number2 = int(inp)

print(number1 + number2)    
#----------------------------------------------------------------
#File I/O

#Writing a File

inp = input("Enter some text:")
with open("textfile.txt","w") as f:
    f.write(inp)
    
#----------------------------------------------------------------

#To append the text

with open("textfile.txt", "a")as f:
    f.write(inp)

#---------------------------------------------------------------

#In Read Mode

with open("textfile.txt", "r") as f:
      print(f.read())

#--------------------------------------------------------------    
 
#FUNCTIONS
      
def  functionName(arg1,arg2):
     print(arg1,arg2)

functionName("This No. is",12)      


#Adds 2 no.s
def sumoftwo(num1,num2):
    return(num1+num2)
    
print(sumoftwo(12,25))

#Length of a number
def length(a):
    count = 0
    for item in a:
        count += 1
    return count
    
    
print(length([12,14,56]))    

#-------------------------------------------------------------

# CLASSES AND OBJECTS

class Fish:
    def swim(self):
        print("Fish is Swimming")
    def eat(self):
        print("Fish is eating")
        
fish = Fish()
fish.swim()
fish.eat()

#------------------------------------------------------------

# OVERRIDE CONSTRUCTOR

class Game:
    def __init__ (self,name):
        self.name = name
    def start(self):
        print(self.name," has started")
    def stop(self): 
        print(self.name," has stopped")

game = Game("Counter Strike")
game.start()
game.stop()       

#-------------------------------------------------------------

# LIST COMPREHENSION

numbers = [1,2,3,4,5,6,7,8,9,10]

# Copy and make New List 
newNumbers = []

for number in numbers:
    newNumbers.append(number)
    

newNumbers = [number for number in numbers]

newNumbers = [number for number in numbers if number <=5] 
    
numbers2 = [1,3,5,7,9]

newNumbers = [number for number in numbers if number not in numbers2]

NewNumbers =[number * 2 for number in numbers]

#------------------------------------------------------------

# GENERATOR COMPREHENSION

squareGen = (number ** 2 for number in numbers)

list(squareGen)

#------------------------------------------------------------

# DICTIONARY COMPREHENSION

myDict = {"apple":1, "orange":4, "banana":10}

newDict = {key: myDict[key] for key in myDict.keys()} 

newDict = {key: myDict[key] for key in myDict.keys() if myDict[key]>5}  

#-----------------------------------------------------------

#JOIN LIST 

words = ["I", "love", "Avengers"]

sentence = ''.join(words)

sentence = '.'.join(words)

#-------------------------------------------------------------
