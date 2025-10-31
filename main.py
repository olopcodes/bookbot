from stats import get_num_of_words;
from stats import get_frequency;


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read();
        return file_contents;        
        # print(file_contents);


def main():
    # text of book
    book_text = get_book_text("books/frankenstein.txt");
    # get the num of words
    num_of_words = get_num_of_words(book_text);
    print(f"Found {num_of_words} total words");

    get_frequency(book_text);
    

main();