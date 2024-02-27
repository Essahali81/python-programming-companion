# Objective 6
"""
word="Hello"
for counter in range(0,len(word)):
    print("letter", counter, "is",word[counter])
"""

# Square numbers challenge
"""
for counter in range(1,21):
    if counter == 21:
        break
    elif counter != 21:
        Squared = counter * counter
        print(counter,"squared is equal to",Squared)

"""

# 9 green bottles challenge
"""
bottles = int(input("enter the number of bottles: "))

for counter in range(bottles, 0, -1):
    print(f"{counter} green bottles sitting on the wall")
if counter == 1:
    print(f"{counter} green bottle sitting on the wall")

"""


# times table challenge 1
"""
multiply_by = int(input("Enter the number you wish to see the multiplication table of: "))

print("here is the table for",multiply_by)

for counter in range(1, 13):
    total = counter * multiply_by
   # print("here is the table for",multiply_by)
    print(multiply_by,"times by", counter,"is equal to",total)
    
"""


# Fibonacci Sequence challenge
"""
def Fibonacci(n):
    fib = [0, 1]
    
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        
    return fib
    
result = Fibonacci(21)
print(result)

"""

# Average calculator
"""
num_values = int(input("Enter how many numbers you want to average: "))

total = 0

for _ in range(num_values):
    number = float(input("Enter a number: "))
    total += number

    mean = total / num_values

    print(f"total: {total}")
    print(f"mean: {mean}")

"""

#FizzBuzz
"""
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz") 
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print("Buzz")
else:
     print(i)


"""


# Times Tables 2
"""
import random
correct_answers = 0

for _ in range(10):
    random_number = random.randint(1,9)
    diff_number = random.randint(1,9)
    question = f"{random_number} * {diff_number} = "
    answer = random_number * diff_number
    user_answer = int(input(question))

    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect - the answer is {answer}.")

if correct_answers >5:
    print(f"Well Done! You got {correct_answers} out of 10 correct.")
else:
 print(f"Good try. You got {correct_answers} out of 10 correct.")

"""


# ROT13
'''
def  rot13(text, shift):
    result = ""
    for char in  text:
        if  char.isalpha():
            is_upper =  char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift)  % 26 + ord('A' if is_upper else 'a'))

            result += shifted_char
        else:
            result += char

    return result

encode_decode = input("Enter if you would like to encode or decode: ")

if encode_decode ==  "encode":

   plain_text = input("Enter your message to be encoded: ")
   cipher_text = rot13(plain_text, 13)
   print(cipher_text)
elif encode_decode == "decode":

    cipher_text = input("Enter your message to be decoded: ")
    plain_text = rot13(cipher_text, -13)
    print(plain_text)
else:
     print("Invalid Input")


'''



# Letter Game Challenge

'''

def points():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    scoreboard = {'e': 1, 'a': 2, 'r': 3, 'i': 4, 'o': 5, 't': 6, 'n': 7, 's': 8, 'l': 9, 'c': 10, 'u': 11, 'd': 12, 'p': 13, 'm': 14, 'h': 15, 'g': 16, 'b': 17, 'f': 18, 'y': 19, 'w': 20, 'k': 21, 'v': 22, 'x': 23, 'z': 24, 'j': 25, 'q': 26}

    word = input('Please enter a five-letter word: ')
    score = 0

    # Check each letter of the word to see if it matches any of the letters in our list
    for i in range(5):
        if letters.find(word[i].lower()) != -1:
            score += scoreboard[word[i].lower()]

    return score

print(points())

'''