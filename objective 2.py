# example
'''
print("hello")
name = input("name please: ")
y = int(input("age please: "))
x = float(5.5)
print(x)
'''


# simple adder
'''
x = int(input("enter num1:"))
y = int(input("enter num2:"))
sum_nums = x + y 
print (sum_nums)
'''


# test marks 
'''
mark_1 = int(input("enter first score out of 100: "))
mark_2 = int(input("enter second mark out of 100: "))
mark_3 = int(input("enter third mark out of 100:  "))
avg = (mark_1 + mark_2 + mark_3)/3
print (avg)

'''


# temperature converter challenge
'''
def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * (5/9)
    return celsius

def conversion():
 farenheit = int(input("Enter temperature in farenheit: "))
 celsius = (farenheit_to_celsius(farenheit))
 print(f"{farenheit} degrees Farenheit is equal to {celsius:.2f} degrees Celsius.")

conversion()

'''


# Height and weight challenge
'''

inches_str = input("please insert your height in inches: ")
inches = float(inches_str)
centimetres = inches * 2.54
print(f"There are approximately {centimetres:.2f} cm in {inches:.2f} inches.")

stone_str = input("please enter your weight in stones: ")
stones = float(stone_str)
kilograms = stones * 6.346
print(f"There are approximately {kilograms:.2f} kilograms in {stones} stones.")

'''


# Toy cars challenge
'''
base_pay_str = input("please enter the number of hours you worked today: ")
hours = float(base_pay_str)
hours_pay = hours * 9.0

toys_str = input("please input the number of toys you made today: ")
toys = float(toys_str)
pay_per_toy = float(toys * 0.6)

total_pay_today = hours_pay + pay_per_toy
print(f"You earned £{total_pay_today:.2f} today. ")

'''


# Fish tank volume challenge
'''
length_str = input("enter the length of the tank in cm: ")
length = float(length_str)
depth_str = input("enter the depth of the tank in cm: ")
depth = float(depth_str)
height_str = input("enter the height of the tank in cm: ")
height = float(height_str)
volume_litres = (height * length * depth) / 1000
volume_gallons = volume_litres / 4.546
print(f"The volume of the fish tank is {volume_litres:.2f} litres.")  
print(f"The volume of the fish tank is {volume_gallons:.2f} UK gallons.")

'''


# Circle properties challenge
'''
diameter_str = input("enter the diameter of the circle in centimetres: ")
diameter = float(diameter_str)
radius = diameter / 2
print(f"The radius of the circle is {radius:.2f} cm.")
area = radius * radius * 3.1415926
print(f"The area of the circle is {area:.2f} cm^2")
circumference = diameter * 3.1415926
print(f"The circumference of the circle is {circumference:.2f}cm")
arc_angle_str = input("enter the arc angle of the circle in degrees: ")
arc_angle = float(arc_angle_str)
arc_length = (circumference * arc_angle) / 360
print(f"The arc length is {arc_length} cm.")

'''