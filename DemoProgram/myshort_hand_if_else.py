a=330
b=3303
print("A") if a>b else print("=") if a==b else print("B")

#Enumerate function
marks=[12,56,32,98,12,45,1,4,2]
index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Anu, Awesome")
#     index+=1
for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("anu,awesome")



# import pandas as pd
# print(pd.__version__)

