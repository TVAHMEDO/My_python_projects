#code by Ahmed
''' THIS IS A SIMPLE TODO LIST SAVER IN LIST + STORAGE AS todo.txt 
DATE:- 8 MARCH 2025'''
import os
import time

#colors
green = "\033[32m"
reset = "\033[0m"
yellow = "\033[33m"
def clear():
    os.system('clear')
list = []

def main():
    print(f'''
    OWNER: {green}AHMED XD{reset}
    TOOL: TODO MAKER
    VERSION: {green}1.0{reset}''')
    print("\n[1] enter one for make a Todo")
    print("[2] enter two for see Todo list")
    print("[3] enter tree or exit for exit\n")
    user = input("enter number 1/2 :")
    if user == '1':
        clear()
        user_todo = input("enter Todo : ")
        list.append(user_todo)
        with open("todo.txt","a") as file:
            file.write(user_todo + "\n")
            print("saved successful")
            print(f"\n{yellow} !note:- the Todo is saved in list and storage as todo.txt{reset}")
            time.sleep(3)
            clear()
            main()
    if user == '2':
        for lis in list:
            print(f"{green}{lis}{reset}")
            time.sleep(5)
            clear()
            main()
    elif user == '3' and 'exit':
        print("thanks for using this program")
        os.system('exit')        


main ()
        