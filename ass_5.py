#Fibonacci series 

f1=0
f2=1
next_number=f1
count=1
n=int(input("Enter a number: "))

while count <= n:
	print(next_number, end=" ")
	count += 1
	f1, f2 =f2, next_number
	next_number = f1 + f2
print()
