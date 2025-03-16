# RANDOM JOKES 
''' SCRIPT BY AHMED XD
DATE: 20 march 2025
time to make 20/30 mint
contact: +923088588638'''

import pyjokes
import time
import os
#clear environment 
def clear():
    os.system('clear')

#main joke
def joke():
    print("here u will get only programming jokes")
    time.sleep(3)
    clear()
    print("\033[42mhere is a joke:❤️\033[0m\n")
    joke = pyjokes.get_joke()
    print(f" \033[35m {joke}")
    time.sleep(4)
 #   os.system(delete)
    user = input("an other joke? yes/no: ")
    if 'y' in user:
        clear()
        joke()
    elif 'n' in user:
        os.system('python main.py')
    else:
        print("enter correct option ")

#infine loop for continue joke (idk)
joke()