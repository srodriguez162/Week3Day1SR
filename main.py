# String Practice:

# Create a Python program that asks the user to input a sentence.
# Print the first and last letter of the sentence.
# Convert the entire sentence to uppercase and print the result.
# Find and print a substring from the inputted sentence.
# Replace a word in the sentence and print the updated sentence.
sentence_1 = input('Type a sentence ') #the sentence I used is," the dog is big"
print(f'{sentence_1}')
print(sentence_1[:1])
print(sentence_1[-1:])
print(sentence_1.upper())
print(sentence_1.find('big'))
print(sentence_1[11:14])
print(sentence_1.replace('big', 'small'))
# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
# Print a message back to the user with this information.
# Note: Make sure to convert the age to an integer.
name = input('what is your name? ')
print(f'my name is {name}')
age = int(input('what is your age? '))
print(f'my age is {age}')
movie = input('what is your favorite movie? ')
print(f'my favorite movie is {movie}')
print(f'my name is {name}, I am {age} years old, and my favorite movie is {movie}')
# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
object_1 = input('Select an object in the room ')
object_2 = input('select a second object ')
object_3 = input('select a third object ')
print('the objects I found in class are a ' + object_1 + ',' +object_2 + ', and ' + object_3)
# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:
sentence = input('insert sentence')
words = sentence.split()[::-1]
l = []
for i in words:
  l.append(i)
  print(" ".join(l))
# reversed_sentence = ''.join(reversed(words))
# print(reversed_sentence)
# Create a Python program that asks the user for the name of their favorite book, movie, and song.
print('hello')
# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."


# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."