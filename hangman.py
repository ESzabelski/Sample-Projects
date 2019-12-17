import random

pic=["""
 ---|
 |  |
    |
    |
    |
--------""","""
 ---|
 |  |
 0  |
    |
    |
--------""","""
 ---|
 |  |
 0  |
 |  |
    |
--------""","""
 ---|
 |  |
 0  |
/|  |
    |
--------""","""
 ---|
 |  |
 0  |
/|\ |
    |
--------""","""
 ---|
 |  |
 0  |
/|\ |
/   |
--------""","""
 ---|
 |  |
 0  |
/|\ |
/ \ |
--------"""]


letters="abcdefghijklmnopqrstuvwxyz"
#answer="dog"
wrong_letters=[]
correct_letters=[]


#displays the board, guesses etc
def board(theboard,guesses_taken,correct_letters,wrong_letters):
    print()
    print("The number of guesses remaining is: %s" %( (len (pic))-guesses_taken))
    print("Correct letters guessed: " + " ".join(correct_letters))
    print("Wrong letters guessed: " + " ".join(wrong_letters))

    print(theboard[guesses_taken])
    print()


#checks a letter input, then puts this into the right slots
def guess(the_word,how_many_guesses): 
    global wrong_letters,correct_letters

    temp=""
    for i in the_word:
        if i in correct_letters:
            temp=temp+i
        else:
            temp=temp+"_"

    print(temp)
    print()
    print("Guess a letter")
    g=input()
    while g.isalpha() !=True or g in wrong_letters or g in correct_letters or len(g)!=1:
        print("Type a single letter you have not guessed yet")
        g=input()
    g=g.lower()
    if g in the_word:
        correct_letters.append(g)
        return (how_many_guesses)        
    else:
        wrong_letters.append(g)
        return (how_many_guesses+1)



def mode_and_word():
    samplewords=["dog","cat","wolf","sword","vanquish","fleet","trip","eve"]
    print("    Welcome to Hangman!    ")
    print()
    print("Do you want to have another player input a word, or have a random word?")
    print("(r)andom for word or (p)layer for a player input word")
    i=input().lower()
    if i.startswith("r"):
        word_index=random.randint(0,(len(samplewords)-1))
        print("The secret word has " + str(len(samplewords[word_index])) +" letters")
        return samplewords[word_index]
    if i.startswith("p"):
        print("Please type a word to have the other player try to guess")
        word=input()
        for i in range(40):
            print()
        print(("The secret word has " + str(len(word)) +" letters"))
        return word
        

#main loop to take a word, then have a player take guesses to get it right
def main():
    global correct_letters, wrong_letters
    total_guesses=len(pic)
    play_again="yes"

    while play_again=="yes":
        secret_word=mode_and_word()
        guesses_taken=0

        all_letters_guess=False

        while guesses_taken<total_guesses and all_letters_guess==False:

            play_again="no"



            
            board(pic,guesses_taken,correct_letters,wrong_letters)
##            guess(secret_word)
##            guesses_taken+=1  #I had to do below to not get stuck with crazy globals
            guesses_taken=guess(secret_word,guesses_taken)
            


            all_letters_guess=set(correct_letters)==set(secret_word)

        
        if all_letters_guess==True:
            print("You win!")
            print("The word was " +secret_word)
        else:
            print("You lose, the word was " +secret_word)
            
        print("Do you want to play again?  (y)es or (n)o ")
        play=input().lower()
        if play.startswith("y"):
            play_again="yes"
            wrong_letters=[]
            correct_letters=[]
        else:
            play_again="no"


#set secret word
    #break secret into list

#update board and guesses

main() 

