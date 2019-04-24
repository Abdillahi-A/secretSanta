import random
import copy

def read_csv():
    # reads the csv and returns a list of names and shuffled list of names
    with open('names.csv') as f:
        listOfNames = f.read().split('\n')
    
    shuffledListOfNames = copy.copy(listOfNames)
    random.shuffle(shuffledListOfNames)

    return listOfNames, shuffledListOfNames

def index_check(listOfNames, shuffledListOfNames):
    # checks to make sure that last person to be allocated isn't left with their own name.
    if listOfNames[-1] == shuffledListOfNames[0]:
        shuffledListOfNames[0], shuffledListOfNames[1] = shuffledListOfNames[1], shuffledListOfNames[0]
        
def doAllocations(listOfNames, shuffledListOfNames):
    index_check(listOfNames, shuffledListOfNames)
    pairingsDict = {}

    for name in listOfNames:
        if name == shuffledListOfNames[-1]:
            pairingsDict[name] = shuffledListOfNames.pop(-2)
        else:
            pairingsDict[name] = shuffledListOfNames.pop(-1)
    
    return pairingsDict

def main():
    listOfNames, shuffledListOfNames= read_csv()
    pairingsDict = doAllocations(listOfNames, shuffledListOfNames)
    print(pairingsDict)

main()
