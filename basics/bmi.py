#Print the Body mass index (BMI) based on these values

massInKg = 81.2
heightInM = 1.78

bmi = massInKg // (heightInM ** 2)

if bmi > 25:
    print("BMI = " + str(bmi) + " kg/m^(2) (Overweight)")
elif 18.5 <= bmi <= 25:
    print("BMI = " + str(bmi) + " kg/m^(2) (Normal)")
else:
    print("BMI = " + str(bmi) + " kg/m^(2) (Underweight)")



