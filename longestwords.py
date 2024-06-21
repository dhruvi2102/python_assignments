inputFile = "myfile.txt"

# Opening the given file in read-only mode.
with open(inputFile, 'r') as filedata:


  wordsList = filedata.read().split()


  longestWordLength = len(max(wordsList, key=len))

  for textword in wordsList:
     if len(textword) == longestWordLength:
        result=textword

print("The following are the longest words from a text file:")
print(result)

filedata.close()