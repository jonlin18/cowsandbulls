import random
#initialize some vars
guess = 0
cow = 0
bull = 0
target = str(random.randint(0000, 9999)).zfill(4)


def check_cows(inp):
    """
    Check how many cows and bulls there are based 
    on number of correct numbers in right posision
    """
    if type(inp) == int:
        if 0 <= inp <= 9999:
            global cow
            global bull
            s = str(inp).zfill(4)
            for i, digit in enumerate(s):
          
                if target[i] == digit:
                    cow += 1
                else:
                    bull +=1
            print("you have",cow,"cows and",bull,"bulls! \n")
        else:
            print("you need to enter a valid number") 
        
            
        
        
#make user input a number and make them keep guessing   
while cow != 4:  
    cow = 0
    bull = 0
    try:
        x = int(input("enter your guess between 0000 to 9999: "))
        check_cows(x)
        guess += 1
    except ValueError:
        print('you need to enter a valid number')
    

print("you have correctly guessed", target, "in",guess, "tries")
    