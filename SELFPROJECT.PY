import random

class Randomroll:
    def rolling(roll,start_range,end_range):
        if(int(start_range)>0 and int(end_range)>0 and int(end_range)>=int(start_range)):
            num_rolled=random.randint(start_range,end_range)
            return num_rolled
        else:
            return "invalid try again"

if __name__ == "__main__":
    play=Randomroll()
    i=True
    while(i):
        print("Welcome to the Dice Rolling simulator ")
        Play_again=input("TO START: Enter any alphabet ; TO QUIT: Enter 'Q' ")
        if(Play_again.upper() != 'Q' ):
            a,b = input(" Enter the Range: ").split()
            x=(play.rolling(int(a),int(b)))
            print(x)    
        else:
            i=False
            print(" Thankyou for Playing :) ")    