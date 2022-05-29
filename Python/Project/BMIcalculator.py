#weight = float(input("Enter your weight:"))
#height = float(input("Enter your height:"))
Enterweight = input("Enter your weight:")
Enterheight = input("Enter your height:")
weight = float(Enterweight)
height = float(Enterheight)
BMI = weight/(height * height)
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("Normal")
elif BMI > 25 and BMI <= 30:
    print("Overweight")
else:
    print("Obesity")

print("Finished")
