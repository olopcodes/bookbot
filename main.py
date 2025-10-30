def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read();
        return file_contents;        
        # print(file_contents);


def get_num_of_words(book_text):
    count = 0;
    arr_text = book_text.split();
    # one way to solve this 
    # for text in len(arr_text):
    #     count += 1;
    # return count;

    # another way to solve this
    for text in range(len(arr_text) - 1):
        count += 1;  
    return count;


def main():
    # text of book
    book_text = get_book_text("books/frankenstein.txt");
    # get the num of words
    num_of_words = get_num_of_words(book_text);
    print(f"Found {num_of_words} total words");


main();