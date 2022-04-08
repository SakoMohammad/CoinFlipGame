from openpyxl import Workbook, load_workbook
#needed module
import random 

#spreadsheet
workbook = load_workbook('cfgame.xlsx')
#worksheet
worksheetSave = workbook['Save']

choice = input()

#random choice function
flipCoin = random.choice(["heads", "tails"])
print(flipCoin)

if choice == flipCoin:
    print('You were right')
else:
    print('you were wrong, it was tails')