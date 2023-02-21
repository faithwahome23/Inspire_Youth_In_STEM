names =["Faith","lisa","Jane","Lenny","June"]
#Accessing items in a list
print(names)
print(names[0])
print(names[2])
fruits = ["banana","apple","guava","melon","kiwi","orange"]
print(fruits[0:-1])
#print("my favourite fruit is", fruits[2])
print(fruits)
#Adding two lists
vegatables = ["kales","cabbage","spinach","managu","tomato"]
stationary = ["pens","ink","paper","glue","scissors"]
shoppings = vegatables + stationary
print(shoppings)
for vegetable in vegatables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("my name is " + names[0]+ " and my favourite fruit is",fruits[3])

