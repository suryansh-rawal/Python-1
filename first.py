import random 
print("Guess a  Number Between 1 to 9 :")
number = random.randint(1,9)
Chances=0
while Chances < 5 :
        Guess = int(input("Guess the Number : "))
        if number==Guess:
                print("Congo!! You have Guessed Righ ;)")
                break 
        elif Guess <number :
                print("Your Guess is less then expected !!", Guess)
                
        else :
                print("Yur Guess is too high than expected !!", Guess)

        Chances =Chances+1




                        



        




        

       

            

