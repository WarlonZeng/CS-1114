''' 
cs1114 

Submission: hw06

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

process manual input data lists

Assume:

transmissions 1 or more, prompt try again.

reject -232.00205 + 33.34, -232.00205 - 33.34;

yo i spent a lot of time on this man
'''



from __future__ import print_function



minValidTemperature = -232.00205 - 33.34
maxValidTemperature = -232.00205 + 33.34



def promptUser():
    'asks for a valid number of sets'
    numOfSets = int(raw_input('How many transmissions to process? '))
    while numOfSets < 1:
        numOfSets = int(raw_input('Sorry must be 1 or more. Try again: '))
    return numOfSets



def validTemperature(temperature):
    'determines what is valid range'
    validTemperature = (temperature > minValidTemperature and temperature < maxValidTemperature)
    return validTemperature



def dataStatsImmediate(temperatureSets, i, count, countAccepted):
    'finds the statistics for that index list of sets'
    print('')
    print('Data set ' + str(int(i)))
    print('Stats: ')
    if len(temperatureSets[i-1]) == 0:
        print('''Number of temperatures processed: 0
Percent rejected: 0%
Average temperature: Not applicable
Maximum temperature: Not applicable
Minimum temperature: Not applicable
              ''')
    else:
        percentRejected = ((count-countAccepted) / count) * 100
        averageTemperature = sum(temperatureSets[i-1]) / (countAccepted)
        maximumTemperature = max(temperatureSets[i-1])
        minimumTemperature = min(temperatureSets[i-1])
        print('Number of temperatures processed: ' + str(int(countAccepted)))
        print('Percent rejected: ' + str(percentRejected) + ' %')
        print('Average temperature: ' + str(averageTemperature))
        print('Maximum temperature: ' + str(maximumTemperature))
        print('Minimum temperature: ' + str(minimumTemperature))
    print('')




def makeSetsOfData(numOfSets):
    'input temperatures in the temperature set, rejects -232.00205 + 33.34, -232.00205 - 33.34'
    temperatureSets = []
    count = 0.0
    countTotal = 0.0
    countAccepted = 0.0
    countAcceptedTotal = 0.0
    for i in range(1, numOfSets+1):
        print('Start entering data for set ' + str(i) + ' and indicate you are finished by typing STOP.')
        temperature = raw_input()
        temperatureSets.append([])
        while temperature != 'STOP':
            temperature = float(temperature)
            if validTemperature(temperature):
                temperatureSets[i-1].append(temperature)
                temperature = raw_input()
                countAccepted += 1
            else:
                print('[REJECTED: ' + str(temperature) + ']')
                temperature = raw_input()
            count += 1
        countTotal += count
        countAcceptedTotal += countAccepted
        print(temperatureSets)
        dataStatsImmediate(temperatureSets, i, count, countAccepted)
        countAccepted = 0
        count = 0
    return temperatureSets, countTotal, countAcceptedTotal, numOfSets



def endingStats(temperatureSets, countTotal, countAcceptedTotal, numOfSets):
    'displays ending stats'
    sumTemperatureSets = 0
    percentRejected = ((countTotal-countAcceptedTotal) / countTotal) * 100
    for i in range(0, numOfSets):
        sumTemperatureSets += sum(temperatureSets[i])
    averageTemperature = sumTemperatureSets / (countAcceptedTotal)
    maximumTemperature = max(max(temperatureSets))
    temperatureSets = [i for i in temperatureSets if i != []]
    minimumTemperature = min(min(temperatureSets))
    print('')
    print('End Processing')
    print('')
    print('Overall stats: ')
    print('Number of data sets processed: ' + str(int(numOfSets)))
    print('Average of all temperatures processed: ' + str(averageTemperature))
    print('Maximum temperature: ' + str(maximumTemperature))
    print('Minimum temperature: ' + str(minimumTemperature))
    


def main():
    'main program for NASA temperature thingy'
    numOfSets = promptUser()
    temperatureSets, countTotal, countAcceptedTotal, numOfSets = makeSetsOfData(numOfSets)
    endingStats(temperatureSets, countTotal, countAcceptedTotal, numOfSets)



main()

