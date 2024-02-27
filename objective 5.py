'''
#Get User input
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#Make calculations
power_of_result = number1 ** number2
division_result = number1 / number2
integer_division_result = number1 // number2
modulus_result = number1 % number2

#output results
print()
print(number1,"to the power of",number2,"is",power_of_result)
print(number1,"divided by",number2,"is",division_result)
print(number1,"divided by",number2,"is",integer_division_result)
print(number1,"divided by",number2,"has a remainder of",modulus_result)
'''
"""
import random
#roll dice
#random_number = random.randint(1,10)
#print("you rolled a",random_number)
dice = int(input("Choose which dice you want to roll between 4,6 or 12 sides: "))
if dice == 4:
    random_number = random.randint(1,4)  
    print("You rolled a",random_number) 
elif dice == 6:
    random_number = random.randint(1,6)
    print("You rolled a",random_number) 

elif dice == 12:
    random_number = random.randint(1,12)
    print("You rolled a",random_number) 

else:
    print("Error. Please choose between 4,6 or 12.")

"""





# RPG dice challenge 
"""
import random

dice = int(input("Choose which dice you want to roll: "))
random_number = random.randint(1,dice)  
print("You rolled a",random_number) 

"""

# Divisible challenge 
"""
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

if first == 0 or second == 0:
    print("Error: you cannot divide by 0")
else:
    answer = second / first 
    remainder = second % first
    if second % first == 0:
     print(second,"is exactly divisible by",first)
    else:
     print(second,"is not exactly divisible by",first,"so there is a remainder of",remainder)

"""

# Month challenge
"""
month = int(input("Enter the numerical value of the month you wish to choose: "))

if month == 1:
    print("January has 31 days.")
if month == 2:
    leap = input("Is it a leap year? ")
    if leap in ("yes","y"):
        print("February has 29 days.")
    elif leap in ("no","n"):
        February = print("February has 28 days.")
    else:
        print("Please answer yes or no.")
elif month == 3:
    print("March has 31 days.")
elif month == 4:
    print("April has 30 days.")
elif month == 5:
    print("May has 31 days.")
elif month == 6:
    print("June has 30 days.")
elif month == 7:
    print("July has 31 days.")
elif month == 8:
    print("August has 31 days.")
elif month == 9:
    print("September has 30 days.")
elif month == 10:
    print("October has 31 days.")
elif month == 11:
    print("November has 30 days.")
elif month == 12:
    print("December has 31 days.")
else:
    print("Error. Please select a number between 1 and 12.")


"""

# Dice Game Challenge
"""
import random
 
dice_1 = random.randint(1,6)
print("for dice 1 you rolled a",dice_1)

dice_2 = random.randint(1,6)
print("for dice 2 you rolled a",dice_2)

dice_3 = random.randint(1,6)
print("for dice 3 you rolled a",dice_3)

total_5 = dice_1 + dice_2 + dice_3
total_4 = dice_1 + dice_2
total_3 = dice_1 + dice_3
total_2 = dice_3 + dice_2


if dice_1 == dice_2 and dice_1 == dice_3:
    print("score =",total_5)
elif dice_1 == dice_2:
    print("Score =",total_4)
    print("End score =",total_4 - dice_3)
elif dice_1 == dice_3:
    print("Score =",total_3)
    print("End score =",total_3 - dice_2)
elif dice_2 == dice_3:
    print("Score =",total_2)
    print("End score =",total_2 - dice_1)
elif dice_1 != dice_2 != dice_3:
    print("Score = 0")

"""