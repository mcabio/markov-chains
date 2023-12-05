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

    #for loop to loop over list of words
    

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


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

print(random_text)
