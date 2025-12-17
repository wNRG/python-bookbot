import sys
from stats import get_word_count, get_character_count, sort_dictionary

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    x = get_book_text(file_path)
    y = get_word_count(x)
    z = sort_dictionary(get_character_count(x))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {y} total words")
    print("--------- Character Count -------")
    for item in z:
        if item['char'].isalpha():
           print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")
main()
