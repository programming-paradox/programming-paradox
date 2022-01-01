"""
Program To Add Password To The Account Text File

-> We will simply open the file and add the password to every account
-> We will not use any external library 

"""

password = "AWAN1010"

filepath = "accounts.txt"

with open(filepath) as fp:
    lines = fp.read().splitlines()

with open(filepath, "w") as fp:
    for line in lines:
        print(line + f":{password}", file=fp)

