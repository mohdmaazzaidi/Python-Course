# WAP to print a paragraph in python?
# Use REPL and print the table of 5 using it?
# Installl an external module and use it to perform an operation of your interest.
# """ pip install pyttsx3"""
# name = "Muaaz"
# age = 23
# Course = "B.tech"
# isPass = True

# print(name, age, Course, isPass, sep="-") # sep is keyword to seprate values between commas

# print(name, end=" ") # end is also key word to print next print satement in same line
# print(age, end=" " ) 
# print(Course) 
# print(isPass) 


# F-string -------------- This helps to write varables with in the Msg and avoid seprating string by coma.
# print(f"My name is {name} and my age is {age} and I have just completed {Course}")



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# product = 0

# for i in range(num2):
#     product += num1

# print("Product =", product)



# a = 67
# b = 98
# c = 56
# print(a>b<c and b>a<c)
# print(b>a>c or a>b<c)
# print(b<a>c and a>b>c)
# print(a<b>c or c>b>a)


# num = 153
# tem = num 
# sum = 0
# while tem >0 :
#     rem = tem % 10
#     cube = rem **3
#     sum = sum + cube
#     tem = tem //10
# print(sum)    


# num = 5
# a = 0
# b = 1
# sum = 0
# count = 1
# while(count<=num):
#     print(sum)
#     a = b
#     b = sum 
#     sum = a + b
#     count+=1
# print(sum)



# num = 20
# a = 0
# b = 1
# count = 1

# while count <= num:
#     c = a + b
#     a = b
#     b = c
#     count += 1
# print(a)


a = 20
b = 78

gcd = 0

i = 1
while(i<=a):
    if(a%i == 0 and b%i == 0):
        gcd = i
    i+=1
print(gcd)        
































