l1=["Dhruvi","hi","r","w","Mokshit","hh","hehh","naman"]
count=0
for i in l1:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
        print(i)
print(count)        