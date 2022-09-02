# Problem Set 1b
# Name: 尤韦捷
# github repos: https://github.com/AemonYwj/pyHw
'''
For the record: I have based all my Hws on the problem sets of mit 
course 6.0001, although I did wrote all the codes on my own
'''



from ntpath import join
from operator import ge
import random
import string

#from sqlalchemy import false, true

# 如果运行不了，可以考虑改一下这里的相对路径
WORDLIST_FILENAME = 'hangmanDict.txt'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# # Test
# print(load_words())

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    flag = True
    for letter in secret_word:
        if letter not in letters_guessed:
            flag = False
    return flag

# # test
# print(is_word_guessed('apple',['a','b','p','s','d','e','l']))
# print(is_word_guessed('apple',['a','b','p','s','d','e']))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    l = []  # the output list
    for letter in secret_word:
        if letter in letters_guessed:
            l.append(letter)
        else:
            l.append('_')
    return ''.join(l)

# # test
# sw = 'apple'
# lg = ['a','e','i','k','p','r','s']
# print(get_guessed_word(sw,lg))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    lowcaseletter = string.ascii_lowercase
    for char in lowcaseletter:
        if char not in letters_guessed:
            available_letters.append(char)
    return ''.join(available_letters)
    
# # test
# lg = ['a','e','i','k','p','r','s']
# print(get_available_letters(lg))



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game of Hangman!")
    n = len(secret_word)
    print("I am thinking of a word that is",n,"letters long.")
    print('----------------')
    letter_guessed = []
    for i in range(1,n+1):
        chances_left = n+1-i
        if i == n:
            print("You have",chances_left,"guess left!")
        else:
            print("You have",chances_left,"guesses left.")
        print('Available letters are: ', get_available_letters(letter_guessed))
        char = input('Please enter the letter you guessed in low case: ')
        letter_guessed.append(char)
        if char in secret_word:
            if is_word_guessed(secret_word,letter_guessed):
                print('Congratulations! You have successfully guessed the word!')
                print(get_guessed_word(secret_word,letter_guessed))
                break
            else:
                print(
                    'So close! ',
                    get_guessed_word(secret_word,letter_guessed)
                    )
        else:
            print(
                'Oops! That letter is not in my word:',
                get_guessed_word(secret_word,letter_guessed)
                )
    if not is_word_guessed(secret_word,letter_guessed):
        print('Sorry, but you have ran out of chances...',\
            'Here is my word:',secret_word)



if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
