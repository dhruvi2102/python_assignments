count = 0
word=input("Enter the word: ")
with open("myfile.txt", 'r') as f: 
	
	for line in f: 
		words = line.split() 
		for i in words: 
			if(i==word): 
				count=count+1
print("Occurrences of the word", word, ":", count)
