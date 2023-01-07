import random
def GetNumber():
    num = random.randint(1,6)
    if num == 1:
        print("[-------]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[-------]")
    if num == 2:
        print("[-------]")
        print("[     0 ]")
        print("[       ]")
        print("[ 0     ]")
        print("[-------]")
    if num == 3:
        print("[-------]")
        print("[ 0     ]")
        print("[   0   ]")
        print("[     0 ]")
        print("[-------]")
    if num == 4:
        print("[-------]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[-------]")
    if num == 5:
        print("[-------]")
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
        print("[-------]")
    if num == 6:
        print("[-------]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[-------]")


on = True
while on:
    run = input("To get a random number type 'YES':\n")
    if run == "YES":
        GetNumber()
        
    else:
        on = False
