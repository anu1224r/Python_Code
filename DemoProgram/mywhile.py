i=0
while(i<3):
    print(i)
    i=i+1
count=5
while(count>0):
    print(count)
    count=count-1




#function
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a=9
b=8
isGreater(a,b)
calculateGmean(a,b)
c=8
d=7
isGreater(c,d)
calculateGmean(c,d)


#Function arguments
# def average(a,b):
#     print("The average",(a+b)/2)
# average(4,6)

# def average(a=9,b=1):
#     print("The average",(a+b)/2)
# average(1,6)
# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Average is:",sum/len(numbers))
# average(5,6)

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(2,4,1,6,7)
print(c)


