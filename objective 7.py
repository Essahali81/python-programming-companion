# objective 7

#program to add up until 0 is entered
"""
total=0
number=1

while number>0:
    number=int(input("enter a number: "))
    total+=number  
print(f"the sum of the numbers is:{total}")
"""



##challenges

# Menu selection challenge
"""
def main_menu():
        print("1. Play Game")
        print("2. Instructions")
        print("3. Quit")


user_input = 0

while user_input not in [1,2,3]:
         user_input = int(input("Please select an option from the menu 1-3: "))
         if user_input==1:
            print("play game")
         elif user_input==2:
             print("instructions")
         elif user_input==3:
            print("Quit")
         else:
          print ("Invalid Option! Please enter again.")

print("Let's Go!")

"""


# Compound Interest challenge
"""
starting_balance = int(input("Enter your starting balance: "))
Interest = int(input("enter the rate of interest: "))
ROI = Interest / 100
new_balance = starting_balance
desired_amount = int(input("enter your desired amount: "))
years = 0
while new_balance < desired_amount:
        new_balance *= (1 + ROI)
        years += 1
print(f"after {years} years your balance will be £{new_balance:.2f}.")

"""

# Guess the number Game
"""
import random

secret_number = random.randint(1,100)
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations you guessed correctly! It took you {tries} tries.")
        break

# if secret_number and guess == 69:
#   print("HAHA 69 lol")
    

"""


# Gamertag challenge
"""
Gamertag = input("Please enter a valid gamertag: ")
if len(Gamertag) >= 15:
    print("Error. The Gamertag must be below 15 characters.")
elif len(Gamertag) <= 4:
    print("Error. The Gamertag must be more than 4 characters.")
else:
    print("Gamertag accepted.")

"""


# Rock, paper, scissors challenge
"""

import random

def play_round():
    choices = ["rock", "paper", "scissors"]

    choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    cpu_guess = random.choice(choices)

    print("Computer guess is", cpu_guess)

    cpu_points = 0
    your_points = 0

    if cpu_guess == choice:
        print("It's a tie!")
    elif (cpu_guess == "rock" and choice == "scissors") or \
         (cpu_guess == "paper" and choice == "rock") or \
         (cpu_guess == "scissors" and choice == "paper"):
        print("Sorry, the computer wins this round.")
        cpu_points += 1
    else:
        print("Congratulations! You win this round.")
        your_points += 1

    return cpu_points, your_points

total_cpu_points = 0
total_your_points = 0
rounds_played = 0

while rounds_played < 3 and total_cpu_points < 2 and total_your_points < 2:
    cpu_points, your_points = play_round()
    total_cpu_points += cpu_points
    total_your_points += your_points
    rounds_played += 1

if total_cpu_points > total_your_points:
    print(f"Tough luck! The computer won the best of 3 with {total_cpu_points} points to {total_your_points}.")
elif total_your_points > total_cpu_points:
    print(f"Congratulations! You won the best of 3 with {total_your_points} points to {total_cpu_points}.")
else:
    print("It's a tie game!")


"""

# Happy Numbers challenge
"""
def sum_of_squares(n):
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy(num):
    seen = set()
    steps = [num]
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
        steps.append(num)
    return num == 1, steps

def print_happy_sequence(number, sequence):
    print(f"The sequence for {number} is:")
    for step in sequence:
        print(step)

def main():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input > 0 and user_input != 4:
            is_happy_result, sequence = is_happy(user_input)
            print_happy_sequence(user_input, sequence)
            if is_happy_result:
                print(f"{user_input} is a happy number.")
            else:
                print(f"{user_input} is a sad number.")
        else:
            print("Please enter a positive integer other than 4.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()


"""

# XP Challenge

player_xp = 0
player_rank = 1
player_role = "Private"

while player_xp < 2000:
    last_game = int(input("Enter the XP earned last game: "))
    player_xp += last_game

    if player_xp >= 1500:
        player_role = "Warrant Officer"
        player_rank += 1
    elif player_xp >= 700:
        player_role = "Staff Sergeant"
    elif player_xp >= 300:
        player_role = "Sergeant"
    elif player_xp >= 100:
        player_role = "Corporal"
       

    print(f"{player_xp}")
    print(f"{player_rank}")
    print(f"{player_role}")   
       
print("Player reached 2000 XP. Exiting program.")

