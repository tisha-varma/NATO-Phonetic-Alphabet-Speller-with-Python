# TODO : Create a dictionary in that format
import pandas

data = pandas.read_csv("nato-phonetic-alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


# TODO : Create a list of phonetic code words from a word that user inputs.
user_input = input("Enter your word : \n").upper()


def generate_phonetic():
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in alphabet phase')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
