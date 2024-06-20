f=open("myfile.txt",'r')

for i in (f.readlines() [-6:]):
    print(i,end="")
    
f.close()