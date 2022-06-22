import pandas


nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(nato_dict)
is_on = True
while is_on:
    try:
        user_input = input("Enter a word: ").upper()
        user_input_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only alphabets allowed\n")
    else:
        print(user_input_list)
        is_on = False

