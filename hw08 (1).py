''' 
cs1114 

Submission: hw08

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

output two files for avg, 3 maxs, 3 mins of change.

Assume:

list given
'''


from __future__ import print_function


def getInputFileName():
    '''gets file from user input. opens in read and write mode; does not damage original file.'''
    fileNameInput = raw_input('File name to process?: ') + '.txt'
    fileObject = open( fileNameInput, 'r+' ) # r+ is safe; does not change original.
    return fileObject


def dataDecoder( fileObject ):
    '''store data from file into a new sexy list'''
    data = []
    i = 0
    for line in fileObject: # line is the actual string line of the file
        data.append(line)
        data[i] = data[i].replace('\t', ', ') # replace a with b. not a mutator.
        data[i] = data[i].replace('%\n', '')
        data[i] = data[i].split( ', ' ) # split is not a mutator. split can only split one matchstring at a time.
        i += 1
    return data


def outputFile1970to1990( avg, max3Change, min3Change, fileOutputName1970to1990 ):
    '''for 1970 to 1990 output file'''
    fileObjectOutput = open( fileOutputName1970to1990, 'w' )
    fileObjectOutput.write('1970-1990 Summary Report\n') # this part is semi-hardcoded
    fileObjectOutput.write('\n')
    fileObjectOutput.write('Average percent change over all: ' + str(avg) + '%\n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write(', '.join(max3Change))
    fileObjectOutput.write('\n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write('The three countries or regions with the largest change: \n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write(', '.join(min3Change))
    fileObjectOutput.write('\n')


def outputFile1990to2007( avg, max3Change, min3Change, fileOutputName1990to2007 ):
    '''for 1970 to 2007 output file'''
    fileObjectOutput = open( fileOutputName1990to2007, 'w' )
    fileObjectOutput.write('1990-2007 Summary Report\n') # this part is semi-hardcoded
    fileObjectOutput.write('\n')
    fileObjectOutput.write('Average percent change over all: ' + str(avg) + '%\n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write(', '.join(max3Change))
    fileObjectOutput.write('\n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write('The three countries or regions with the largest change: \n')
    fileObjectOutput.write('\n')
    fileObjectOutput.write(', '.join(min3Change))
    fileObjectOutput.write('\n')
    

def obtainAverage( data, period ):
    '''traditional way to get average'''
    count = 0
    accumulator = 0
    for i in range(1, len(data)):
        if data[i][1] == period:
            accumulator += float(data[i][2])
            count += 1
    avg = accumulator/count
    return avg, data


def largestChange( data, period ):
    '''what it is: triple checking algorithm for maximum comparison'''
    max1st = [0, 0]
    max2nd = [0, 0]
    max3rd = [0, 0]
    max3Change = []
    for i in range(1, len(data)):
        if data[i][1] == period:
            if abs(float(data[i][2])) > abs(float(max1st[1])): #[0-name, 1-number]
                max1st = [data[i][0], data[i][2]]
            if abs(float(data[i][2])) < abs(float(max1st[1])) and abs(float(data[i][2])) > abs(float(max2nd[1])):
                max2nd = [data[i][0], data[i][2]]
            if abs(float(data[i][2])) < abs(float(max2nd[1])) and abs(float(data[i][2])) > abs(float(max3rd[1])):
                max3rd = [data[i][0], data[i][2]]
    max3Change = [ max1st, max2nd, max3rd ]
    max3 = []
    for j in range(len(max3Change)): # just to make data look pretty
        max3.append(max3Change[j][0] + ' ' + '(' + max3Change[j][1] + '%' + ')')
    max3Change = max3 # i just want the name kept
    return max3Change, data


def smallestChange( data, period ):
    '''what it is: triple checking algorithm for minimum comparison'''
    min1st = [0, 999]
    min2nd = [0, 999]
    min3rd = [0, 999]
    min3Change = []
    for i in range(1, len(data)):
        if data[i][1] == period:
            if abs(float(data[i][2])) < abs(float(min1st[1])): #[0-name, 1-number]
                min1st = [data[i][0], data[i][2]]
            if abs(float(data[i][2])) > abs(float(min1st[1])) and abs(float(data[i][2])) < abs(float(min2nd[1])):
                min2nd = [data[i][0], data[i][2]]
            if abs(float(data[i][2])) > abs(float(min2nd[1])) and abs(float(data[i][2])) < abs(float(min3rd[1])):
                min3rd = [data[i][0], data[i][2]]
    min3Change = [  min1st, min2nd, min3rd ]
    min3 = []
    for j in range(len(min3Change)): # just to make data look pretty
        min3.append(min3Change[j][0] + ' ' + '(' + min3Change[j][1] + '%' + ')')
    min3Change = min3 # i just want the name kept
    return min3Change, data


def generateFile1970to1990():
    '''all in one kit to finish the 1970 to 1990 file'''
    fileObject = getInputFileName()
    data = dataDecoder( fileObject )
    avg, data = obtainAverage( data, timePeriod1970to1990 )
    max3Change, data = largestChange( data, timePeriod1970to1990 )
    min3Change, data = smallestChange( data, timePeriod1970to1990 )
    outputFile1970to1990( avg, max3Change, min3Change, fileOutputName1970to1990 )
    return data


def generateFile1990to2007( data ):
    '''all in one kit to finish the 1990 to 2007 file'''
    avg, data = obtainAverage( data, timePeriod1990to2007 )
    max3Change, data = largestChange( data, timePeriod1990to2007 )
    min3Change, data = smallestChange( data, timePeriod1990to2007 )
    outputFile1990to2007( avg, max3Change, min3Change, fileOutputName1990to2007 )


timePeriod1970to1990 = '1970-1990'
timePeriod1990to2007 = '1990-2007'
fileOutputName1970to1990 = '1970_1990_summary.txt'
fileOutputName1990to2007 = '1970_2007_summary.txt'


def main():
    '''main program, makes two output files'''
    data = generateFile1970to1990()
    generateFile1990to2007( data )

    
main()
