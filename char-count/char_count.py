import pprint

sentence = "This is supposed to be a looong sentence"
user_in = input("Would you like to input your own sentence? Y/N: ")

if user_in.upper() == "Y":
    print("Please type or paste your sentence")
    user_sent = input()
else:
    print("Alrighty, we'll count the characters in the following " f"sentence:\n\n\"{sentence}\"\n")

count_dict = {}

for character in sentence.upper():

    """if char does not exist set 0 as value, if it exists
    nothing happens."""
    count_dict.setdefault(character, 0) 
    count_dict[character] += 1

# Sorting dict by keys and printing it
print( dict(sorted(count_dict.items())) )

# Or you can use pprint module. 
# It will be printed sorted
pprint.pprint(count_dict)