''' 
cs1114 

Submission: hw09

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

class WorkerRec

Assume: (can be found on cs1114 webpage)

'''

####### WORKER REC class =========================================        
####### WORKER REC class =========================================        
####### WORKER REC class =========================================        

# ----------------------------------------------
# WorkerRec module
# filename: hw09_workerRec.py
# ----------------------------------------------

# error codes

WAGE_ERROR = -666
OVERPAID_ERROR = -420
UNDERPAID_ERROR = -69
TIME_ERROR = -1337
NEGATIVE_PAY_ERROR = -360

class WorkerRec( object ):
    '''
        has name
            SSN (unique indentifier)
            current wage
        supports getting paid and earning a title with constraints 
		(calulated mutators)
        accessors for name, wage and SSN
        mutator for name (direct setter)
    '''

    def __init__( self, SSN, name, wage=17.22, hoursWorked=0, title='' ):
        '''
            data members   assumptions:
              SSN       SSN is of correct form
              name           name is a str
              wage        wage is float
              hoursWorked    int
              title          title is str
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
        ''' returns worker's name name '''
        return self.__name

    def getWage( self ):
        ''' returns wage
            returns error if negative wage
        '''
        if self.__wage < 0:
            return WAGE_ERROR
        return self.__wage

    def getHours( self ):
        ''' assumes hours is numeric
            when hours is negative or 0
            returns TIME_ERROR if negative hours worked
        '''
        if self.__hoursWorked < 0:
            return TIME_ERROR
        return self.__hoursWorked

    def getTitle( self ):
        ''' returns title
        '''
        return self.__title

    def bestowTitle( self, title ):
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
        self.__hoursWorked += hoursWorked
        return self.__hoursWorked

    def resetHours( self ):
        ''' reset hours worked since last pay period
        '''
        self.__hoursWorked = 0
        return self.__hoursWorked

    def receivePay( self ):
        ''' assumes hours is numeric
            when pay is incorrectly under
                returns UNDERPAID_ERROR
            when pay is incorrectly over
                returns OVERPAID_ERROR
            when pay is negative
                returns NEGATIVE_PAY_ERROR
        '''
        pay = self.__hoursWorked * self.__wage
        if pay > self.__hoursWorked * self.__wage:
            return OVERPAID_ERROR
        if pay < self.__hoursWorked * self.__wage:
            return UNDERPAID_ERROR
        if pay < 0:
            return NEGATIVE_PAY_ERROR
        return pay

    def __str__( self ):
        ''' stringify
            for print purposes
        '''
        return str(self.__SSN) + ' ' + str(self.__name) + ' ' +  '$' + str(self.__wage) + ' ' +  str(self.__hoursWorked) + 'hrs ' + str(self.__title)

# ----------------------------------------------
# end WorkerRec module
# filename: hw09_workerRec.py
# ----------------------------------------------


