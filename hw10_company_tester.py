''' 
cs1114 

Submission: hw10

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

class WorkerRec

Assume: (can be found on cs1114 webpage)

'''

#TESTER

from hw09_worker import *

from hw10_company import *

RockPitSnakePitAndCo = Company( 'RockPit SnakePit and Co' )
#0

print(RockPitSnakePitAndCo.addWorkerRec( 443882354, 'Sally Jones' ))
#1

print(RockPitSnakePitAndCo.changeTheWage( 443882354, 35.22 ))
#2

print(RockPitSnakePitAndCo.addWorkerRec( 283728992, 'Joe Smith' ))
#3

print(RockPitSnakePitAndCo.changeTheWage( 283728992, 25.34 ))
#4

print(RockPitSnakePitAndCo.addHoursIntoAccount( 443882354, 11 ))
#5

print(RockPitSnakePitAndCo.addHoursIntoAccount( 283728992, 9 ))
#6

print(RockPitSnakePitAndCo.addHoursIntoAccount( 443882354, 3 ))
#7

RockPitSnakePitAndCo.doPayDay()
#8

print(RockPitSnakePitAndCo.addHoursIntoAccount( 443882354, 10 ))
#9

print(RockPitSnakePitAndCo.addWorkerRec( 248339271, 'Ralphael' ))
#10

print(RockPitSnakePitAndCo.changeTheWage( 248339271, 26.39 ))
#11

print(RockPitSnakePitAndCo.addHoursIntoAccount( 283728992, 4 ))
#12

print(RockPitSnakePitAndCo.giveTitle( 443882354, 'Master Snake Handler' ))
#13

print(RockPitSnakePitAndCo.changeTheWage( 283728992, 15.15 ))
#14

print(RockPitSnakePitAndCo.addHoursIntoAccount( 283728992, 7 ))
#15

RockPitSnakePitAndCo.doPayDay()
#16

print(RockPitSnakePitAndCo.addHoursIntoAccount( 283728992, 9 ))
#17

print(RockPitSnakePitAndCo.addHoursIntoAccount( 248339271, 4 ))
#18

RockPitSnakePitAndCo.fireWorker( 283728992 )
#19

print(RockPitSnakePitAndCo.changeTheWage( 248339271, 26.41 ))
#20

print(RockPitSnakePitAndCo.addHoursIntoAccount( 248339271, 18 ))
#21

RockPitSnakePitAndCo.doPayDay()
#22
