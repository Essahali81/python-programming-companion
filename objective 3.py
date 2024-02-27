#Working with strings
'''
email=input("Enter your email: ")
email_lowercase=email.lower()
print("Your email in lowercase letters is:", email_lowercase)

'''


#Len returns the number of characters in a string
'''
surname = input("Enter your surname: ")
length_name = len(surname)
print("There are", length_name,"letters in your surname.")

'''


#[:?] returns a number of characters to the left of a string ]
'''
sentence = "I saw a wolf in the forest. A lonely wolf"
characters = sentence[-12:]
print(characters)

'''


#[start:end] returns a number of characters in the middle of a string
'''
sentence = "I saw a wolf in the forest. A lonely wolf"
characters = sentence[20:26]
print(characters)

'''


#find returns the location of one string insde another
'''
sentence = "I saw a wolf in the forest. A lonely wolf"
print(sentence)
word = input("Enter the word to find: ")
position = sentence.find(word)
print("The word",word,"is at character", position)

'''


# initial and surname challenge
'''
forename = input("please enter your forename:")
initial_f = forename[0].upper()
print("your first initial is", initial_f)
surname = input("please enter your surname: ")
initial_s = surname[0].upper()
print("your first initial of your surname is", initial_s)
print("that makes your full initials ",initial_f,initial_s)

'''


# Airline ticket challenge
'''
From = input("please input where you are flying from: ")
print("you are flying from",From)
To = input ("please enter where you are flying to: ")
print("you are flying to", To)
code = From[0:4].upper() + "-" + To[0:4].upper()
print("Your flight code is", code)


'''



# Name separator challenge
'''
full_name = input("please enter your full name: ")
forename = full_name.split()[0]
surname = full_name.split()[-1]
print("your forename is",forename)
print("your surname is",surname)


'''


# Word extractor challenge
'''
sentence = "Quick brown fox jumps over the lazy dog."
print(sentence)
delete = input("enter a word to delete: ")
modified_sentence = sentence.replace(delete,'')
print (modified_sentence)

'''
