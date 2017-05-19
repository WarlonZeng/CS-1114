####### COMPANY class =========================================        
####### COMPANY class =========================================        
####### COMPANY class =========================================        

# ----------------------------------------------
# start Company module
# filename: worker_Moldule.py
#
# final version
# - Company does not generate next account number
#
# ----------------------------------------------

from hw09_worker import *

# error codes

DUPL_ACCNT_NUM_ERROR = 0x00000034

class Company( object ):
    ''' manages WorkerRecs

        has:
            name
            dictionary of account -> CompanyAccnt pairs
        account numbering is managed externally
        provides:
            addWorkerRec( name, bal=0 )
                also generates next account number
            getBalance( accountNumber )
            depositIntoAccount( accountNumber, depositAmt )
            withdrawFromAccount( accountNumber, amt )
            xfer( FromAccountNumber, ToAccountNumber, amt )
            [xfer is not implemented here - you write it!]
        all will return error codes on error
    '''

    def __init__( self, name ):
        '''
            data member 	   type
	    name	           str
	    SSN	         dictionary of CompanyAccnt objects
        '''
        self.__name = name
        self.__SSNs = {}

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
            return DUPL_ACCNT_NUM_ERROR
        WR = WorkerRec( SSN, name, wage, hoursWorked, title='' )
        self.__SSNs[ SSN ] = WR

    def addHoursIntoAccount( self, SSN, hoursWorked ):
        ''' returns None on success,
            returns ACCNT_NOT_FOUND_ERROR when either accountNumber not found
            returns DEPOSIT_NEG_AMT_ERROR when neg deposit attempted
			returns OVERDRAFT_ERROE
        '''
        self.__SSNs[ SSN ].clockHours( hoursWorked )

    def giveTitle( self, SSN, title):
        self.__SSNs[ SSN ].bestowTitle( title )

    def changeTheWage( self, SSN, wage ):
        self.__SSNs[ SSN ].changeWage( wage )

    def doPayDay( self, SSN, threeDigits=288 ):
        '''self.__name implies company name which is public ... '''
        threeDigits += 177
        if threeDigits > 999:
            threeDigits -= 1000
        paySSNs = []
        payNames = []
        payAmounts = []
        payTitles = []
        payWorkersList = []
        for workers in range(len(self.__SSNs)):
            paySSNs.append(SSN)
            payNames.append(self.__SSNs[ SSN ].getName())
            payAmounts.append(self.__SSNs[ SSN ].receivePay( hoursWorked, wage ))
            payTitles.append(self.__SSNs[ SSN ].getTitle())
            payWorkersList.append(paySSNs[workers], payNames[workers], payAmounts[workers], payTitles[workers])
        ascendingOrder = sorted(payWorkersList.items(), key=lambda x: x[2])
        payWorkers = self.__name.replace(' ', '') + str(threeDigits) + '''.txt'''
        payWorkersFile = open( payWorkers, 'r+' )
        for workers in range(len(ascendingOrder)):
            payWorkers.write(str(payWorkersList[workers][0]))
            payWorkers.write('\n')
            payWorkers.write(payWorkersList[workers][1] + ' $' + str(payWorkersList[workers][2]) + payWorkersList[3])
            payWorkers.write('\n')
        payWorkersFile.close()
        
    def fireWorker( self, SSN ):
        self.__name =  self.__SSNs[ SSN ].getName()
        self.__hoursWorked = self.SSNs[ SSN ].getHoursWorked()
        self.__wage = self.SSNs[ SSN ].getWage()
        self.__title = self.SSNs[ SSN ].getTitle()
        self.__pay = self.__SSNs[ SSN ].receivePay( hoursWorked, wage )
        firedWorker = str(self.__name.replace(' ', '')) + '''FINAL.txt'''
        firedWorkerFile = open( fileNameOutput, 'r+' )
        firedWorkerFile.write(str(SSN))
        firedWorkerFile.write('\n')
        firedWorkerFile.write(self.__name + ' ' + str(self.__pay) + self.__title)
        firedWorkerFile.write(str(SSN))
        firedWorkerFile.close()
        
		
# ----------------------------------------------
# end Company module
# filename: worker_Moldule.py
# ----------------------------------------------

