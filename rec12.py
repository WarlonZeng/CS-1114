''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec12.py

assume: files to work with/going to make

'''

from __future__ import print_function

import os.path


#Part 1


def getInputFileName():
    fileNameInput = './' + raw_input('File name to process?: ') + '.txt'
    doesFileExist = os.path.exists(fileNameInput)
    while doesFileExist == False:
        print('File does not exist. Try again.')
        fileNameInput = './' + raw_input('File name to process?: ') +'.txt'
    fileObject = open( fileNameInput, 'r+' )
    return fileObject
            

def getOutputFileName():
    fileNameOutput = raw_input('File name to output?: ') + '.txt'
    confirmOverwrite = raw_input('Are you sure you want to wipe out preexistent file? Type Yes or No: ')
    if confirmOverwrite == 'Yes':
        fileObjectOutput = open( fileNameOutput, 'w' )
    return fileObjectOutput, fileNameOutput

    
def getBetweenString():
    betweenString = raw_input('What is your between string?: ')
    return betweenString


def betweenStringBetweenWords( fileObject, fileObjectOutput, betweenString ):
    'replace space with string'
    for line in fileObject:
        fileObjectOutput.write(line.replace(' ', betweenString))
    fileObject.close()
    fileObjectOutput.close()
    return fileObjectOutput


#Part 2


def restoreBetweenStringBetweenWords( fileNameOutput ):
    restore = raw_input('Do you want to restore the process? Type Yes or No: ')
    if restore == 'Yes':
        fileObject = open( fileNameOutput, 'r+' )
        fileNameOutput = raw_input('File name to output?: ') + '.txt'
        fileObjectOutput = open( fileNameOutput, 'w' )
        betweenString = getBetweenString()
        for line in fileObject:
            fileObjectOutput.write(line.replace(betweenString, ' ')) # replace string with space
        fileObject.close()
        fileObjectOutput.close()
        return fileObjectOutput


def part1and2():
    fileObject = getInputFileName()
    fileObjectOutput, fileNameOutput = getOutputFileName()
    betweenString = getBetweenString()
    betweenStringBetweenWords( fileObject, fileObjectOutput, betweenString )
    restoreBetweenStringBetweenWords( fileNameOutput )


#Part 3


def microprocessor( fileObject, fileObjectOutput ):
    newSetIndicator = '*****'
    accumulator = 0
    divideAccumulator = 0
    dataList = []
    dataFromText = []
    line = 1
    for i in fileObject:
        dataFromText.append(i.strip())
    while line <= len(dataFromText):
        if dataFromText[line] == newSetIndicator:
            if accumulator == 0 and divideAccumulator!= 0:
                dataList.append( [dataFromText[line-divideAccumulator-1] + ': ', str(0.0)] )
            else:
                dataList.append( [dataFromText[line-divideAccumulator-1] + ': ', str(accumulator/divideAccumulator)] )
                accumulator = 0
                divideAccumulator = 0
            line += 2
        if line > len(dataFromText):
            break
        if dataFromText[line] == newSetIndicator:
            dataList.append( [dataFromText[line-1] + ': ', str(-1e+12)] )
            line += 2
        accumulator += float(dataFromText[line])
        divideAccumulator += 1
        line += 1
    for lines in range(len(dataList)):
        fileObjectOutput.writelines(dataList[lines])
        fileObjectOutput.writelines('\n')
    fileObjectOutput.close()
    return dataList
    

#Part 4


def invalidProjects( dataList ):
    rejects = []
    for j in range(len(dataList)):
        if '7' not in dataList[j][0]:
            rejects.append(dataList[j])
    fileObjectRejects = open( 'rejects.txt', 'w' )
    for l in range(len(rejects)):
        fileObjectRejects.writelines(rejects[l])
        fileObjectRejects.writelines('\n')
    fileObjectRejects.close()


def part3and4():
    fileObject = getInputFileName()
    fileObjectOutput, fileNameOutput = getOutputFileName()
    dataList = microprocessor( fileObject, fileObjectOutput )
    invalidProjects( dataList )


def main():
    part1and2()
    print('Now doing part 3 and 4')
    part3and4()
