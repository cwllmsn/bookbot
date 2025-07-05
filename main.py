from stats import get_num_words, get_char_count, get_sort_on_value
import sys

def get_book_test (file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_content = get_book_test(file_path)
    num_words = get_num_words(book_content)
    char_count = get_char_count(book_content)
    sort_on_value = get_sort_on_value(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for item in sort_on_value:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()