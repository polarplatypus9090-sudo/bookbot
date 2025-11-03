import sys
#opens the file to read then closes the file

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


#Gets the text and returns the text

def book_text (path):
    text = get_book_text(path)
    return (text)

#Imports word counter from stats file

from stats import word_count 
from stats import char_count
from stats import sort_on
from stats import char_dictonary
#prints the number of words

def main():
    if len (sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    book_path = sys.argv[1]
    text = book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------"
)
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