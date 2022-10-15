#import math for sqaure root function to solve in the distance formula
import math

#State your input and output files
inputFile = 'Problem1_IOFiles/Problem1_Input.txt'
outputFile = 'Problem1_IOFiles/Problem1_Output.txt'

#Takes the file as an input and stores the read file in a list.
def readFile(fileName):
    fileItems = []
    myFile = open(fileName, "r")
    #Reding each individual line
    while myFile:
        line = myFile.readline()
        if line == "":
            break
        #Spliting and appending each line to a list
        splitLine = line.split(' ')
        fileItems.append(splitLine)
    myFile.close()
    #Coverting all values from string to floats
    for n in range(0, len(fileItems)):
      for i in range(0, len(fileItems[n])):
        fileItems[n][i] = float(fileItems[n][i])
    return fileItems

#Lists all possible points on the given cartesian grid
def gridPoints(xPoints, yPoints, Dx, Dy):
    cordinates = []
    for xValue in range(0, xPoints):
        for yValue in range(0, yPoints):
            #Appends all points to a list
            cordinates.append([xValue*Dx, yValue*Dy])
    return cordinates
#Takes each point on the cartesian grid and compares the distance between it and the points given as input
def closestPoint(numOfPoints, fileItemsList, cordinateList):
    closestPoint = []
    #Cycles through each point in the given input and compares it to each point on the cartesian grid
    while numOfPoints > 0:
        distances = []
        Point = numOfPoints
        x_1 = fileItemsList[Point][0]
        y_1 = fileItemsList[Point][1]
        for cordinate in range(0, len(cordinateList)):
            x_2 = cordinateList[cordinate][0]
            y_2 = cordinateList[cordinate][1]
            #Distance Formula
            dist = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
            #Appends all disatances to a list
            distances.append(dist)
        #Finds the least value in the list of distances, and compares its index, to the index of the points on the cartesian grid to find the closest point to the given point
        #Finally it appends this value to a new list
        closestPoint.append(cordinateList[distances.index(min(distances))])
        #Clears the distances list so it can be reused for the next point in the iteration
        distances.clear()
        numOfPoints -= 1
    #Reverses list so it list from points 1-3 instead of points 3-1.
    closestPoint.reverse()
    return closestPoint
#Scales the point to integer values by dividing by the grid accuracies
def finalValues(closestPointValues, Dx, Dy):
    for point in range(0, len(closestPointValues)):
        closestPointValues[point][0] /= Dx
        closestPointValues[point][0] = int(closestPointValues[point][0])
        closestPointValues[point][1] /= Dy
        closestPointValues[point][1] = int(closestPointValues[point][1])
    return closestPointValues
#Write the final point to the output file
def writeToOutput(listOfValues):
    with open(outputFile, "w") as output:
        #Converts all integer values to strings
        for l in range(0, len(listOfValues)):
            for a in range(0, len(listOfValues[l])):
                listOfValues[l][a] = str(listOfValues[l][a])
        #Joins together points using a space in between and prints each point on a newline
        for index in range(0, len(listOfValues)):
            result = " ".join(listOfValues[index])
            output.write(result + '\n')
#Calling the main function
def main():
    #Calling readFile function and storing the list in a variable
    fileItemsList = readFile(inputFile)

    #Storing important values from the list
    #N
    xPoints = int(fileItemsList[0][0])
    #M
    yPoints = int(fileItemsList[0][1])
    #Dx
    Dx = fileItemsList[0][2]
    #Dy
    Dy = fileItemsList[0][3]
    #K
    numOfPoints = int(fileItemsList[0][4])

    #Calling gridPoints function and storing the list returned as a variable
    cordinateList = gridPoints(xPoints, yPoints, Dx, Dy)

    #Calling closestPoint function and storing the list returned as a variable
    closestPointValues = closestPoint(numOfPoints, fileItemsList, cordinateList)

    #Calling finalValues function and storing the list returned as a variable
    closestPointValuesList = finalValues(closestPointValues, Dx, Dy)

    #Calling writeToOutput function to write final output to the output file
    writeToOutput(closestPointValues)

#Triggers the main function
if __name__ == "__main__":
    main()