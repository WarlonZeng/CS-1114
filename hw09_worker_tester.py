''' 
cs1114 

Submission: hw09

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

class WorkerRec

Assume: (can be found on cs1114 webpage)

'''

#TESTER

from hw09_worker import *

someWorker = WorkerRec( 420420420, 'gallaghersmokes', wage=0.01, hoursWorked=1, title='wat' )
# INITIALIZED

print( someWorker.getSSN())
# SSN

print( someWorker.getName())
# Name

print( someWorker.getWage())
# Wage
# GIVES WAGE_ERROR if wage is negative

print( someWorker.getHours())
# Hours worked
# Gives TIME_ERROR (-1337) if hoursWorked is negative

print( someWorker.getTitle())
# Title given
# TITLE IS A BLANK STRING IF NO TITLE GIVEN

print( someWorker.bestowTitle( 'what' ))
# Title earned
# Is an object mutator

print( someWorker.changeWage( 0.02 ))
# mutator
# gallaghersmokes now receives 0.02 per hour

print( someWorker.clockHours( 99 ))
# mutator

print( someWorker.receivePay())
# Pay earned
# GIVES NEGATIVE_PAY_ERROR (-360) if pay is negative
