# Problem Set 3
# Name: 尤韦捷
# github repos: https://github.com/AemonYwj/pyHw
'''
For the record: I have based all my Hws on the problem sets of mit 
course 6.0001, although I did wrote all the codes on my own
'''


import string

FILENAME = "words.txt"

# 用于从words.txt中获得实际存在的词的列表
def load_words(file_name=FILENAME):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

# 基类Message
class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words()

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return  self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words
        return copy_valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict = {}
        for letter in string.ascii_lowercase:
            encrypted_letter = chr((ord(letter)+shift-ord('a'))%26 +ord('a'))
            dict[letter] = encrypted_letter
        for letter in string.ascii_uppercase:
            encrypted_letter = chr((ord(letter)+shift-ord('A'))%26 +ord('A'))
            dict[letter] = encrypted_letter
        return dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        punctuations = string.punctuation + ' '
        newString = []
        encrypt_dict = self.build_shift_dict(shift)
        for letter in self.message_text:
            if letter not in punctuations:
                newletter = encrypt_dict[letter]
                newString.append(newletter)
            else:
                newString.append(letter)
        newText = ''.join(newString)
        return newText

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.valid_words = load_words()
        self.shift = shift
        self.encrtption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
    

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        dict_copy = self.encrtption_dict.copy()
        return dict_copy


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrtption_dict = self.get_encryption_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words()

    def get_decryption_dict(self,shift):
        '''
        shift(int): the shift steps it trys to get the dictionary
        
        Returns: a dictionary containing 26 lower case letters and their decrypted 
        letters

        Note: I am honestly just copying the get_encrpytion_dict func above
        '''
        dict = {}
        for letter in string.ascii_lowercase:
            encrypted_letter = chr((ord(letter) + shift-ord('a'))%26 +ord('a'))
            dict[letter] = encrypted_letter
        for letter in string.ascii_uppercase:
            encrypted_letter = chr((ord(letter)+shift-ord('A'))%26 +ord('A'))
            dict[letter] = encrypted_letter
        return dict

    
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value

        Note: for the law of ceaser encryption makes its decryption just another
        encryption with a shift that equals to 26 minus the original shift value,
        so what returns in the turple is the shift it used to encrypt this message
        And I actually just copied the code I wrote above to encrypt the text...
        :D
        '''
        punctuation = string.punctuation + ' '
        last_count = 0
        for shift in range(26):
            decrypted_list = []
            decryption_dict = self.get_decryption_dict(shift)
            for letter in self.message_text:
                if letter not in punctuation:
                    decrypted_letter = decryption_dict[letter]
                    decrypted_list.append(decrypted_letter)
                else:
                    decrypted_list.append(letter)
            decrypted_message = ''.join(decrypted_list)
            decrypted_words = decrypted_message.split()
            count = 0
            for word in decrypted_words:
                if word in self.valid_words:
                    count += 1
            if count >= last_count:
                last_count = count
                best_shifts = shift
                best_fit = decrypted_message
        return (best_shifts,best_fit)


        

        

if __name__ == '__main__':

    # #TEST
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())


    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    # plaintext = PlaintextMessage(
    #     'this is a secret message, you should not be able to find out!',
    #     13
    # )

    # ciphertext = CiphertextMessage(plaintext.get_message_text_encrypted())
    # print('Encrypted Message:',ciphertext.message_text)
    # print('Decryption Info:',ciphertext.decrypt_message())
    text = input('Please enter the text you wish to encrypt:')
    k = int(input('Please enter an intergar K with which you would like to encrypt the message:'))
    plaintext = PlaintextMessage(text,k)
    encrpted_text = plaintext.get_message_text_encrypted()
    print('Your text is encrpted to be:',encrpted_text)
    ciphertext = CiphertextMessage(encrpted_text)
    print('Decryption Info(decryption key,decrypted message):',ciphertext.decrypt_message())
    