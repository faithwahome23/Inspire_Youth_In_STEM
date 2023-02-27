def factorial(n):
    for i in range(0,n):
        fact_n = n * (n - i)
        return fact_n



print(factorial(3))
#write a programme to calculate simple interest 

def simple_interest():
    interest = (p * r * t)/100
    print(interest)
simple_interest(2000000,10,2)