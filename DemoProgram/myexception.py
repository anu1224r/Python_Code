# a=input("enter the number")
# print(f"Multiplication table of {a} is")
# try:
#  for i in range(1,11):
#     print(f"{int(a)}X{i}={int(a)*i}")
# except:
#     print("invalid number")

# print("some imp lines of code")
# print("end of program")

try:
    num=int(input("Enter an integer"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")



#Finally keyword
try:
    l=[1,2,3,4,8,9]
    i=int(input("enter the index"))
    print(l[i])
except:
    print("some error occurred")
finally:
    print("I am always executed")



