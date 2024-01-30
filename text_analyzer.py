####################_Header_####################
'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marian Sopoliga
email: sopoligamarian@gmail.com
discord: Marian S.
'''
####################_Text to analyze_####################

TEXTS = [
"""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",

"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",

"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",]

print_line = "-" * 40
splitted_texts = list(enumerate(TEXTS, start=1))
count_of_texts = len(splitted_texts)
registered_users = {"bob": "123", 
                    "ann": "pass123", 
                    "mike": "password123", 
                    "liz": "pass123"}

####################_Enter login and password_####################

user_login = input("Enter your login: ")
user_password = input("Enter your password: ")

####################_Verify login and password_####################

if user_login in registered_users and registered_users[user_login] == user_password:
    print(f"username:{user_login} \npassword:{user_password}")
    print(print_line)
    print(f"Welcome to the app, { user_login} \nWe have {count_of_texts} texts to be analyzed.")
    print(print_line)
else:
    print(f"username:{user_login} \npassword:{user_password} \nunregistered user, terminating the program..")
    quit()

####################_Validate text sellection_####################
    
entered_input = input(f"Enter a number btw. 1 and {count_of_texts} to select: ")
if not entered_input.isdigit() or int(entered_input) not in range(1, count_of_texts + 1):
    print("Incorrect entry. Terminating the program.")
    quit()
else:
    selected_text = list(splitted_texts[int(entered_input) - 1])[1]

####################_Total words_count in selected list_####################

clean_words = list()
words_count = 0
for single_word in selected_text.split():
    clean_word = single_word.strip(".,?!-_")
    clean_words.append(clean_word)
    words_count += 1
    
print(print_line)
print(f"There are {words_count} words in the selected text.")

###################_Wordsc ount starting with capital letter_####################

capital_words_count = 0
for word in clean_words:
    if word[0].isupper():
        capital_words_count +=1
print(f"There are {capital_words_count} titlecase words.")

####_Words count uppercase, lowercase, numeric, sum of numeric strings_#####

uppercase_word_count = 0
lowercase_word_count = 0
numeric_word_count = 0
sum_numeric_string = 0

for word in clean_words:
    if word.isupper() and word.isalpha():
        uppercase_word_count +=1
    elif word.islower():
        lowercase_word_count +=1
    elif word.isdigit():
        numeric_word_count +=1
        sum_numeric_string = sum_numeric_string + int(word)
    else: 
        continue

###################_Print values_####################

print(f"There are {uppercase_word_count} uppercase words.")
print(f"There are {lowercase_word_count} lowercase words.")
print(f"There are {numeric_word_count} numeric words.")
print(f"The sum of all the numbers {sum_numeric_string}")

###################_Occurrences of different word lengths_####################

len_word_occurrences = dict()

for word in clean_words:
    len_word = len(word)
    if len_word in len_word_occurrences:
        len_word_occurrences[len_word] +=1
    else:
        len_word_occurrences[len_word] = 1

###################_Print bar chart of occurrences_####################      

max_occurrence = max(len_word_occurrences.values())
print(print_line)
print(f"LEN| {'OCCURRENCES'.center(max_occurrence)} |NR.")
print(print_line)

for length in sorted(len_word_occurrences):
    occurrences = len_word_occurrences.get(length, 0)
    print(f"{length:3}| {'*' * occurrences:<{max_occurrence}} |{occurrences}")
print(print_line)