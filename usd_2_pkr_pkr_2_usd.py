def USD(a):
    return a * 279.7689  
    
def pkr(a):
    return a * 0.0036 
    
def logo():
    print('''
    OWNER  : AHMED_XD
    TOOL   : CURRENCY  CONVERTER
    VERSION: BASIC''')
    print("\n")
    print("[1] PKR TO USD")
    print("[2] USD TO PKR")
    hm = input(" enter number 1/2 : ")
    if hm == '1':
        a = int(input(" input value to convert pkr to USD: "))
        result = pkr(a)
        print(result)
    if hm == '2':
        a = int(input("enter value to convert USD to PKR: "))
        result = USD(a)
        print(result)
          
logo()   