"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #read entire contents of file as string - .read()
    file = open(file_path).read()

    return file

# print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    #empty dictionary
    chains = {}

    #split words by white space
    words = text_string.split()

    #for loop to loop over list of words by index
    for i in range(len(words)-2):
        #we need to add pair_words (keys) to dictionary chains
        pair_words = (words[i], words[i+1])
        #we created an empty values list
        ##########when we do this it creates an empty list each for loop. we dont want that#######
        # chains[pair_words] = []
        value_word = words[i+2]

    # #seperate for loop for the value - so itll keep looping and adding to the same list
    # for pair_words in chains:
    #     print(pair_words)
        #Check to see if the key is in the dictionary already. if so add value
        if pair_words in chains:
            chains[pair_words].append(value_word)
        #initialize that list and put your word into it
        else:
            chains[pair_words] = [value_word]

        # value_words = words[i+2]
        #dictionary[key] = [value]
    # print(chains)

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []

    #get random key from dictionary -- will use choice and list(chains.keys())
    key = choice(list(chains.keys()))
    #will add each key to the lst
    #we could also do words.extend(key)
    for k in key:
        words.append(k)

    #get random value from dictionary[key]
    # rand_value = choice(chains[key])
    #will add to lst
    # words.append(rand_value)

    #repeat at random based on previous key until KeyError
    while key in chains:

        #1. look up new_key in chains and pull random value that matches new key
        rand_value = choice(chains[key])
        words.append(rand_value)

        #2. make a new key out of key[1], rand_value
        key = key[1], rand_value



        #3. keep doing that
    

    print(words)
    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

#input text = the read string of the file
#make_chains(text_string) <- text_string can = any string
#text_string = input_text
# Get a Markov chain
chains = make_chains(input_text)


# Produce random text
random_text = make_text(chains)

# print(random_text)
