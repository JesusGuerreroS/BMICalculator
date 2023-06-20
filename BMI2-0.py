#############################################
#script to calculate your BMI
#############################################


#get your height and weight
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#doing the calculation of the bmi
bmi = round((weight / (height ** 2)))

#calculate your actual BMI
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")




