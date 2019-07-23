import random

dictionary = open('words_alpha.txt', 'r')

words = [line.rstrip('\n') for line in dictionary]
print(words[random.randrange(0, len(words)-1)])
dictionary.close()
