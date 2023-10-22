import re

pattern="was"
text='''Anumeha is a good girl, she is hardworking, she was brilliant student'''
match=re.search(pattern,text)
print(match)