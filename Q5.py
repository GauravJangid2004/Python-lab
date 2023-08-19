R = float(input("Enter the radius:"))
if R <= 100 and R >=1:
    print("The area of circle is:",(3.141)*R**2)
else:
    print("Invalid Input")
    print("Enter the value in range of 1 to 100")