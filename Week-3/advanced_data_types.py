#Advanced data types

#Mutable vs immutable

#Mutable are data types that can change/edited during programm life cycle
#Add/remove elements
#immutable -->Data types that cannot be edited during programm life cycle


#1 list(mutable)


friends = ["lisa","Fay","Queen","Mark"]
#or friends = [] for empty list
# add/append/extend
students = ["Mary","Kigen","Serphin"]
friends.extend(students)
friends.append("James")
friends.sort()
friends.reverse()
#remove -->pop/delete
#2 tuples(immutable)
#Type of lists that are immutable
stationaries = ("pens","ruler","ink","sharpener",)
#can replace the whole tuple
stationaries("clipboard","eraser","pencils")
for stationary in stationaries:
print(stationary)
numbers = (1,2,3,4,5)

#Dictionaries aka dict
#uses key and value pair
student = {"Name" : "Faith","age""" : 18, "gender" : "female"}
print(student["age"])
print(student["gender"])
#"name" : "Faith" -->name(key) Faith (value)
#4