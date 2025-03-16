import os
import time

#colors 
red = "\033[32m" 
yellow = "\033[33m" 
reset = "\033[0m" 
blue = "\033[35m" 
d = {
    "hi": "hello bro how are you", 
    "hello": "hii bro",
    }
  
def clear():
    os.system('clear')

def upload():
    clear()
    logo()
    key = input("enter key: ")
    value = input("value")
    d[key] = value
    print("saved successful")
    time.sleep(1)
    clear()

def logo():
    print("_"*40)
    print(f"""
    OWNER: {red}AHMED XD{reset}
    TOOL: SIMPLE AI
    VERSION:{yellow} 1.0{reset}""")
    print("_"*40)   


def main():
    clear()
    logo()
    print("[1] chat with ai: ")
    print("[2] update data of ai: ")
    print("[3] for exit: ")
    user_inp = input("enter 1/2: ")
    if user_inp == '1':
   #     clear()
        chatwithai()
    elif user_inp == '2':
        upload()
    elif user_inp == '3':
        print("thanks for using this program")
        os.system('exit')    
  
def chatwithai():
    print("enter back for back or just enter for continue")
    print(f"{blue}wait a bit{reset}")
    time.sleep(1)
    clear()
    logo()
    print("if u want to back then enter back/break")
    print ("\nhello how I can assist you 😊") 
    user_input = input("You: ").lower()
    if user_input in d:
        print(f" AI: {d[user_input]}")
     #   chatwithai()
      #  WHILE()
    elif user_input == 'back' and 'break':
        main()  
    else:
        print("\nI don't know can u help me to learn it")
        time.sleep(2)
        clear()
        main()
        
main()        