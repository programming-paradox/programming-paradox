import json  # Importing The Json Module To Parse The Data
from difflib import get_close_matches  # For Checking The Word Similarity Ratio

data = json.load(open("data.json"))  # Opening The Json File


def translate(word):
    w = word.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            f"Did You Mean {get_close_matches(w, data.keys())[0]} Instead Enter Y for Yes And N for No:\n")

        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":
            return "The Word Doesn't Exist In Our DataBase"

        else:
            return "We do not understand your query"

    else:
        print("PLease Double Check Your Input")


word = str(input('Please Enter A Word: \n'))

output = translate(word)
for items in output:
    print(items)
