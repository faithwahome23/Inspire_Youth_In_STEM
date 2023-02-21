#write a programme that calculates 16% 
#ranging between 100k-150k
#19% tax if income is between 150k-300k
#30% tax income is above 300k
#15% if income is less than 100k
#print grosss icome,net income
income = input("Enter the net income")
#!/usr/bin/env python3
#This is a single line comment
#write a programme that calculates 16% tax on income
#name : Faith Wahome
#Email : wahomewarish@gmail.com
#Date : 17th Feb 2023
#File : bank.py
gross_income = int(input("Enter your income:"))
if(gross_income <= 100000):
    net = gross_income - (gross_income*0.05)
    print(net)
    print(gross_income)
elif((gross_income > 100000) & (gross_income <= 150000)):
    net = gross_income -(gross_income*0.16)
    print(net)
    print(gross_income)
elif((gross_income > 150000) &(gross_income <= 300000)):
    net = gross_income -(gross_income*0.19)
    print(net)
    print(gross_income)
elif(gross_income >300000):
    net = gross_income -(gross_income*0.3)

print(net)
print(gross_income)