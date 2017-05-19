''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec04part3.py

constraints: none

assumtions: 1 pesos = 0.066 usd
'''

from rec04part2 import printAsUSDollars
from rec04part2 import convertPesosToUSDollars
from rec04part2 import printAsCoins
from rec04part2 import quantityOfCoins

def main():
    printAsUSDollars(4.47)
    print('''''')
    convertPesosToUSDollars(20)
    print('''''')
    printAsCoins(4.47)
    print('''''')
    quantityOfCoins(4.47)

main()
    
