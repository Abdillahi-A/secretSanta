import random
import copy

def read_csv():
    # reads the csv and returns a list of names and shuffled list of names
    with open('names.csv') as f:
        lisOfNames = f.read().split('\n')
    
    shuffledListofNames = copy.copy(lisOfNames)
    random.shuffle(shuffledListofNames)

    return lisOfNames, shuffledListofNames

def index_check(lisOfNames, shuffledListofNames):
    # checks to make sure that last person to be allocated isn't left with their own name.
    if lisOfNames[-1] == shuffledListofNames[0]:
        shuffledListofNames[0], shuffledListofNames[1] = shuffledListofNames[1], shuffledListofNames[0]
        
def doAllocations(lisOfNames, shuffledListofNames):
    index_check(lisOfNames, shuffledListofNames)
    pairings = []

    for name in lisOfNames:
        if name == shuffledListofNames[-1]:
            pairings.append((name, shuffledListofNames.pop(-2)))
        else:
            pairings.append((name, shuffledListofNames.pop(-1)))
    
    return pairings

def main():
    lisOfNames, shuffledListofNames= read_csv()
    pairings = doAllocations(lisOfNames, shuffledListofNames)
    print(pairings)

main()