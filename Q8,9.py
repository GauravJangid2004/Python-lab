basic_salary = int(input("Enter its basic salary:"))
HRA = (basic_salary * 20)/100
TA = (basic_salary * 5)/100
DA = (basic_salary * 10)/100
G_S = basic_salary + HRA + TA + DA
print("The gross salary is:", G_S)

if G_S < 300000:
    print("Employee give 0% income tax")
elif 300000 <= G_S < 1000000:
    print("Employee give 10% income tax")
elif 1000000 <= G_S <2500000:
    print("Employee give 20% income tax")
else:
    print("Employee give 30% income tax")