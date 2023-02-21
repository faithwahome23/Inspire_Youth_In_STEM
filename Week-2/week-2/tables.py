#import module
from tabulate import tabulate

#assign data
mydata = [
    ["Nikhi","Delhi"],
    ["Ravi","Kanpur"],
    ["Manish","lisa"],
    ["Prince","Newton"]
]
#create header
head = ["Name","City"]

#display table
print(tabulate(mydata,headers=head,tablefmt="grid"))