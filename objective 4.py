#Example
'''
# Using selection statements to check variables
# Ask user for the number
number = int(input("Enter a number 1-3: "))
# check value of the number
if number == 1: print("Number one")
if number == 2: print("Number two")
if number == 3: print("Number three")


'''


# works out pass or fail
'''
score = int(input("Enter score: "))
if score > 50:
    print("Congratulations. You passed.")
else:
    print("Sorry, you failed.")

'''

# returns whether two numbers are the same
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 != num2:
    print("The numbers are not the same.")
else:
    print("The numbers are the same")
# '!=' means does not equal

'''

# Using logic operators
'''
choice = input("Enter a number 1-3: ")
if choice > "0" and choice < "3":
    print("Valid input")
else:
    print("Invalid input")


'''


# Using case selection
'''
# Ask user for number
print("1. Add numbers")
print("2. Subtract numbers")
print("3. Quit")

choice = input("Enter your choice: ")
#Multiple branches depending on selection
if choice == "1":
    print("Add nhmbers chosen")
elif choice == "2":
    print("Subtract numbers chosen")
elif choice == "3":
    print("Quitting program")

'''


# Under age challenge
'''
age = int(input("Enter your age: "))
if age < 18:
    print("Under 18")
elif age == 18:
    print("You are exactly 18 years of age.")
else:
    print("Over 18")


'''


# Water temperature challenge
'''
temperature = int(input("Enter the temperature of water in °C: "))

if temperature <= 0:
    print("The water is frozen")
elif temperature >= 100:
    print("The water is boiling")
else: 
    print("The water is still in liquid state")


'''


# Vocational Grade challenge
'''
Test_Mark = int(input("Enter your test mark out of 100: "))
if Test_Mark < 40:
    print("FAIL")
elif 40 <= Test_Mark < 60:
    print("PASS")
elif 60 <= Test_Mark < 80:
    print("MERIT")
elif Test_Mark >= 80:
    print("DISTINCTION")


'''


# Extended visual dice challenge
'''
Number = int(input("Enter the number you wish to display on the dice: "))
one = """
ooooooooo
o       o
o   #   o
o       o
ooooooooo
"""
two = """
oooooooooo
o #      o
o        o
o      # o
oooooooooo
"""
three = """
ooooooooooo
o #       o
o    #    o
o       # o
ooooooooooo
"""
four = """
oooooooooooo
o #      # o
o          o 
o #      # o
oooooooooooo
"""
five = """
ooooooooooooo
o  #     #  o
o     #     o
o  #     #  o
ooooooooooooo
"""
six = """
oooooooooooooo
o  #      #  o
o  #      #  o
o  #      #  o
oooooooooooooo
"""

if Number == 1:
    print(one)
elif Number == 2:
    print(two)
elif Number == 3:
    print(three)
elif Number == 4:
    print(four)
elif Number == 5:
    print(five)
elif Number == 6:
    print(six)
else:
    print("Error. Please select a number from 1-6.")
           
 """   


# Greatest Number challenge

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

if number1 == number2:
    print("Both numbers are equal.")
elif number1 > number2:
    print("The largest number is", number1)
else:
    print("The largest number is", number2)


'''


# Nitrate challenge
"""
nitrate_lvl = int(input("Enter nitrate level (1-50): "))

if nitrate_lvl > 10:
     print("Dose 3ml")
elif nitrate_lvl > 2.5:
     print("Dose 2ml")
elif nitrate_lvl > 1:
     print("Dose 1ml")
else:
     print("Dose 0.5ml")



if nitrate_lvl > 50:
     print("Error. Choose a number between 1 and 50.")


"""

# Portfolio Grade Challenge
"""
analysis = int(input("Enter your grade for analysis: "))
design = int(input("Enter the score for design: "))
implementation = int(input("Enter the score for implementation: "))
evaluation = int(input("Enter the score for evaluation: "))
grade_n = (analysis + design + implementation + evaluation) / 4

if 0<= grade_n <= 3:
     grade = "U"
     next_grade_marks = 4 - grade_n
elif 4 <= grade_n <= 12:
     grade = "G"
     next_grade_marks = 13 - grade_n
elif 13 <= grade_n <= 21:
     grade = "F"
     next_grade_marks = 22 - grade_n
elif 22 <= grade_n <= 30:
     grade = "E"
     next_grade_marks = 31 - grade_n
elif 31 <= grade_n <= 40:
     grade = "D"
     next_grade_marks = 41 - grade_n
elif 41 <= grade_n <= 53:
     grade = "C"
     next_grade_marks = 54 - grade_n
elif 54 <= grade_n <= 66:
     grade = "B"
     next_grade_marks = 67 - grade_n
elif 67 <= grade_n <= 80:
     grade = "A"
     next_grade_marks = 81 - grade_n
else:
     grade = "A*"

next_grade = str(next_grade_marks)

print ("Your grade is " + grade)
print("You are " + next_grade + " marks away from the next grade.")

"""


# Cash Machine challenge
"""
balance = 1200
withdraw = int(input("Enter the withdrawal amount: "))
new_balance = balance - withdraw

if withdraw % 10 != 0:
    print("Error. You can only withdraw in notes of 10 and 20 pounds.")
elif withdraw > 250: 
    print("error. Can only print upto 250 pounds.")
elif balance < withdraw:
    print("Error. You do not have enough money in your account.")
else:
    new_balance = balance - withdraw
    print("Your balance is £" + str(balance))
    print("Withdrawal amount: £" + str(withdraw))
    print("Your new balance is £" + str(new_balance))
"""


# Periodic table challenge
"""
elements_info = {
  'H': {'name': 'Hydrogen', 'mass_number': 1, 'group': 'Nonmetal'},
  'Li': {'name': 'Lithium', 'mass_number': 6.9, 'group': 'Alkali metals'},
  'Na': {'name': 'Sodium', 'mass_number': 23, 'group': 'Alkali metals'},
  'K': {'name': 'Potassium', 'mass_number': 39, 'group': 'Alkali metals'},
  'Rb': {'name': 'Rubidium', 'mass_number': 85, 'group': 'Alkali metals'},
  'Cs': {'name': 'Cesium', 'mass_number': 133, 'group': 'Alkali metals'},
  'Fr': {'name': 'Francium', 'mass_number': 223, 'group': 'Alkali metals'},
  'Be': {'name': 'Beryllium', 'mass_number': 9, 'group': 'Alkaline Earth Metal'},
  'Mg': {'name': 'Magnesium', 'mass_number': 24, 'group': 'Alkaline Earth Metal'},
  'Ca': {'name': 'Calcium', 'mass_number': 40, 'group': 'Alkaline Earth Metal'},
  'Sr': {'name': 'Strontium', 'mass_number': 88, 'group': 'Alkaline Earth Metal'},
  'Ba': {'name': 'Barium', 'mass_number': 137, 'group': 'Alkaline Earth Metal'},
  'Ra': {'name': 'Radium', 'mass_number': 226, 'group': 'Alkaline Earth Metal'},
  'Sc': {'name': 'Scandium', 'mass_number': 45, 'group': 'Transition Metal'},
  'Y': {'name': 'Yttrium', 'mass_number': 89, 'group': 'Transition Metal'},
  '__': {'name': 'Lanthanide', 'mass_number': 57-71, 'group': 'Lanthanide'},
  '_': {'name': 'Actinide', 'mass_number': 89-103, 'group': 'Actinide'},
  'Ti': {'name': 'Titanium', 'mass_number': 48, 'group': 'Transition Metal'},
  'Zr': {'name': 'Zirconium', 'mass_number': 91, 'group': 'Transition Metal'},
  'Hf': {'name': 'Hafnium', 'mass_number': 178, 'group': 'Transition Metal'},
  'Rf': {'name': 'Rutherfordium', 'mass_number': [261], 'group': 'Transition Metal'},
  'V': {'name': 'Vanadium', 'mass_number': 51, 'group': 'Transition Metal'},
  'Nb': {'name': 'Niobium', 'mass_number': 93, 'group': 'Transition Metal'},
  'Ta': {'name': 'Tantalum', 'mass_number': 181, 'group': 'Transition Metal'},
  'Db': {'name': 'Dubnium', 'mass_number': [262], 'group': 'Transition Metal'},
  'Cr': {'name': 'Chromium', 'mass_number': 52, 'group': 'Transition Metal'},
  'Mo': {'name': 'Molybdenum', 'mass_number': 96, 'group': 'Transition Metal'},
  'W': {'name': 'Tungsten', 'mass_number': 184, 'group': 'Transition Metal'},
  'Sg': {'name': 'Seaborgium', 'mass_number': [266], 'group': 'Transition Metal'},
  'Mn': {'name': 'Manganese', 'mass_number': 55, 'group': 'Transition Metal'},
  'Tc': {'name': 'Technetium', 'mass_number': 99, 'group': 'Transition Metal'},
  'Re': {'name': 'Rhenium', 'mass_number': 186, 'group': 'Transition Metal'},
  'Bh': {'name': 'Bohrium', 'mass_number': [264], 'group': 'Transition Metal'},
  'Fe': {'name': 'Iron', 'mass_number': 56, 'group': 'Transition Metal'},
  'Ru': {'name': 'Ruthenium', 'mass_number': 101, 'group': 'Transition Metal'},
  'Os' : {'name': 'Osmium', 'mass_number': 190, 'group': 'Transition Metal'},
  'Hs' : {'name': 'Hassium', 'mass_number': [269], 'group': 'Transition Metal'},
  'Co' : {'name': 'Cobalt', 'mass_number': 58.9, 'group': 'Transition Metal'},
  'Rh' : {'name': 'Rhodium', 'mass_number': 103, 'group': 'Transition Metal'},
  'Ir' : {'name': 'Iridium', 'mass_number': 192, 'group': 'Transition Metal'},
  'Mt' : {'name': 'Meitnerium', 'mass_number': [278], 'group': 'Transition Metal'},
  'Ni' : {'name': 'Nickel', 'mass_number': 58.7, 'group': 'Transition Metal'},
  'Pd' : {'name': 'Palladium', 'mass_number': 106, 'group': 'Transition Metal'},
  'Pt' : {'name': 'Platinum', 'mass_number': 195, 'group': 'Transition Metal'},
  'Ds' : {'name': 'Darmstadtium', 'mass_number': [281], 'group': 'Transition Metal'},
  'Cu' : {'name': 'Copper', 'mass_number': 64, 'group': 'Transition Metal'},
  'Ag' : {'name': 'Silver', 'mass_number': 108, 'group': 'Transition Metal'},
  'Au' : {'name': 'Gold', 'mass_number': 197, 'group': 'Transition Metal'},
  'Rg' : {'name': 'Roentgenium', 'mass_number': [280], 'group': 'Transition Metal'},
  'Zn' : {'name': 'Zinc', 'mass_number': 65, 'group': 'Transition Metal'},
  'Cd' : {'name': 'Cadmium', 'mass_number': 112, 'group': 'Transition Metal'},
  'Hg' : {'name': 'Mercury', 'mass_number': 201, 'group': 'Transition Metal'},
  'Cn' : {'name': 'Copernicium', 'mass_number': [285], 'group': 'Transition Metal'},
  'B' : {'name': 'Boron', 'mass_number': 11, 'group': 'Metalloid'},
  'Al' : {'name': 'Aluminum', 'mass_number': 27, 'group': 'Post-Transition Metal'},
  'Ga' : {'name': 'Gallium', 'mass_number': 70, 'group': 'Post-Transition Metal'},
  'In' : {'name': 'Indium', 'mass_number': 115, 'group': 'Post-Transition Metal'},
  'Tl' : {'name': 'Thallium', 'mass_number': 204, 'group': 'Post-Transition Metal'},
  'Nh' : {'name': 'Nihonium', 'mass_number': [286], 'group': 'Post-Transition Metal'},
  'C' : {'name': 'Carbon', 'mass_number': 12, 'group': 'Nonmetal'},
  'Si' : {'name': 'Silicon', 'mass_number': 32, 'group': 'Metalloid'},
  'Ge' : {'name': 'Germanium', 'mass_number': 73, 'group': 'Metalloid'},
  'Sn' : {'name': 'Tin', 'mass_number': 118, 'group': 'Post-Transition Metal'},
  'Pb' : {'name': 'Lead', 'mass_number': 207, 'group': 'Post-Transition Metal'},
  'Fl' : {'name': 'Flerovium', 'mass_number': [289], 'group': 'Post-Transition Metal'},
  'N' : {'name': 'Nitrogen', 'mass_number': 14, 'group': 'Nonmetal'},
  'P' : {'name': 'Phosphorus', 'mass_number': 31, 'group': 'Nonmetal'},
  'As' : {'name': 'Arsenic', 'mass_number': 75, 'group': 'Metalloid'},
  'Sb' : {'name': 'Antimony', 'mass_number': 122, 'group': 'Metalloid'},
  'Bi' : {'name': 'Bismuth', 'mass_number': 209, 'group': 'Post-Transition Metal'},
  'Mc' : {'name': 'Moscovium', 'mass_number': [289], 'group': 'Post-Transition Metal'},
  'O' : {'name': 'Oxygen', 'mass_number': 16, 'group': 'Nonmetal'},
  'S' : {'name': 'Sulfur', 'mass_number': 32, 'group': 'Nonmetal'},
  'Se' : {'name': 'Selenium', 'mass_number': 79, 'group': 'Nonmetal'},
  'Te' : {'name': 'Tellurium', 'mass_number': 128, 'group': 'Metalloid'},
  'Po' : {'name': 'Polonium', 'mass_number': [208.982], 'group': 'Metalloid'},
  'Lv' : {'name': 'Livermorium', 'mass_number': [293], 'group': 'Post-Transition Metal'},
  'F' : {'name': 'Fluorine', 'mass_number': 19, 'group': 'Halogen'},
  'Cl' : {'name': 'Chlorine', 'mass_number': 35, 'group': 'Halogen'},
  'Br' : {'name': 'Bromine', 'mass_number': 80, 'group': 'Halogen'},
  'I' : {'name': 'Iodine', 'mass_number': 127, 'group': 'Halogen'},
  'At' : {'name': 'Astatine', 'mass_number': 210, 'group': 'Halogen'},
  'Ts' : {'name': 'Tennessine', 'mass_number': [294], 'group': 'Halogen'},
  'He' : {'name': 'Helium', 'mass_number': 4, 'group': 'Noble Gas'},
  'Ne' : {'name': 'Neon', 'mass_number': 20, 'group': 'Noble Gas'},
  'Ar' : {'name': 'Argon', 'mass_number': 40, 'group': 'Noble Gas'},
  'Kr' : {'name': 'Krypton', 'mass_number': 84, 'group': 'Noble Gas'},
  'Xe' : {'name': 'Xenon', 'mass_number': 131, 'group': 'Noble Gas'},
  'Rn' : {'name': 'Radon', 'mass_number': 222, 'group': 'Noble Gas'},
  'Og' : {'name': 'Oganesson', 'mass_number': [294], 'group': 'Noble Gas'},
 }  
search_key = input("Enter the symbol, name, or group of the element you are looking for (Case sensitive): ")

element_info = elements_info.get(search_key)

if element_info:
    print(f"Element Name: {element_info['name']}")
    print(f"Mass Number: {element_info['mass_number']}")
    print(f"Group: {element_info['group']}")
else:
    print("Element not found. Please try again.")       
"""


# Train  ticket challenge
"""
station = int(input("Enter how many stations you need to travel: "))
adult = int(input("Enter how many adult tickets are required: "))
child = int(input("Enter how many child tickets are required: "))
time = int(input("Enter the time of day you will be travelling: "))
cost_per_station_adult = 20
cost_per_station_child = cost_per_station_adult * 0.5
#cost_per_station_child = half_price
#cost_per_station_adult = float(station)
#cost_per_station_child = float(child)
if 6 <= time <= 9:
   cost_per_station_adult += 5
   cost_per_station_child += 2.50

total_cost = (station * cost_per_station_adult * adult) + (station * cost_per_station_child * child ) 

print(f"Your total cost is £{total_cost}")

"""

# Hours worked challenge
"""
ot_pay = 0
hour_pay_N_ot = 0

hours_worked = int(input("Enter the number of hours worked this week: "))
rate_per_hour = float(input("Enter your hourly rate: "))


if 0 <= hours_worked <= 60:
    ot = hours_worked - 40

    if ot > 0:
     ot_rate = rate_per_hour * 1.5
     ot_pay = ot_rate * ot

    hour_pay_N_ot = 40 * rate_per_hour
    total_pay = hour_pay_N_ot + ot_pay

    print(f"Normal pay is £{hour_pay_N_ot:.2f}")
    print(f"Overtime pay is £{ot_pay:.2f}")
    print(f"total pay is £{total_pay:.2f}")

else:
 print("Error. Hours must be between 0 and 60.")

 """



