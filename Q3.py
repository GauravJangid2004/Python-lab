a = float(input("Enter the first side:"))
b = float(input("Enter the second side:"))
c = float(input("Enter the third side:"))
if a<=0 or b<=0 or c<=0:
    print("Invalid input")
elif a+b>c and b+c>a and a+c>b:
    print("These sides form a triangle")
else:
    print("These sides does not form triangle")