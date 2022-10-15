#Import math library to calculate trigonometric values
import math

#State your input and output files
inputFile = 'Problem2_IOFiles/Problem2_Input.txt'
outputFile = 'Problem2_IOFiles/Problem2_Output.txt'

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

#Find the required altitude of the drone
def uavAltitude(length, verticalAOV):
    #Find the height using half the length divided by the tan of half of the verticalAOV to find the height
    #Also round to the nearest tenth
    return round((length/2)/(math.tan((verticalAOV/2)*(math.pi/180))), 1)

#Find the width of the image feed after alititude adjustment
def widthOfImageFeed(uavFinalAltitude, horizontalAOV):
    #Finds twice the product of half the altitude and the tan of half the horizontalAOV
    #This equals to the width
    return 2*(round(uavFinalAltitude*(math.tan((horizontalAOV/2)*(math.pi/180))), 1))

#Find the roll of the camera in degrees
def rollOfCamera(uavFinalAltitude, y):
    #To find the roll just take twice the atan of half the y coordinate divided by the altitude of the drone
    finalRoll = round(2*((math.atan((abs(y)/2) /uavFinalAltitude))*(180/math.pi)), 1)
    #If the y coordinate is less tha 0 this means that the angle is positive and vice versa
    if y <= 0:
        return finalRoll
    else:
        return -(finalRoll)

#Find the pitch of the camera in degrees
def pitchOfCamera(uavFinalAltitude, x):
    #To find the pitch just take twice the atan of half the x coordinate divided by the altitude of the drone
    finalPitch = round(2*((math.atan((abs(x)/2) /uavFinalAltitude))*(180/math.pi)), 1)
    #If the x coordinate is greater tha 0 this means that the angle is positive and vice versa
    if x >= 0:
        return finalPitch
    else:
        return -(finalPitch)

#Print output list into the output file
def sendToOutput(fileContent):
    with open(outputFile, "w") as output:
        #Iterates through each element and prints them individually with a space
        for z in range(0, len(fileContent)):
            output.write(str(fileContent[z]) + ' ')

def main():
    #Calling readFile function and storing the list in a variable
    fileItemsList = readFile(inputFile)

    #Storing important values from the list
    #H
    horizontalAOV = fileItemsList[0][0]
    #V
    verticalAOV = fileItemsList[0][1]
    #L
    length = fileItemsList[0][2]
    #X
    x = fileItemsList[0][3]
    #Y
    y = fileItemsList[0][4]

    uavFinalAltitude = uavAltitude(length, verticalAOV)

    width = widthOfImageFeed(uavFinalAltitude, horizontalAOV)

    roll = rollOfCamera(uavFinalAltitude, y)

    pitch = pitchOfCamera(uavFinalAltitude, x)

    output = [uavFinalAltitude, width, roll, pitch]

    sendToOutput(output)

#Triggers the main function
if __name__ == "__main__":
    main()