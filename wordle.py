import random

# Class of different styles for colored text
class style():
    BLACK =   '\033[30m'
    RED =     '\033[31m'
    GREEN =   '\033[32m'
    YELLOW =  '\033[33m'
    BLUE =    '\033[34m'
    MAGENTA = '\033[35m'
    CYAN =    '\033[36m'
    WHITE =   '\033[37m'
    RESET =   '\033[0m'

valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
words = []    
text_file = open("valid-wordle-words.txt", "r")
for i in text_file.readlines():
    words.append(i.replace("\n", ""))
 
# choosing random valid word
target = words[random.randint(0, len(words))]
#print(target)

#########################################################
counter = 0

while True:
     user_Input = input("Enter your guess: ")
     if user_Input == target:
          print(style.GREEN + target + style.RESET+' You Won!')
          break
     elif counter == 5:
          print(' You Lost! The word is: '+ target + style.RESET)
          break

     elif user_Input in words:
          for i,j in zip(user_Input, target):
               if j == i:
                    print(style.GREEN+ i,end="",flush="True")
               elif i in target: 
                    print(style.YELLOW+ i,end="",flush="True")
               else: 
                    print(style.RED+ i,end="",flush="True")
                    if i in valid_letters:
                         valid_letters.remove(i)
     else:
          print('Not a valid word')
     counter = counter +1

     print(style.RESET)      
     print(valid_letters)               
              