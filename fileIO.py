#Reading a file
f=open('myfile1.txt','r')
# print(f)
text=f.read()
print(text)
# f.close()

#writing to a file
# f=open('myfile3.txt','w')
# f.write("hello world")
# f.close()


# with open('myfile.txt','a') as f:
#     f.write("hey I am inside with")