'''
Created on Aug 14, 2014

@author: Max Ruiz
'''
import shelve, re
workOutRoutines = "Work_Out_Routines"



class Routine(object):
    movements = {  'Shoulders' : ['Side Arm Raises', 'Front arm raises', 'Overhead Presses', 'Shrugs']
                  , 'Biceps' : ['Curls', 'Hammer Curls', 'Preacher Curls', 'Inclined Curls']
                  , 'Triceps' : ['Overhead Tri Presses', 'Bench Tri Presses', 'Bent Over Tri raises', 'Diamond Pushups']
                  , 'Forearms' : ['Dead Hang', 'Reverse Curls', 'Dumbell Squeezes']
                  , 'Back' : ['Pull Ups', 'Reverse Flys', 'Beach Balls', 'Bent Over Rows']
                  , 'Chest' : ['Pushups', 'Flys', 'Chest Press', 'Bench Press', 'Inclined Chest Press']
                  , 'Core' : ['Crunches', 'Roman Crunches', 'Leg Raises', 'Hanging Leg Raises', 'Side core lift']
                  , 'Legs' : ['Squats', 'Wall sit', 'Calf Raises', 'Lunges', 'One Leg Squats']}

    def __init__(self, rName):

        self.myRoutine = {  'Shoulders' : {}
                          , 'Biceps' : {}
                          , 'Triceps' : {}
                          , 'Forearms' : {}
                          , 'Back' : {}
                          , 'Chest' : {}
                          , 'Core' : {}
                          , 'Legs' : {}}
        self.rName = rName


    def addMovement(self, bodyPart, movement):
        if isinstance(bodyPart, str) and isinstance(movement, str):
            try:
                self.movements[bodyPart].append(movement)
                print("{0} : {1} added successfully!".format(bodyPart, movement))
            except:
                print("{0} was not found in list of body parts to exercise".format(bodyPart))


    def deleteMovement(self, bodyPart, movement):
        if isinstance(bodyPart, str) and isinstance(movement, str):
            try:
                self.movements[bodyPart].remove(movement)
                del self.myRoutine[bodyPart]
                rtnStr = "{0} : {1} removed successfully!".format(bodyPart, movement)
                print(rtnStr)
            except:
                failStr = "Either {0} or {1} does not exist".format(bodyPart, movement)
                print(failStr)

    def listMovements(self):
        for keys in self.movements.keys():
            print(keys, "\n==========")
            for x in range(len(self.movements[keys])):
                print(self.movements[keys][x])
            print("-----------")

    def buildRoutine(self, bodyPart, movement, sets, reps):
        if(isinstance(bodyPart, str) and isinstance(movement, str)):
            try:
                self.myRoutine[bodyPart][movement] = [sets, reps]
            except:
                print("There was an issue with your entry. It was most likely cause by a mispelling of body part")


    def listRoutine(self):
        i = 0
        for bp in self.myRoutine.keys():
            i = i + 1
            print("===", bp, "===")
            for lifts in self.myRoutine[bp].keys():
                print(">", "{0} => Sets: {1}, Reps: {2}".format(lifts, self.myRoutine[bp][lifts][0], self.myRoutine[bp][lifts][1]))

    def stringRoutine(self):
        i = 0
        str = ""
        for bp in self.myRoutine.keys():
            i = i + 1
            str = str + "===" + bp + "===\n"
            for lifts in self.myRoutine[bp].keys():
                str = str + "> {0} => Sets: + {1}, Reps: {2}\n".format(lifts, self.myRoutine[bp][lifts][0], self.myRoutine[bp][lifts][1])
        return str

    def returnName(self):
        return self.rName

    def listBodyParts(self):
        print("Body Parts to exercise")
        print("======================")
        for keys in self.movements.keys():
            print(keys)
        print("\n")



genericRoutine = Routine("GenericRoutine")

genericRoutine.buildRoutine("Shoulders", "Side Arm Raises", 2, 11)
genericRoutine.buildRoutine("Shoulders", "Overhead Presses", 2, 9)
genericRoutine.buildRoutine("Shoulders", "Front Arm Raises", 2, 11)
genericRoutine.buildRoutine("Shoulders", "Shrugs", 3, 9)

genericRoutine.buildRoutine("Biceps", "Curls", 3, 11)
genericRoutine.buildRoutine("Biceps", "Hammer Curls", 2, 9)
genericRoutine.buildRoutine("Biceps", "Preacher Curls", 2, 13)
genericRoutine.buildRoutine("Biceps", "Inclined", 2, 9)

genericRoutine.buildRoutine("Triceps", "Overhead Tri Presses", 3, 11)
genericRoutine.buildRoutine("Triceps", "Diamond Pushups", 2, 21)
genericRoutine.buildRoutine("Triceps", "Bench Tri Presses", 2, 9)
genericRoutine.buildRoutine("Triceps", "Bent Over Tri raises", 2, 9)

genericRoutine.buildRoutine("Forearms", "Dead Hang", 2, 2)
genericRoutine.buildRoutine("Forearms", "Reverse Curls", 2, 11)
genericRoutine.buildRoutine("Forearms", "Dumbell Squeezes", 2, 21)

genericRoutine.buildRoutine("Back", "Pull Ups", 3, 13)
genericRoutine.buildRoutine("Back", "Reverse Flys", 3, 9)
genericRoutine.buildRoutine("Back", "Beach Balls", 2, 7)
genericRoutine.buildRoutine("Back", "Bent Over Rows", 2, 15)

genericRoutine.buildRoutine("Chest", "Chest Press", 2, 13)
genericRoutine.buildRoutine("Chest", "Flys", 2, 15)
genericRoutine.buildRoutine("Chest", "Bench Press", 2, 7)
genericRoutine.buildRoutine("Chest", "Inclined Chest Press", 2, 7)
genericRoutine.buildRoutine("Chest", "Pushups", 3, 31)

genericRoutine.buildRoutine("Core", "Crunches", 3, 51)
genericRoutine.buildRoutine("Core", "Side Core Lift", 2, 25)
genericRoutine.buildRoutine("Core", "Roman Crunches", 2, 31)
genericRoutine.buildRoutine("Core", "Leg Raises", 3, 25)
genericRoutine.buildRoutine("Core", "Hanging Leg Raises", 2, 13)

genericRoutine.buildRoutine("Legs", "Squats", 2, 11)
genericRoutine.buildRoutine("Legs", "Calf Raises", 2, 25)
genericRoutine.buildRoutine("Legs", "Wall Sit", 2, 1)
genericRoutine.buildRoutine("Legs", "Lunges", 3, 13)
genericRoutine.buildRoutine("Legs", "One Leg Squats", 2, 7)

def saveNewRoutine(rInstance):
    file = shelve.open(workOutRoutines)
    file[rInstance.returnName()] = rInstance
    file.close()

def listAvailableRoutines():
    rList = list()
    file = shelve.open(workOutRoutines)
    for keys in file.keys():
        rList.append(keys)
    file.close()
    return rList

def returnRoutine(rName):
    rName = str(rName)
    file = shelve.open(workOutRoutines)
    try:
        currentRoutine = file[rName]
        print("Routine set as: ", currentRoutine.returnName())
        return currentRoutine
    except:
        print("No routine named \"{0}\" found, current routine set to genericRoutine".format(rName))
        return file[genericRoutine.returnName()]
    file.close()

def deleteRoutine(rName):
    file = shelve.open(workOutRoutines)
    try:
        del file[rName]
        print("Routine: {0} was deleted successfully!".format(rName))
    except:
        print("Routine: {0} was not found.".format(rName))
    file.close()

def printToTextFile(fName, rInstance):
    fExt = re.findall(r"(\.txt)", fName)
    if not fExt:
        fName1 = fName + ".txt"
        f = open(fName1, 'w')
    else:
        f = open(fName, 'w')
    f.write(rInstance.stringRoutine())
    f.close()

