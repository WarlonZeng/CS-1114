''' 
cs1114 

Submission: hw10_company.py

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

class Company

Assume: (can be found on cs1114 webpage)

'''

####### COMPANY class =========================================        
####### COMPANY class =========================================        
####### COMPANY class =========================================        

# ----------------------------------------------
# start Company module
# filename: hw10_company.py
#
# Company does generate next account number
#
# ----------------------------------------------

from hw09_worker import *

# error codes

DUPL_SSN_ERROR = -34

# constants

threeDigits = 288

class Company( object ):
    ''' manages WorkerRecs
        has:
            name
            dictionary of account -> CompanyAccnt pairs
        account numbering is managed externally
        provides:
            addWorkerRec
            addHoursIntoAccount
            giveTitle
            changeTheWage
            doPayDay
                also generates next number
            fireWorker
        all will return error codes on error
    '''

    def __init__( self, name ):
        '''
            data member 	   type
	    name	           str
	    SSN	         dictionary of CompanyAccnt objects
	    threeDigits            int
        '''
        self.__name = name
        self.__SSNs = {}
        self.__threeDigits = threeDigits

    def __verifySSNInDictionary( self, SSN ):
        ''' returns True when SSN is valid,
                    False otherwise
        '''
        return SSN in self.__SSNs
        
    def addWorkerRec( self, SSN, name, wage=17.22, hoursWorked=0, title='' ):
        '''
            creates and adds a worker account
            returns DUPL_ACCNT_NUM_ERROR on dupl
        '''
        if self.__verifySSNInDictionary( SSN ):
            return DUPL_SSN_ERROR
        WR = WorkerRec( SSN, name, wage, hoursWorked, title )
        self.__SSNs[ SSN ] = WR
        return self.__SSNs

    def addHoursIntoAccount( self, SSN, hoursWorked ):
        ''' TIME_ERROR on negative hours worked
        '''
        self.__SSNs[ SSN ].clockHours( hoursWorked )
        if hoursWorked < 0:
            return TIME_ERROR
        return self.__SSNs[ SSN ]
        
    def giveTitle( self, SSN, title):
        ''' gives title to worker
        '''
        title = '[' + title + ']'
        self.__SSNs[ SSN ].bestowTitle( title )
        return self.__SSNs[ SSN ]

    def changeTheWage( self, SSN, wage ):
        ''' changes the wage of said worker
        '''
        self.__SSNs[ SSN ].changeWage( wage )
        return self.__SSNs[ SSN ]

    def doPayDay( self ):
        ''' self.__name implies company name which is public ...
            next three digit generator in this function as part of identifying the file '''
        self.__threeDigits += 177
        if self.__threeDigits > 999:
            self.__threeDigits -= 1000
        paySSNs = []
        payNames = []
        payAmounts = []
        payTitles = []
        payWorkersList = []
        for workers in range(len(self.__SSNs)):
            paySSNs.append(self.__SSNs.items()[workers][1].getSSN())
            payNames.append(self.__SSNs.items()[workers][1].getName())
            payAmounts.append(self.__SSNs.items()[workers][1].receivePay())
            payTitles.append(self.__SSNs.items()[workers][1].getTitle())
            payWorkersList.append((paySSNs[workers], payNames[workers], payAmounts[workers], payTitles[workers]))
        print(payWorkersList)
        ascendingOrder = sorted(payWorkersList, key=lambda x: x[2])
        payWorkers = self.__name.replace(' ', '') + str(self.__threeDigits) + '''.pay'''
        payWorkersFile = open( payWorkers, 'w' )
        for i in range(len(ascendingOrder)):
            payWorkersFile.write(str(ascendingOrder[i][0]))
            payWorkersFile.write('\n')
            payWorkersFile.write(ascendingOrder[i][1] + ' $' + str(ascendingOrder[i][2]) + ' ' + ascendingOrder[i][3])
            payWorkersFile.write('\n')
        payWorkersFile.close()
        for j in range(len(self.__SSNs)):
            self.__SSNs.items()[j][1].resetHours() # 343343: object <-- reset that
        return self.__SSNs, threeDigits
        
    def fireWorker( self, SSN ):
        ''' fires worker and pays him
        '''
        name =  self.__SSNs[ SSN ].getName()
        hoursWorked = self.__SSNs[ SSN ].getHours()
        wage = self.__SSNs[ SSN ].getWage()
        title = self.__SSNs[ SSN ].getTitle()
        pay = self.__SSNs[ SSN ].receivePay()
        firedWorker = str(name.replace(' ', '')) + '''FINAL.pay'''
        firedWorkerFile = open( firedWorker, 'w' )
        firedWorkerFile.write(str(SSN))
        firedWorkerFile.write('\n')
        firedWorkerFile.write(name + ' $' + str(pay) + title)
        firedWorkerFile.close()
        return self.__SSNs
		
# ----------------------------------------------
# end Company module
# filename: hw10_company.py
# ----------------------------------------------

