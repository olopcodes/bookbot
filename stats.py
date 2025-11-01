def get_num_of_words(book_text):
    count = 0;
    arr_text = book_text.split();

    
    for text in range(len(arr_text)):
        count += 1;  
    return count;


def get_frequency(text):
    # initiate a new dictionary
    frequency = {}; 
    # convert all text to lowercase
    lower_text = text.lower();
    # loop of the text
    for char in lower_text:
        # skip if character is a space value
        if char.isspace():
            continue;
        # check if character key is in dictionary
        elif char in frequency:
            # add one inside already
            frequency[char] += 1;
        else:
            # create a key and the value is one
            frequency[char] = 1;
    # show results
    return frequency;


def sortByNum(e):
    return e["num"];


def print_count(a_list):
    for item in a_list:
        print(f"{item['char']}: {item['num']}");

def sort_data(dict):
    #initialize list
    my_list = [];
    
    # print(dict);
    for item in dict:
        # create new dictionary
        new_dict = {}
        # add key value pair of "char" and "item"
        new_dict["char"] = item;
        # add key value pair of "num" and value
        new_dict["num"] = dict[item];
        # add dictionary to list
        my_list.append(new_dict);
    # sort list by function
    sorted_list = sorted(my_list, key=sortByNum, reverse=True);
    
    print_count(sorted_list);