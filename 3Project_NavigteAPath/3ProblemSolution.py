'''
Approach: In the function "borderPoints" we find all the points on the border of the polygons given to us. After we find
all points existing within the polygon. To do this we iterate between all points from the first point to all the points
existing on the perimeter of the polygon. After we take the midpoints of all these points and if any are coordinates
that are whole numbers, they will be accepted as points existing within the polygon. Since this will not find all the
points existing with the polygon, we can repeat these steps again, including the new points each time, to find the
remaining points. We can finally stop finding points when no new points are being found. Finally, we store all the
points on the polygons we find into a list of "obstacles".

In the pathfinding portion, we first move the UAV from the first waypoint in every direction it can possibly take. We
then use the distance formula to find the distance between the step it took, and the next waypoint. The point with the
lowest distance to the next waypoint, which doesn't lie in the "obstacles" list we defined earlier, wins and gets to be
the next point the UAV will take. Repeat these steps until you arrive and the next waypoint. Repeat these steps again
but take the 2nd waypoint as the starting point and the 3rd waypoint as the destination. After repeating this with the
number of waypoints you received(4 in the example) store all points taken into a list and output them into the output
file using the write command.
'''

#State your input and output files
inputFile = 'Problem3_IOFiles/Problem3_Input.txt'
outputFile = 'Problem3_IOFiles/Problem3_Output.txt'

#Takes the file as an input and stores the read file in a list.
def readFile(fileName):
    fileItems = []
    #Opens input file
    myFile = open(fileName, "r")
    #Reads the file line by line and stores into a variable called line
    line = myFile.readline()

    #Split line into a list of string integers
    splitLine = line.split(' ')
    fileItems.append(splitLine)
    #Set variables as important values and define other lists
    waypoints = float(fileItems[0][2])
    waypointsList = []

    obstacles = int(fileItems[0][3])
    obstaclesList = []

    #Appends all waypoints to the waypoint list
    while waypoints > 0:
        line = myFile.readline()
        if line == "":
            break
        splitLine = line.split(' ')
        waypointsList.append(splitLine)
        waypoints -= 1
    #Appends all obstacles or vertices of the polygons into the obstacles list
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
    #The next three for loopes converts every list from string values to integer values
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
    #Appends the new lists to fileItems list
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