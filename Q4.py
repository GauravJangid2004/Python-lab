n=int(input("enter the number N :"))
s=0
c=0
v=0
t=0
while t!=-999:
    t=int(input())
    if t%n==0:
        c=c+1
    else:
        v=v+1
    s=c+v
print("sum of all no. till now:",s+999)
print("number divisible by n:",c)
print("number not divisible by n:",v)