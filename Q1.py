x = float(input("Enter the first side:"))
y = float(input("Enter the second side:"))
h = float(input("Enter the height:"))
if x<=0 or y<=0 or h<=0:
    print("Invalid input")
else:
    area = (1/2)*h*(x+y)
    print("Area of trapazium is:",area)
