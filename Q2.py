# Que. first
w = float(input("Enter the weight(in KG):"))
h = float(input("Enter the height(in Meters):"))
if w<=0 or h<=0:
    print("Invalid input")
else:
    print("The BMI is:", w/(h**2))

# Que. second
W = float(input("Enter the weight(in pounds):"))
H = float(input("Enter the height(in inches):"))
bmi = (W/2.205)/((H/39.37)**2)
if W<=0 or H<=0:
    print("Invalid input")
else:
    print("The BMI is :",bmi)
    