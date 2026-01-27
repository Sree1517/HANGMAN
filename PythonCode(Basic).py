import random
import nltk #Natural Language Tool Kit
#nltk.download('words') #download word dataset
from nltk.corpus import words #acces data set
def getRandom():
 word_list=words.words() #get words as list
 wl=[w for w in word_list if len(w)==5 ]
 random_Word=random.choice(wl)
 return random_Word 
def play():
 random_Word=getRandom()
 word_blank=['_']*len(random_Word)
 #a
 # print("Random word:",random_Word)
 attempts=8 #considering the words
 while attempts>0:
    print("\nCurrent Word:"+''.join(word_blank))
    guess=input("Guess a letter: ").lower()
    attempts-=1
    if guess in random_Word:
        for i in range(len(random_Word)):
            if random_Word[i]==guess:
                word_blank[i]=guess
        print('Great guess!')
    else:
        print("Wrong guess! ")
    print("attempts left:-",attempts)
    if '_' not in word_blank:
        print("Congratulations!! YOU GUESSED CORRECT WORD:",random_Word)
        break
 if attempts==0 and '_' in word_blank:
    print("you have run out of attempts..The word was:",random_Word)
play()