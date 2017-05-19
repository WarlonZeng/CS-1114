''' 
cs1114 

Submission: hw09

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

class workerRec

Assume:

list given
'''

####### WORKER REC class =========================================        
####### WORKER REC class =========================================        
####### WORKER REC class =========================================        

# ----------------------------------------------
# WorkerRec module
# filename: workerRec_MODULE.py
# ----------------------------------------------

# error codes
OVERPAID_ERROR = 0x00000069
UNDERPAID_ERROR = 0x00000420
TIME_ERROR = 0x00001337

class WorkerRec( object ):
    '''
        has name
            SSN (unique indentifier)
            current wage
        supports getting paid and earning a title with constraints 
		(calulated mutators)
        accessors for name, wage and SSN
        mutator for name (direct setter)
        __str__ formatted:
                   name [SSN num]: $99.99
    '''

    def __init__( self, SSN, name, wage=17.22, hoursWorked=0, title='' ):
        '''
            data members   assumptions:
              SSN       SSN is of correct form
              name           name is a str
              wage        wage is float
        '''
        self.__SSN = SSN
        self.__name = name
        self.__wage = wage
        self.__hoursWorked = hoursWorked
        self.__title = title

    def getSSN( self ):
        ''' returns account  number'''
        return self.__SSN

    def getName( self ):
        ''' returns account holder's name '''
        return self.__name

    def getWage( self ):
        ''' returns wage '''
        return self.__wage

    def getHours( self ):
        ''' assumes hours is numeric
            when hours is negative or 0
            returns DEPOSIT_NEG_AMT_ERROR
        '''
        return self.__hoursWorked

    def getTitle( self ):
        ''' returns title
        '''
        return self.__title

    def bestowTitle( self, title)
        '''give title
        '''
        self.__title = title
        return self.__title

    def changeWage( self, wage ):
        ''' assumes newName is a valid name str '''
        self.__wage = wage
        return self.__wage

    def clockHours( self, hoursWorked ):
        ''' clock in hours worked
        '''
        if hoursWorked < 0:
            return TIME_ERROR
        self.__hoursWorked += hours
        return self.__hoursWorked

    def receivePay( self, hoursWorked, wage ):
        ''' assumes hours is numeric
            when hours is negative or 0
            returns WITHDRAW_NEG_AMT_ERROR
            when the hours > wage
            returns OVERDRAFT_ERROR
        '''
        pay = hoursWorked * wage
        if pay > hoursWorked * wage:
            return OVERPAID_ERROR
        elif pay < hoursWorked * wage:
            return UNDERPAID_ERROR
        return self.__pay

    def __str__( self ):
        ''' stringify
            formatted:
            name [accnount num]: $99.99
        '''
        return "%10s [%s]: $%.2f " % (self.__name, self.__SSN, self.__wage)

# ----------------------------------------------
# end WorkerRec module
# filename: workerRec_MODULE.py
# ----------------------------------------------


