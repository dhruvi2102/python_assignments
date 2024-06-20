#swap num with & without temp variable

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

c=a
a=b
b=c

print("a=",a)
print("b=",b)

#WITHOUT TEMP VARIABLE

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

print("a & b are ",b,a)
