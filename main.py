import sys
from stats import count_word_count, count_char_occurances, sort_char_occurances

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        return book.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_word_count(get_book_text(book))} total words")
    print("--------- Character Count -------")
    occ_dict = count_char_occurances(get_book_text(book))
    sorted_char_occurances = sort_char_occurances(occ_dict)
    for char in sorted_char_occurances:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")


main()
