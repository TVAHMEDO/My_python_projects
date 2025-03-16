'''SIMPLE FUNNY TOOL BY AHMED_XD (ME)‚
DATE : 8 march 2025
DAY: SATURDAY '''
import os
import time
#colors
color = "\033[32m"#green
clear = "\033[0m" #white/restore
def brain():
    print("hello' will be start in two seconds! ðŸ™‚")
    time.sleep(2)
    user_input = input("enter the word/sentence  to run forever. which crash your terminal :")
    while True:
        print(user_input + color)
        
 
def menu():
    print(f'''
    OWNER: {color}AHMED_XD{clear}
    TYPE: CRASH SYSTEM
    ''')
    print("[1] enter 1 for crash system")
    print("[2] exit system")
    hm = int(input("enter 1/2 : "))
    if hm == 1:
        brain()
    if hm == 2:
        print("system will exited in 2 seconds")
        time.sleep(2)
        os.system("exit")
    else:
        print(" wrong choose")
        time.sleep(2)
        os.system('clear')
        print(" try again...")
        time.sleep(1)
        os.system("clear")
        menu()    


menu()       