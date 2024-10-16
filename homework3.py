import random
import string

#fitness test
def fitnessTest(parent, desiredSeries):
    #I need the desired character series and the parent
    fitOfParent = ""
    #a for loop to check to see what values are in the desired series
    for i in range(len(parent)):
        if parent[i] == desiredSeries[i]:
            fitOfParent += parent[i]
        else:
            fitOfParent += "µ"
    return fitOfParent
def listOfBestFit(parentFit, parent):
    fitnessScore = 0
    placeHolder = 0
    sortedFitList = []
    for x in range(len(parent)):
        for y in range(len(parentFit[x])):
            if parentFit[x][y] == 'µ':
                parentFit[x][y] == ''
    for i in range(len(parent)):
        for j in range(len(parent)):
            if len(parentFit[j]) > fitnessScore:
                fitnessScore = len(parentFit)
                placeHolder = i
        sortedFitList.append(parent[placeHolder])
        parent[placeHolder] = ''
        parentFit[placeHolder] = ''
        placeHolder = 0
        fitnessScore = 0
    return sortedFitList
#gene splicing
def splicer(parent1, parent2, string, mutationRate):
    splicedChild = []
    #need to see what is fit 
    fitParent1 = fitnessTest(parent1, string)
    for i in range(len(string)):
        splicedChild.append('')
    for j in range(len(fitParent1)):
        if fitParent1[j] != 'µ':
            splicedChild[j] = fitParent1[j]
    for k in range(len(parent2)):
        if splicedChild[k] == '':
            if (random.random() < mutationRate):
                if (ord(parent2[k]) == 255):
                    splicedChild[k] = chr(0)
                else:
                    splicedChild[k] = chr(ord(parent2[k])+1)
            else:
                splicedChild[k] = parent2[k]
    return splicedChild
#survival rate

#choosing parents

#elitism

#when to stop? When the desired string is reached

def main():
    #generation number
    generation = 0
    #I need a file to be inputed
    fileName = input("Please input a file to open with the file extension (.txt): ")
    file = open(fileName, "r")
    desiredString = file.read().replace("\n", " ")
    file.close()
    #mutation rate
    mutationPercentage = 99
    mutationRate = .99
    #pop size
    popSize = 2
    #parents and parent fitness keeper
    parent = []
    parentFit = []
    #I need the size of the parents
    for size in range(0, popSize, 1):
        newString = ''
        for i in range(len(desiredString)):
            newString += chr(random.randint(0,255))
        parent.append(''.join(newString))
    for i in range(len(parent)):
        parentFit.append(fitnessTest(parent[i], desiredString))
    organizedList = listOfBestFit(parentFit, parent)
    #now I will take the highest fit parent and the lowest fit parent and splice them
    #The most fit parent will first have their characters added and then the second parent
    #will fill in the rest
    while (organizedList[0] != desiredString):
        #prints the results so far
        print(organizedList[0])
        howFit = 0
        for i in range(len(organizedList[0])):
            if organizedList[0][i] == desiredString[i]:
                howFit +=1
        print("Fitness Score: ", howFit)
        generation+=1
        print("Generation: ", generation)
        #splices all of the children
        children = []
        for i in range(len(organizedList)):
            if (len(organizedList)-i) > 0:
                spot = len(organizedList)-i-1
            else:
                spot = (i-len(organizedList)-1) * -1
            newChild = splicer(organizedList[i], organizedList[spot], desiredString, mutationRate)
            newChild = ''.join(newChild)
            children.append(newChild)
        #makes a new organized list
        for i in range(len(children)):
            parentFit[i] = fitnessTest(children[i], desiredString)
        organizedList = listOfBestFit(parentFit, children)
    #repeat the printing sequence for the last iteration
    print(organizedList[0])
    howFit = 0
    for i in range(len(organizedList[0])):
        if organizedList[0][i] == desiredString[i]:
            howFit +=1
    print("Fitness Score: ", howFit)
    generation+=1
    print("Generation: ", generation)
main()