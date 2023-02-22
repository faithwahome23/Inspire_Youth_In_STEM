#!/usr/bin/env python3
#This is a single line comment
#using for loop draw a triangle
#name : Faith Wahome
#Email : wahomewarish@gmail.com
#Date : 21st Feb 2023
#File : assignment2.py
h = eval(input("Enter diamond's height:"))
for x in range (h):
    print(""*(h-x),"*"*(2*x + 1))
for x in range(h-2,-1,-1):
    print(""*(h-x),"*" * (2*x + 1))
#Drawing a triangle using python
start = 1 
for i in range(5):
    for j in range(i + 1):
        print(start, end=" ")
        start +=1
    print("")
#Drawing a pascals triangle 
num = int(input("Enter the number:"))
list1 = [] #an empty list
for i in range(num):
    list1.append([])
    list1[i].append(1)
    for j in range(1,i):
        list1[i].append(list1[i-1][j-1] + list1[i-1][j])
        if(num != 0):
            list1[i].append(1)
    for i in range(num):
        print(" " *(num-i),end = "",sep = " ")
    for j in range(0,i + 1):
        print('{4:6}'.format(list1[i][j]), end = " ",sep = " ")
    print()
