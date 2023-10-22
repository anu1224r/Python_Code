dic={
    "ANU":"Human Being",
    "Spon":"Object"
}
print(dic["ANU"])



dict={
    344:"Neha",
    56:"anu",
    12:"Ansh"
}
print(dict[56])


info={'name':'Karan','age':12,'Eligible':True}
print(info)
print(info.keys())

for key in info.keys():
    print(info[key])




print(info.items())
for key, value in info.items():
    print(f"The value corresponding is {key} is {value}")




#Methods
#1-Update method
ep1={122:45,122:89,567:69,678:69}

ep2={222:67,566:98}
ep1.update(ep2)
print(ep1)

#Clear method
#ep1.clear()
ep1.pop(122)
ep1.popitem() #last value gets deleted
#delete one dictionary- del ep1