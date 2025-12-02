# # Dictionary in Python
# info ={
#     "ID" : 1035596,
#     "Name" : "Md Anamul Haque",
#     "Subject" :["python", "numpay", "panda"],
#     "Topic" : ("Dictionary", "Set"),
#     "Age" : 30,
#     "Marks" : 94.5
# }
# print(info)
# print(info["Subject"])
# print(info["Topic"])

# info["Name"] = "Sadia Haque"
# print(info)
# info["Subject"] = "pytorch"
# print(info)


# # nested dictionary
# student = {
#     "name" : "sadia akter",
#     "subject" : {
#         "phy":  97,
#         "chem": 98,
#         "math": 95

#     }
# }


# print(student)
# print(student["subject"])             # specific key value print
# print(student["subject"]["chem"])     # specific value print

# # Dictionary Methods

# # myDict.keys( )              #returns all keys 
# # myDict.values( )            #returns all values 
# # myDict.items( )             #returns all (key, val) pairs as tuples
# # myDict.get( “key““ )        #returns the key according to value 
# # myDict.update({newDict} )    #inserts the specified items to the dictionary

# print(student.keys())                 
# print(list(student.keys()))           # type cast
# print(student.values())
# print(student.items())                 
# print(student["name"])
# print(student.get("name"))              # no error -> none

# student.update ({"city":"duisburg"})
# student["subject"]["biology"] = 90      # add new value in nested dictionary
# print(student)

# # Set in python
# # unordered , unique(ignor duplicate value) & element immutable(unchanged)

# collection = {"hello", 1, 7, 3, 4, "hi", "hi", 5, 5}
# print(collection)
# collection1 = set() #empty set; syntax
# print(collection1)

# # Set Methods

# # set.add( el )         #adds an element 
# # set.remove( el )      #removes the elem an
# # set.clear( )          #empties the set 
# # set.pop( )            #removes a random value 

# collection1.add(9)
# collection1.add(8)
# collection1.add(7)
# print(collection1)

# collection.remove(2)
# print(collection)

# collection.clear()
# print(collection)

# collection.update('6')
# print(collection)

# collection.discard("hi")
# print(collection)

# print(collection.union(collection1))

# print(collection.intersection(collection1))

# # Let‘s Practice

# # Store following word meanings in a python dictionary : 

# # table : “a piece of furniture”, “list of facts & figures”
# # cat : “a small animal”

# dictionary = {
#     "table" : ["a piece of furniture","list of facts & figures" ],
#     "cat" : "a small animal"
# }
# print(dictionary)

# # You are given a list of subjects for students. Assume one classroom is required for 1 subject.
# # How many classrooms are needed by all students.

# # ”python”, “java”, “C++”, “python”, 
# # “javascript”,“java”, “python”, “java”, “C++”, “C”

# subjects = {
#     "python", "java", "c++", "python", 
#     "javascript","java","python", "java", "c++", "c"
    
# }

# print(subjects)
# print(len(subjects))

# # WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# # Start withan empty dictionary & add one by one. 
# # Use subject name as key & marks as value.

# marks = {}

# x= int(input("enter phy: "))
# marks.update({"phy" : x})

# x= int(input("enter math: "))
# marks.update({"math" : x})

# x= int(input("enter chem: "))
# marks.update({"chem" : x})

# print(marks)

 