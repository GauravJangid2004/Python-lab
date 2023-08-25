x = int(input("Enter three digit number:"))

n1 = x % 10
a1 = x//10

n2 = a1 % 10
a2 = a1//10

n3 = a2 % 10 

s = n1 + n2 + n3
print("The sum of three digit is:",s)

if s%3==0:
    print("Their sum is also divisible by 3")
else:
    print("Their sum is not divisible by 3")
