#--------------------------------------------
#   Name: Fahrin Bushra
#   ID: 1669159
#   CCID: bushra1
#   CMPUT 274, Fall 2021
#
#   Weekly Exercise #4: Text Preprocessor
#-------------------------------------------- 

import sys
def both_present(word: str):
    '''Returns true if both integers and characters are present in word
    '''
    digits = "0123456789"
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = "~!@#$%^&*()_-+=`<>?/.,\|}{[]''"":;"
    
    d = False
    a = False
    
    for char in word:
    	if char in digits:
    	    d = True
    	if (char in alphabets) or (char in symbols):
    	    a = True
    return (d and a)
    
    
def print_words(word_list:list):
    ''' Prints out all the words in word_list as a concatenated string
    '''
    
    output = ''
    for word in word_list:
        output = output + word.strip() + " "
    output = output.strip()
    print(output)


def rem_digits(word: str):
    ''' Removes all integers from a word if both_present returns true
    '''
    
    digits = "0123456789"
    if both_present(word) == True:
        new_word = ''
        for char in word:
            if char not in digits:
                new_word = new_word + char
        return new_word
    else:
        return word


def rem_symbols(word: str):
    ''' removes all symbols from word
    '''
    
    symbols = "~!@#$%^&*()_-+=`<>?/.,\|}{[]''"":;"
    
    new_word = ''
    for char in word:
        if char not in symbols:
            new_word = new_word + char
    return new_word
  
    
def rem_stop_words(word_list: list, stop_words_list: list):
    ''' Returns a new list which contains all words from word list
    that are not in stop_words_list
    '''
    new_list = []
    for item in word_list:
        if item not in stop_words_list:
            new_list.append(item)
    return new_list 
   
        	
def turn_to_lower(word_list: list):
    ''' Converts all words in word_list to lowercase
    '''
    
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()


def preprocess():
    ''' Takes in space separated strings from user. Processes the input in the following ways:
    For each word:
        1. Converts to lowercase.
        2. Removes all punctuation and symbols.
        3. Removes all numbers UNLESS the token consists only of numbers.
        4. If the word is a stopword (see the list below), removes it.
        5. If the word has not been completely removed by steps 1-4, adds it to a list of processed
    words.
    '''
    FILE = open('stopwords.txt', 'r')
    stop_words_list = FILE.read().strip()
    stop_words_list = stop_words_list.strip("]")
    stop_words_list = stop_words_list.strip("[").split(",")
    for i in range(len(stop_words_list)):
        word = stop_words_list[i].replace('"', '').strip()
        stop_words_list[i] = word
    FILE.close()

    word_list = input().strip().split()
    turn_to_lower(word_list)


    if len(sys.argv) < 2:
        for i in range(len(word_list)):
            word_list[i] = rem_symbols(word_list[i])
        for i in range(len(word_list)):
            word_list[i] = rem_digits(word_list[i])
        word_list = rem_stop_words(word_list, stop_words_list)
        print_words(word_list)
        return
        
           


    elif len(sys.argv) == 2:
    	if((sys.argv[1] == "keep-digits")):
    	    for i in range(len(word_list)):
    	        word_list[i] = rem_symbols(word_list[i])   	    
    	    word_list = rem_stop_words(word_list, stop_words_list)
    	    print_words(word_list)
    	    return
    	
    	elif((sys.argv[1] == "keep-symbols")):
    	    for i in range(len(word_list)):
    	        word_list[i] = rem_digits(word_list[i])   
    	    word_list = rem_stop_words(word_list, stop_words_list)
    	    print_words(word_list)
    	    return
    	    
    	elif((sys.argv[1] == "keep-stops")):
    	    for i in range(len(word_list)):
    	        word_list[i] = rem_symbols(word_list[i])
    	    for i in range(len(word_list)):
    	        word_list[i] = rem_digits(word_list[i])

    	    print_words(word_list)
    	    return    
    	
    	else:
    	    print("Incorrect mode. Usage: python3 freq.py <mode>. mode = keep-symbols/keep-stops/keep-digits")
    	    return
    	
    else:    
    	print("Too many arguments. Usage: python3 preprocess.py <mode >")
    	return


if __name__ == "__main__":
    preprocess()
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant 
    # to this exercise, so you should call your code from here.
