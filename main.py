#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


"""
Steps

1. Loop through the list of names in the file
2. Replace each [name] with the specific name we looped through
3. Create a new file that contains this updated letter with the specific name
"""

PLACEHOLDER = '[name]'
names_lst = []

# Accessing all the names
with open('./input/Names/invited_names.txt') as names:
    # readlines() returns every line and places it in a list.
    all_invited = names.readlines()

# Accessing letter information
with open('./input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()

# names_lst contains all names without \n
for name in all_invited:
    names_lst.append(name.strip('\n'))

for invited in names_lst:
    new_letter = letter_contents.replace(PLACEHOLDER, invited)
    # Note that if the specific file name doesn't exist, this will create a new one.
    with open(f'./output/ReadyToSend/letter_for_{invited}', mode='w') as rep:
        sentence = rep.write(new_letter)


