with open('myfile.txt','r') as myfile1, open('myfile2.txt','w') as myfile2: 
	
	for line in myfile1: 
			
			myfile2.write(line)
