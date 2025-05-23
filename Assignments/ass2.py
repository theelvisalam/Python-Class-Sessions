# -*- coding: utf-8 -*-
"""ass2_9676

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15IisWAFkOCflr1wkwa27PPRsS19gEfVM

Question 1:
"""

you = int(input("What is your stylish? "))
date = int(input("What is your date stylish? "))

if you <= 2 or date <= 2:
    result = 0
elif you >= 8 or date >= 8:
    result = 2
else:
    result = 1

print("Result:", result)

"""Question 2:"""

weight = float(input("Please type in your weight in lbs: "))
height = float(input("Please type in your height in inches: "))

bmi = (weight / (height ** 2)) * 703

if bmi < 16.0:
    category = "Severely Underweight"
elif 16.0 <= bmi <= 18.4:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
elif 30.0 <= bmi <= 34.9:
    category = "Moderately Obese"
elif 35.0 <= bmi <= 39.9:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"\nYour BMI is: {bmi:.1f}, you are {category.lower()}.")

"""Question 3:"""

year = int(input("Please type in the car Year: "))
mileage = int(input("Please type in the car mileage: "))
color = input("Please type in the car color: ").lower()
model = input("Please type in the car model: ").lower()
price = int(input("Please type in the car price: "))

acceptable_colors = ["white", "black", "grey"]
acceptable_models = ["truck", "suv"]

if year > 2015:
    if mileage < 30000:
        if color in acceptable_colors:
            if model in acceptable_models:
                if 20000 <= price <= 30000:
                    print("\nThis is the car that I am looking for!")
                else:
                    print("\nSorry, this is not the car that I am looking for.")
            else:
                print("\nSorry, this is not the car that I am looking for.")
        else:
            print("\nSorry, this is not the car that I am looking for.")
    else:
        print("\nSorry, this is not the car that I am looking for.")
else:
    print("\nSorry, this is not the car that I am looking for.")