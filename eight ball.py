import random

def eightball(choice):
    if choice==1:
        print("Yes")
    elif choice==2:
        print("no")
    elif choice==3:
        print("Dougt it")
    elif choice==4:
         print("Mabybe")
    elif choice==5:
        print("Defielif")
    else:
        print("I have no idea")
        
def main():
    randomNumber = random.randint(1, 6)
    eightball(randomNumber)
main()
