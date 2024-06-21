with open("myfile.txt", 'w') as f: 
    l=["Hello","apple","bananas"]
    f.writelines(l)
f.close()    