"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jana Lásková
email: janalaskova2@seznam.cz
"""
user_name = input("Enter your username: ")
user_password = input("Enter your password: ")
users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

if user_name in users and users[user_name] == user_password:
    print("\nHi, welcome to the text analysis section.")
else:
    print("\nI’m sorry, but it seems that you are not registered.")
    exit()

text_1 = """Situated about 10 miles west of Kemmerer
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""

text_2 = """The history of the Union Pacific Railroad
in this region is closely tied to the
construction of the transcontinental
railroad in the 19th century. Railroads
helped to shape economic and cultural
landscapes, facilitating trade and
movement across vast distances."""

text_3 = """Fossilized remains of ancient plants and animals
have been discovered in Fossil Butte, providing
evidence of prehistoric ecosystems. These fossils
include fish, insects, and reptiles, which are
remarkably well-preserved, offering scientists
valuable insights into Earth's distant past."""

user_choice = input("\nWhich text would you like to analyze? Enter a number btw. 1 and 3 to select: ")

if not user_choice.isdigit():
    print("\nInvalid input. Please enter a number between 1 and 3.")
    exit()

choices = int(user_choice)
if choices == 1:
   selected_text = text_1
elif choices == 2:
    selected_text = text_2
elif choices == 3:
    selected_text = text_3
else:
    print("\nInvalid choice. The program will now exit.")
    exit()

text_split = selected_text.split()
punctuation = ".,!?;:"
text_cleaned = [word.strip(punctuation) for word in text_split]

capital_letter_words = [word for word in text_cleaned if word.istitle()]
uppercase_word = [words for words in text_cleaned if words.isalpha() and words.isupper()]
lowercase_word = [lwords for lwords in text_cleaned if lwords.islower()]
numbers_as_word = [int(nwords) for nwords in text_cleaned if nwords.isnumeric()]

print("The total number of words in the text is: ", len(text_split))
print("The number of words starting with a capital letter is: ", len(capital_letter_words))
print("The number of words written in uppercase is: ", len(uppercase_word))
print("The number of words written in lowercase is: ", len(lowercase_word))
print("The number of numbers written as words is: " , len(numbers_as_word))
print("The sum of all numbers written as words is: ", sum(numbers_as_word))

print("A bar chart for the frequency of different word lengths in the text.")
word_lengths = {}

for word in text_cleaned:  
    word_length = len(word)  
    if word_length in word_lengths:
        word_lengths[word_length] += 1  
    else:
        word_lengths[word_length] = 1  

for length in sorted(word_lengths.keys()):
    print(str(length) + "| " + "*" * word_lengths[length] + " " + str(word_lengths[length]))