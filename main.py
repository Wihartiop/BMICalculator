# install the art from 'Terminal' by typing 'pip install art'
# then import module
from art import *

# Return ASCII text with block font
# If font=None then there is no block
Art = text2art("BMI", font='block', chr_ignore=True)

print(Art)
print('WELCOME TO BMI CALCULATOR  ')

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height_square = height ** 2
bmi = weight / height_square
bmi_final = round(bmi)

if bmi <= 18.5:
    message = "you are underweight"
elif bmi <=25:
    message = "you have a normal weight."
elif bmi <=30:
    message = "you are slightly overweight."
elif bmi <=35:
    message = "you are obese."
else:
    message = "you are clinically obese."
print(f"Your BMI is {bmi_final}, {message}.")