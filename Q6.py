n=int(input("Enter the number:"))
temp=n
s=0
i=0
m=0
while temp!=0 :
    digit=n%10
    s=digit*(10**i)
    i=i+1
    m+=s
    temp//=10
if n==m:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
    