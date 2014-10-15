'''
Created on Aug 14, 2014

@author: Max Ruiz
'''
import MovementBank as mvbk
import sys
'''
import inspect, re

def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)
'''
genRoutine = mvbk.genericRoutine
state = 0
currentRoutine = genRoutine
mvbk.saveNewRoutine(genRoutine)
appLoop = 1

while appLoop == 1:
    if state is 0:
        print("Please select what to do by entering a number from 1 to 9")
        print("=========================================================")
        print("1) Display Current Routine")
        print("2) Show and Select Available Routines")
        print("3) List Movements")
        print("4) Add Movement")
        print("5) Remove Movement")
        print("6) Form New Routine")
        print("7) Delete Routine")
        print("8) Print to text file")
        print("9) Exit Application")

        answer = input(">>>>> ")
        answer = int(answer)

        while(answer > 9):
            print("Response must be a number between 1 and 9")
            answer = input(">>>>> ")
            answer = int(answer)

        if answer is 1:
            state = 1
        elif answer is 2:
            state = 2
        elif answer is 3:
            state = 3
        elif answer is 4:
            state = 4
        elif answer is 5:
            state = 5
        elif answer is 6:
            state = 6
        elif answer is 7:
            state = 7
        elif answer is 8:
            state = 8
        elif answer is 9:
            state = 9



    if state is 1:
        currentRoutine.listRoutine()
        state = 0

    if state is 2:
        rtnList = mvbk.listAvailableRoutines()
        print("Available Routines")
        print("==================")
        for keys in range(len(rtnList)):
            print(rtnList[keys])
        setRoute = input("\nEnter which routine you want to check out or type \"e\" to exit: ")
        if setRoute == "e":
            state = 0
        else:
            currentRoutine = mvbk.returnRoutine(setRoute)
            state = 0

    if state is 3:
        currentRoutine.listMovements()
        state = 0

    if state is 4:
        currentRoutine.listBodyParts()
        BP = input("Please select from the above body parts to add movement to: ")
        print("\n")
        newMvmnt = input("Please enter name of new movement: ")
        print("\n")
        currentRoutine.addMovement(BP, newMvmnt)
        state = 0

    if state is 5:
        currentRoutine.listBodyParts()
        BP = input("Please select from the above body parts to remove movement from: ")
        print("\n")
        newMvmnt = input("Please enter name of movement to remove: ")
        print("\n")
        currentRoutine.deleteMovement(BP, newMvmnt)
        state = 0

    if state is 6:
        buildRoutineLoop = 1
        print("Hello, you will be building a Workout Routine, here is how it works:")
        print("You will be asked to specify the body part it will work, the movement name, the number of set and reps.")
        print("You then have a chance to continue entering moves until you are done.")
        print("There are also two extra options, one for exiting without saving, and one for exiting and saving.\n")
        newRtnName = input("Please enter name of new routine: ")
        tempRoutine = mvbk.Routine(newRtnName)
        while buildRoutineLoop == 1:
            nextState = input("Enter \"save\" to save and exit; enter \"exit\" to exit without saving; enter anything else to continue: ")
            if nextState == "save":
                try:
                    mvbk.saveNewRoutine(tempRoutine)
                    print("{0} was successfully saved!".format(tempRoutine.returnName()))
                except:
                    print("There was nothing to save")
                state = 0
                buildRoutineLoop = 0
            elif nextState == "exit":
                state = 0
                buildRoutineLoop = 0
            else:
                tempRoutine.listBodyParts()
                BP = input("Please select from the above body parts to add movement to: ")
                print("\n")
                tempRoutine.listMovements()
                newMvmnt = input("Please enter name of movement list above or enter new movement: ")
                print("\n")
                sets = input("Please enter number of sets for this movement: ")
                sets = int(sets)
                print("\n")
                reps = input("Please enter number of reps for this movement: ")
                print("\n")
                tempRoutine.buildRoutine(BP, newMvmnt, sets, reps)



    if state is 7:
        rtnList = mvbk.listAvailableRoutines()
        print("Available Routines")
        print("==================")
        for keys in range(len(rtnList)):
            print(rtnList[keys])
        rName = input("Please enter name of routine above to delete: ")
        mvbk.deleteRoutine(rName)
        state = 0

    if state is 8:
        fName = input("Please name the text file with which your routine will be printed in: ")
        rtnList = mvbk.listAvailableRoutines()
        print("Available Routines")
        print("==================")
        for keys in range(len(rtnList)):
            print(rtnList[keys])
        rName = input("Please enter name of routine above to print to text file: ")
        rInstance = mvbk.returnRoutine(rName)
        mvbk.printToTextFile(fName, rInstance)
        state = 0

    if state is 9:
        print("Exiting Application")
        appLoop = 0
        sys.exit
