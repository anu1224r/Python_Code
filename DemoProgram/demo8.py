#format strings 
letter="Hello my name is {1} and I  am from {0}"
country="India"
name="Rahul"
#print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

# doctstring
def square(n):
    '''takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#Zen of python
import this


#recursion in python
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(4))
