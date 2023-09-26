import os
import exScript

def clearScreen():
    os.system('cls||clear')

def startRun():
    clearScreen()
    print('---------------- Start Run ----------------\n')
    
def endRun():
    print('\n----------------  End Run  ----------------')

def printHeader(script):
    print (script)

def runEx():
    # Input value
    print("Please choose Exercise (use space to select Multi Exercises)")

    selected_Ex = input("Run exercise: ").split()

    print('\nCHECK SELECTED EXERCISE VALID OR NOT')

    for i, Ex in enumerate(selected_Ex):
        nameEx = "".join(["Ex_",'{:0>2}'.format(Ex)])
        
        if not(Ex.isdigit()) \
        or (int(Ex) not in range (1,101))  \
        or (nameEx not in dir(exScript)):
            print(f"Exercise {Ex}: INVALID")
            selected_Ex.pop(i)
            selected_Ex.insert(i, '*')
            print("Wrong Value!!!\nThe value must be the integer and in range 1 - 100 and the Ex must VALID\n")
        else: 
            print(f"Exercise {Ex}: VALID")
            selected_Ex.pop(i)
            selected_Ex.insert(i, nameEx)
    
    selected_Ex = list(filter(lambda a: a != '*', selected_Ex))

    for valid_Ex in selected_Ex:
        run_scripts(getattr(exScript, valid_Ex))
        # for Ex in dir(exScript):
        #     try:
        #         if valid_Ex == Ex:
        #             printHeader(Ex)
        #             catchErr(getattr(exScript,Ex))
        #             break
        #     except:
        #         continue

def run_scripts(func):
    try:
        ex = func()
        ex.execute()
        del ex
    except Exception as e:
        print(f"==> Error!: {e}",)

if __name__ == "__main__":
    print(__name__)
    clearScreen()
    runEx()