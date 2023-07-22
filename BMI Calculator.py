
#BMI = (weight in Kg)/(Height in Meters)^2

def bmi_calculator(weight,height):
    bmi = weight / (height**2)
    return bmi

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in m: "))
BMI = bmi_calculator(w,h)
print(f"Total BMI is: {BMI}")