import sys;
from stats import get_num_of_words;
from stats import get_frequency;
from stats import sort_data;

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read();
        return file_contents;        
        # print(file_contents);


def main():
    print("Hoe to get book details run:")
    print("Usage: python3 main.py <path_to_book>")
    # this is what is run in the command line
    # python3 main.py books/frankenstein.txt
    # below is how to access text
    filename = sys.argv[1];
    # text of book
    book_text = get_book_text(filename);
    # get the num of words
    num_of_words = get_num_of_words(book_text);
    print("============ BOOKBOT ============");
    print(f"Analyzing book found at {filename}...");
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words");
    print("--------- Character Count -------");
    freq = get_frequency(book_text);
    sort_data(freq);
    print("============= END ===============");

main();


# print(sys.argv[1]);