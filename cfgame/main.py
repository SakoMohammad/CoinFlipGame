from openpyxl import Workbook, load_workbook
#needed module
import random 

#spreadsheet
workbook = load_workbook('cfgame.xlsx')
#worksheet
worksheetSave = workbook['Save']



#random choice function
a = random.choice([1, 2])
print(a)

#save function
def save():
  