#tuples are immutable
tup=(1,2,76,342,32,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
if 342 in tup:
    print("yes")


#methods in tuple
countries=("Spain","India","USA","China")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
countries=tuple(temp)
print(countries)

tuple1=(0,1,2,5,3,2,3,2,4,2,1)
res=tuple1.count(3)
print(res)
