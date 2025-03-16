#AHMED XD
''' THIS CODE IS MADE BY AHMEDXD (ME)
TIME TO MAKE = 1HOUR+
DATE = 15 MARCH 2025'''

import time
import os

dic = {
    "apple": 150,
    "orange":20,
    "banana":100,
    "pineapple":300,
    "fresh dates":220,}
 
def clear():
    os.system('clear') 
def check():
     cur = "current price is: "
     inp = str(input("enter the name to find fruit: ")).lower()
     if cur in dic:
         print(cur + str(dic[inp]))
         input("enter to back")
         main()
     else:
         print("fruit not found ")
         time.sleep(2)
         main()
hm = []       
def order():
    clear()
    for all in dic:
        print(all)
    user = input("\nenter the fruit name to order now: ").lower()   
    if user in dic:
        ahm = hm.append(user)    
    print(f"Fruit ordered successfully {hm}")
    print("\n TYPE 'ANOTHER' TO ORDER ANOTHER\n TYPE ENTER TO BACK")
    back = str(input("ENTER: ")).lower
    if back == 'another':
        print("wait a bit")
        time.sleep(2)
        order()
 #   elif back == 'back':
   #     print("wait a bit sir: ")
   #     time.sleep(0.9)
   #     return
    else:
        print("wrong choice\n try again....")
        main()
     #   main()
   # return hm    


def check_order():
    print("ordered fruits")
    for fruit in hm:
        print(fruit)
    input("enter to back: ")    
    main()
def price():
    nm = int(input(" enter price of fruit: "))
    print(f" ur price is {nm}")
    
     
       
def main():
    clear()
    print('''
    OWNER: AHMED_XD
    DATE: 15/3/2025\n''')
    print("[1] order fruit")
    print("[2] check orders")
    print("[3] check price")
    print("[4] check your total price\n")
    user = int(input(" enter number 1/2/3\n    :"))
    if user == 3:
        check()
    elif user == 1:
        order()    
    elif user == 2:
        check_order()
    elif user == 4:
        price()      
    
main()    