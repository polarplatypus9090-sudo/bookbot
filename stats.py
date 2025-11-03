# returns number of words

def word_count(text):
    words = text.split()
    return len(words)

# counts each character(case sensitive) 
# and stores results in a dictionary

def char_count(text):
    letters = {}
    for char in text:
       char = char.lower()
       if char not in letters:
           letters[char] = 1
       else:
           letters[char]+= 1
    return letters

# helper function to set sorting method

def sort_on(letters):
    return letters["num"]

# creates a dictionary to count each character

def char_dictonary(char_counts):

# empty list to hold characters 

    char_sorted = []
# loops through each character in the char_counts dictionary

    for c in char_counts:

# grabs the amount of times a character appears

        count = char_counts[c]

# builds dictionary

        char_dict ={}
        char_dict["char"] = c
        char_dict["num"] = count

# builds the list that will be sorted

        char_sorted.append (char_dict)

# sorts the list that was built by the for loop

    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted








    

