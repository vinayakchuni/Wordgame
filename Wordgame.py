
import itertools
from itertools import *
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
Total_score=0

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



WORDLIST_FILENAME = "words1.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    global Total_score
    score=0
    keys=SCRABBLE_LETTER_VALUES.keys()
    values=SCRABBLE_LETTER_VALUES.values()
    for i in word.lower():
        if i!="" :
            score=score+SCRABBLE_LETTER_VALUES.get(i,0)
    if len(word)==n:
        Total_score+=(score*n)+50
        return (score*n +50)
    else:
        Total_score+=score*len(word)
        return score*len(word)
    
            

    

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              
    print                               
    return ' '


def deal_hand(n):
    """
    
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    global handr
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    handr=hand.copy()
        
    return hand


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    global handr
    hand1=hand.copy()
    for i in word:
        if i in hand1.keys():
            hand1[i]=hand1.get(i)-1
            if hand1[i]==0:
                del hand1[i]
    return hand1
            


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    count=0
    hand1=hand.copy()
    for i in word:
        if i in hand1.keys() and hand1[i]>0:
            hand1[i]=hand1[i]-1
        else:
            return False
    if word in word_list:
        return True
    else:
        return False

        
        

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen
def sum(hand):
    sum=0
    for i in hand.values():
        sum=sum+i
    return sum


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    global HAND_SIZE

    global sum
    
    
    
    
    print display_hand(hand)
    word=raw_input("Enter a word :")
    if word=='.' :

        return Total_score
        
    
    if is_valid_word(word,hand,word_list):
        print "Good Guess, Your score is",get_word_score(word,sum)
        
        
        hand=update_hand(hand,word)
        print hand
        print sum(hand)
        if sum(hand)<8:
            
            k=0
            for x in itertools.permutations(hand.keys(),len(hand.keys())):
                
                if string.join(x,'') in word_list:
                    k=k+1
            if k>0:
                play_hand(hand,word_list)
            else:
                print"No more words are possible using the given letters.Exit by pressing '.'"
                
                
        play_hand(hand,word_list)
    else:
        print"You entered an incorrect word. Try again!"
        play_hand(hand,word_list)
        
    
    return Total_score
    


        
    
        


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    
    """
    

    print"Welcome to the game "
    print "Enter n to play a random hand"
    print "Enter r to play the last hand again"
    print "Enter e to exit the game"

    user_input=raw_input("Enter the correct choice from the above menu: ")
    if user_input=='n':
         play_hand(deal_hand(random.randrange(6,14)),word_list)
    elif user_input=='e':
        print "Game Over"
        return ''
    elif user_input=='r':
        play_hand(handr,word_list)
        
    else :
        play_game(word_list)
    print "Your total score in this hand is",Total_score
    print "Ready for the next hand!"
    play_game(word_list)
    
 
    

    return ''
    
    
    






if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)





