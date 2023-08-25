x = int(input("Enter the five digit number:"))
n1 = x % 10
a1 = x//10

n2 = a1 % 10
a2 = a1//10

n3 = a2 % 10 
a3 = a2//10

n4 = a3 % 10
a4 = a3//10

n5 = a4 % 10 

p = (n1*10000)+(n2*1000)+(n3*100)+(n4*10)+(n5)
print("Reversed number is:",p)
if p==x:
    print("Number is palindrome")
else:
    print("number is not Palindrome")
    