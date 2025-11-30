# # Lecture 3

# # List 

# marks = [94.5, 87.4, 78.5, 55, 78, 43]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1])
# print(marks[5])

# # It can store elements of different types (integer, float, string, etc.)
# student = ["Anamul", 95.5, "Duisburg"]
# print(student)
# print(student[0])
# print(len(student))
# student[0] = "Haque" # value change in 0 index
# print(student)

# # String -> immutable( not change able )
# # List -> mutable ( change able )

# # List Slicing
# marks = [10, 20, 30, 40, 50]
# print(marks[0:3])

# # List Methods
# # list = [2, 1, 3]
# # list.append(4)              #adds one element at the end  [2, 1, 3, 4]    
# # list.sort( )                #sorts in ascending order     [1, 2, 3]
# # list.sort( reverse=True )   #sorts in descending order    [3, 2, 1]
# # list.reverse( )             #reverses list                [3, 1, 2]
# # list.insert( idx, el )      #insert element at index 



# marks = [ 20, 10,30, 40, 50]

# marks.append(60)            # add 60 in the end
# print(marks)

# marks.sort()                #sorts in ascending order  
# print(marks)

# marks.sort(reverse=True)    #sorts in descending order
# print(marks)

# marks.reverse()             #reverses list  
# print(marks)

# marks.insert(6, 70)         #insert element at index 6
# print(marks)

# # Tuple -> immutable( not change able )

# tuple = (2, 1, 3, 1)

# print(tuple)
# print(type(tuple))
# print(tuple[0])
# print(tuple[1])

# tuple1 = (1,)       # without (,) type show int 
# print(tuple1)
# print(type(tuple1))

# # write a program to ask the user to enter names of their 3 favorite movies & store them in a list

# a = input("enter the first favorite movie name: ")
# b = input("enter the 2nd favorite movie name: ")
# c = input("enter the 3rd favorite movie name: ")
# F_M_list=[a, b, c]
# print(F_M_list)

# # write a program to check if a list contain a palindrome(shoro or las theke porle ekoi lagbe) of clements ( hints use copy() method )

# list1 = [1,2,3,2,1]
# list2 = [1,2,3,4,5]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# copy_list2 = list2
# copy_list2.reverse()


# if(copy_list1 == list1):
#     print("List1 Palindrome")
# elif(copy_list2 == list2):
#     print("List2 Palindrome")
# else:
#     print("Not Palimdrome")

# # write a program to count the number of students with the "A" grade in the following tuple.

# grade = ["C", "D", "A", "A", "B", "B", "A" ]
# grade.count("A")
# print(grade.count("A"))

# grade.sort()
# print(grade)