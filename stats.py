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


def get_frequency(text):
    # initiate a new dictionary
    frequency = {}; 
    # convert all text to lowercase
    lower_text = text.lower();
    # loop of the text
    for char in lower_text:
        # check if character key is in dictionary
        if char in frequency:
            # add one inside already
            frequency[char] += 1;
        else:
            # create a key and the value is one
            frequency[char] = 1;
    # show results
    print(frequency);
