#my build of a guessing game.

import random
print('Enter your name below')
myname = input()
print('Hello!, welcome to the number guessing game, ' + str(myname) + '.Now guess a number between 1 and 10')
secretnumber = random.randint(1,10)
print(secretnumber)
x=0

for i in range(1,7):
   try:
      print('This is your guess number ' + str(i) + ' out of 6')
      guessnumber = input()
      if int(guessnumber) > secretnumber:
                print('You guessed too high')
      elif int(guessnumber) < secretnumber:
                print('you guessed too low')
      else:
           print('Wow that is the correct answer!')
           x = 999
           break
   except ValueError:
       print('Please only enter integer values')   

if x != 999:
    print('Sorry you are out of tries. The number i had was ' + str(secretnumber))
