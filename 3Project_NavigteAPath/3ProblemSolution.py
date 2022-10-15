'''
Approach: In the function borderpoints we find all the point on the border of the polyons given to us.


'''

#State your input and output files
inputFile = 'Problem3_IOFiles/Problem3_Input.txt'
outputFile = 'Problem3_IOFiles/Problem3_Output.txt'

#Takes the file as an input and stores the read file in a list.
def readFile(fileName):
    fileItems = []
    myFile = open(fileName, "r")

    line = myFile.readline()


    splitLine = line.split(' ')
    fileItems.append(splitLine)

    waypoints = float(fileItems[0][2])
    waypointsList = []

    obstacles = int(fileItems[0][3])
    obstaclesList = []


    while waypoints > 0:
        line = myFile.readline()
        if line == "":
            break
        splitLine = line.split(' ')
        waypointsList.append(splitLine)
        waypoints -= 1

    while obstacles > 0:
        object = []
        object.clear()
        line = myFile.readline()
        if line == "":
            break
        splitLine = line.split(' ')
        if len(splitLine) == 1:
            object.append([splitLine[0]])
            obstacleCordinates = int(object[0][0])
            while obstacleCordinates > 0:
                line = myFile.readline()
                if line == "":
                    break
                splitLine = line.split(' ')
                object.append([splitLine[0], splitLine[1]])
                obstacleCordinates -= 1
        obstacles -= 1
        obstaclesList.append(object)

    for a in range(0, len(fileItems)):
      for b in range(0, len(fileItems[a])):
        fileItems[a][b] = int(fileItems[a][b])

    for c in range(0, len(waypointsList)):
      for d in range(0, len(waypointsList[c])):
        waypointsList[c][d] = int(waypointsList[c][d])

    for e in range(0, len(obstaclesList)):
        for f in range(0, len(obstaclesList[e])):
            for g in range(0, len(obstaclesList[e][f])):
                obstaclesList[e][f][g] = int(obstaclesList[e][f][g])

    fileItems.append((waypointsList))
    fileItems.append(obstaclesList)

    myFile.close()
    return fileItems

def borderPoints(fileItemsList, polygon, max_xValue, max_yValue, totalWaypoints):
    pointsOnBorder = []
    while totalWaypoints > 0:
        startingWaypointYValue = fileItemsList[1][0][0]
        startingWaypointYValue = fileItemsList[1][0][1]
        endingWaypointXValue = fileItemsList[1][0][0]
        endingWaypointyValue = fileItemsList[1][0][0]
        xStep = fileItemsList[1][0][0]
        yStep = fileItemsList[1][0][1]



    '''
     for x in range(0, polygon):
    for y in range(0, len(fileItemsList[2][x])):
        for z in range(0, len(fileItemsList[2][x][y])):
            print(fileItemsList[2][x][y][z])   
    '''




def main():
    #Calling readFile function and storing the list in a variable
    fileItemsList = readFile(inputFile)

    max_xValue = fileItemsList[0][0]
    max_yValue = fileItemsList[0][1]
    totalWaypoints = fileItemsList[0][2]
    polygon = fileItemsList[0][3]

    borderPoints(fileItemsList, polygon, max_xValue, max_yValue, totalWaypoints)

#Triggers the main function
if __name__ == "__main__":
    main()