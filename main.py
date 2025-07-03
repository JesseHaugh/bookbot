from stats import get_num_words, letter_to_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)      
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    letter_count = letter_to_dict(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in letter_count:
        if not letter["char"].isalpha():
            continue
        print(f"{letter["char"]}: {letter["num"]}")
    


def get_book_text(book_path):
    with open(book_path, "r") as f:
        file_contents = f.read()
    return file_contents

main()
