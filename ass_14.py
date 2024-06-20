'''str="Dhruvi"

if len(str)>2:
    print(str[0:2]+str[4:6])
else:
    print(" ")    '''

name=input("Enter a name: ")

if len(name)>2:
    s1=name[:2] + name[-2:]
    print(s1)
else:
    print(" ")    