#opens the file to read then closes the file

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


#Gets the text and returns the text

def book_text ():
    text = get_book_text("books/frankenstein.txt")
    return (text)

#Imports word counter from stats file

from stats import word_count 
from stats import char_count
from stats import sort_on
from stats import char_dictonary
#prints the number of words

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------"
)
    text = book_text()
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    char_counts = char_count(text)
    print("--------- Character Count -----")
    sorted_list = char_dictonary(char_counts)
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

main()