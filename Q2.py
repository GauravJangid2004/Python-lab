x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
n=int(input("enter the divisibility number:")) 
i=x+1
while (i>x and i<=y):
    if i%n==0:
        print(i)
    i=i+1
    