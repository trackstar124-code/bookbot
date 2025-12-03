import sys
from stats import get_num_words
from stats import character_counts
from stats import sort_letters


def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents


def main():
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the path from command line arguments
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # Get the book text
    text = get_book_text(path)

    # WORD COUNT
    print("----------- Word Count ----------")
    total_words = get_num_words(text)
    print(f"Found {total_words} total words")

    # CHARACTER COUNT
    print("--------- Character Count -------")
    sorted_counts = sort_letters(text)

    for char, count in sorted_counts:
        print(f"{char}: {count}")

    print("============= END ===============")


main()
