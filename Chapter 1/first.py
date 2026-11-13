# ab = 10
# ba = 20
# sum = ab + ba
# print(sum)

# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# print("Printing Jokes")   ----> Singal line comment 
"""Hello!
this is my first class 
----> Multi line comments ---->
""" 

# firstName = "Tony"
# lastName = "Stark"
# print("Tony's age is 53")
# print("Tony's height is 1.85m")

# name = input("Enter you super name : ")
# print("Tony is secretly a",name)

# numbers = range(5)
# print(range(5))

# for i in range(1,51):
#     if(i == 15):
#         continue
#     if(i%3 == 0):
#         print(i)


# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# for i in range(2,1001):
#     if( a% i == 0 and b%i == 0):
#         print(i)
#         break


#LIST --------------------------------------------------------------

#Printing list
# marks = [23,44,34,45,56]
# print(marks)

#printing list type  #using --- type()
# marks = [23,44,34,45,56]
# print(type(marks))   

#printing length   #using --- len()
# marks = [23,44,34,45,56]
# print(len(marks))  

#Accessing list element using index
# marks = [23,44,34,45,56]
# print(marks[0])  #It will print first element of the list 23
# print(marks[1])  # 44
# print(marks[2])  # 34
# print(marks[-1]) #It will print last element of the list 56
# print(marks[-2]) #It will print second last element of the list 45

#SLICING A LIST  (use to extract a small part of the list)
# marks = [23,44,34,45,56]
# print(marks[0:3])  #it take fist and last index and last index is excluded
# print(marks[:2])  #starting index is by default is 0


# LOOP ON LIST
# marks = [23,44,34,45,56]
# for i in marks:
#     print(i)


#LISTS ARE MUTEABLE
# marks = [23,44,34,45,56]
# marks.append(50)  #use append function to add the new value in the end of the list.
# print(marks)


#LIST INSERT FUNCTION
# marks = [23,44,34,45,56]
# marks.insert(2,14)        #insert function takes two values index and value 
# print(marks)

#LIST VALUE CHECKING USING in KEYWORD
# marks = [23,44,34,45,56]
# print(100 in marks)


#CLEARING LIST VALUE USING .clear() method
# marks = [23,44,34,45,56]
# marks.clear()
# print(marks, len(marks))


#FINDING LAST INDEX IN LIST
# marks = [23,44,34,45,56]
# ab = len(marks)
# marks.insert(len(marks),67)
# print(marks)

# Tuple ------------------------------------------------------------
# Tuple are immutable

# marks = (23,44,34,45,56) # we use () to create a tuple
# print(type(marks))


# marks = (23,44,34,45,56) 
# print(marks[2])   #Accessing element in tuple using index

#Counting Occurence of number in tupple using .count(number)
# marks = (23,44,34,45,56,44,44,44) 
# print(marks.count(44))


#Printing index of a number present in tupple using .index()
# marks = (23,44,34,45,56,44,44,44) 
# print(marks.index(44))

#Dictionary ---------------------------------------------------------------

# ab = {"Maths":97,"Science": 98,"English":95}

# print(ab, type(ab))
# ab["Maths"] = 91    #Changing value is possible
# ab[""]
# print(ab["Maths"])

# for a in ab:
#     print(a,ab[a])


# Q&A ---------------------------------------------------------------------------------------------------------
# Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll nums in the list.

# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# Example - [
# (101, "Alice", 50000),
# (102, "Bob", 65000),
# (103, "Charlie", 45000)
# ]
# Ask user to enter Employee ID & search it inside records.
# 
# 

# employees = [
#  (101, "Alice", 50000),
#  (102, "Bob", 65000),
#  (103, "Charlie", 45000)
# ]
# search_id = int(input("Enter Employee ID: "))
# found = False
# for employee in employees:
#  employee_id = employee[0]
#  if employee_id == search_id:
#      print("Employee found!")
#      print("Employee ID:", employee[0])
#      print("Employee Name:", employee[1])
#      print("Salary:", employee[2])
#      found = True
#      break
# if found == False:
#  print("Employee not found.")    


# Functions in python
# def sum(a,b):  # define function 
#     print("sum of both num is: ",a+b)

# sum(23,7)  # function call


# def calGst(price):
#     newPrice = price + (price * 0.18)
#     return newPrice

# print(calGst(1500))


# Module functions in python---------------------

# import math
# print(dir(math))

# from math import sqrt,log2
# print(sqrt(289))
# print(log2(32))

# import random

# print(random.random())  # it will genrate values from range 0 to 1
# print(random.randint(1,10)) # it take 2 argument and it will genrate values from range 1 to 10

# QA ----------------------------------

#1 WAF TO CHECK IF A NUMBER IS EVEN OR ODD
# def evenOdd(num):
#     if(num%2 == 0):
#         print("Even num")
#     else:
#         print("odd num")   
         
# evenOdd(39)

#2 WAF TO COUNT THE NUMBER OF VOWELS IN A STRING
# a = "WAF FHaa bbb ee"
# def vowelsCount(ab):
#     count = 0
#     for i in ab.lower():
#         if(i in "aeiou"):   
#                count+=1
#     return count           

# print(vowelsCount(a))


#WAF TO PRINT IF A NUMBER IS PRIME OR NOT.
# def isPrime(num):
#      primeNum = True
#      for i in range(2,num-1):
#           if num%i == 0:
#                primeNum = False
#                break
#      if primeNum == True:
#           print("Prime No.")   
#      else: 
#           print("Not a Prime No.")
                 
# isPrime(58)


# WAF TO RETURN THE AVERAGE MARKS IF A LIST OF MARKS IS PASSES AS PARAMETER

# def avgMarks(lst):
#     ab = len(lst)
#     sum = 0
#     for i in lst:
#         sum = i + sum
#     return sum/ab


# a = [1,2,3,4,5]
# print(avgMarks(a))


# guessing number game --------------------------------------------
# import random
# print("*****Lets play the Guessing number game******")
# luckyNum = random.randint(1,50)
# UsernNum = int(input("Enter the guess number in range 1 to 50: "))
# count = 1
# while count < 5:
#         if(luckyNum == UsernNum):
#             print("You won! game over!")
#             break
#         elif luckyNum > UsernNum:
#             print("You entered Low Number")
#             print("Guess Again")
#             UsernNum = int(input("Enter the guess number in range 1 to 50: "))
#             count+=1 
#         else:
#             print("You entered higher Number")
#             print("Guess Again") 
#             UsernNum = int(input("Enter the guess number in range 1 to 50: "))  
#             count+=1     

# if count == 5 and luckyNum != UsernNum:
#     print("You lost all 5 chances")
#     print("Lucky number was:", luckyNum)









