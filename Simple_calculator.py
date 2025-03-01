#calculator by AHMED_XD:)
import time
import os
#functions
print("HELLO THIS IS SIMPLE CALCULATOR THAT IS MADE BY AHMED_XD\n")
   
#FUNCTION FOR FIND + PLUS
def getsum(a, b):
    return a + b
#FUNCTION FOR FIND MULTIPLICATION 
def multi(a, b):
    return a * b
#FUNCTION FOR FIND DIVISION!
def division(a, b):
    if b == 0:
        return "can't divide by 0" 
    return a / b
 #function for cutting 
def cut(a, b):
     return a - b
 
 #input methods + variable! 
#main function! 
def main():
    print("[1] SUBSTRACTION: ")
    print("[2] Multiplication: ")
    print("[3] Addition")
    print("[4] DIVISION")
    user = input(" enter number 1,2,3,4?: > ")
    os.system('clear')
    a = float(input("input first value: "))
    b = float(input("input second value: "))
    
    if user == '1':
        result = cut(a, b)
      #  cut()
    elif user == '2':
        result = multi(a, b)
   #     multi()
    elif user == '3':
        result = getsum(a, b)
      #  getsum()
    elif user == '4':
        result = division(a, b)
       # division()
    else:
        print("enter correct number")
        time.sleep(2)
        main()
        return 
        
        
       
    print(f" the result is \033[32m{result}\033[0m\n")
   # main()

#os.system('clear')    
main()        
