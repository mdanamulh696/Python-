# # Lecture 2

# str1 = "This is a string."
# str2 = 'Md Aanamul Haque.'
# str3 = """This is a string an another way."""

# print(str1, "it's lenght:",len(str1))
# print(str2, "it's lenght:",len(str2))
# print(str3, "it's lenght:",len(str3))

# final_str = str1 +" "+ str2 +" "+ str3

# print(final_str)
# print(len(final_str))



# #indexing
# name = "anamul_haque"
# print(name[0])
# print(name[0:3])
# print(name[3:6])



# # String Functions

# # str.endsWith(“ue“)       #returns true if string ends with substr 
# # str.capitalize( )         #capitalizes 1st char
# # str.replace( old, new )   #replaces all occurrences of old with new Apna College 
# # str.find( word )          #returns 1st index of 1st occurrence 
# # str.count(“am“)           #counts the occurrence of substr in string


# str = "anamul_haque"

# print(str.endswith("ue"))
# print(str.capitalize("anamul_haque"))
# print(str.replace("u", "o"))
# print(str.find("u"))
# print(str.count("u"))

# # write a program to iput user name and print its lenght
# name = input("enter your name: ")
# print("your name lenght is:",len(name))

# # write a program to find the occourrence of '$' in a string
# str = "hi, $ i am the $ symbol $99.99"
# print(str.count("$"))

# # Conditional Statements
# # if-elif-else (SYNTAX)
    
# # if(condition):        
# #     Statement1

# # elif(condition):        
# #     Statement2

# # else:        
# #     StatementN

# # Exercise 1
# age = int(input("enter you age:"))
# if(age>=18):
#     print("can vote and apply for license")
# else:
#     print("not allowed")

# # Exercise 2
# light = input("enter the light colour:")
# if(light=="green"):
#     print("can go")
# elif(light=="yellow"):
#     print("wait")
# elif(light=="red"):
#     print("stop")
# else:
#     print("light colour wrong")

# # Exercise 3
# marks = int(input("enter your marks:"))
# if(marks>=90): 
#    grade = "A"
# elif(90>marks>=80): 
#    grade = "B"
# elif(80>marks>=70): 
#    grade = "C"
# elif(marks<70): 
#    grade = "D"
# print("grade of the student ->", grade)

# # write a program to check if a number entered by the user is odd or even.
# num = int(input("enter any number:"))
# if(num%2==0):
#     print("even")
# else: print("odd")

# # write a program to fird the freatest of 3 numbers entered by the user.
# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
# c = int(input("enter 3rd number:"))

# if(a>b and a>c ):
#     print("1st number is largest number")
# elif(b>c):
#     print("2nd number is largest number")
# else: 
#     print("3rd number is largest number")

# # write a program to check if a number entered by the user is multiple of 7 or not.
# num = int(input("enter any number:"))
# if(num%7==0):
#     print("multiple of 7")
# else: 
#     print("not multiple of 7")

