n=int(input("Enter the number:"))
temp=n
s=0
while temp!=0 :
    digit=n%10
    s+=digit
    temp//=10
print("Sum is:",s)
    
             