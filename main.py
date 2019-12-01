#import words
#promt user to generate a word
#generate a word
#repeat

import random
import time

print('**** Welcome to your own Pictionary word generator ! ****')

#Load the words for the game from a text file
file_name=input('Name of the file with your words: ')
try:
  words = set((line.strip() for line in open(file_name)))
except IOError:
    print("Could not read file:", file_name)
    quit()
#print(words)

#Get a random list
words=list(words)
nb_words=len(words)
print(' You have',nb_words, 'words to play with')
random.shuffle(words)
#print(words)

#Play
name='n'
word_count=0
successes=0
failures=0

while word_count<nb_words:
  name=input("Press n for next word, anything else to stop: ")
   
  if name!='n':
    break

  print('Your word is: ',words[word_count].upper())
  
  t0 = time.time()

  result=input('Success or Failure ? type s for success or anything else for failure')

  print('Time used to guess: ',"{:12.2f}".format(time.time() - t0), 'seconds')

  if result=='s': 
    successes +=1 
  else:
     failures +=1

  print('You have ', nb_words-word_count-1,' words left to play with')
 
  word_count +=1

print('You scored ',successes, 'out of', successes+failures)
print("Goodbye")
