import openpyxl

# create object for workbook
wb = openpyxl.Workbook()

# grab the active sheet
sh = wb.active

# set sheet name
sh.title = "Dev"

sh['A1'] = "FNAME"
sh['B1'] = "LNAME"
sh['C1'] = "EMAIL"

sh['A2'] = "Gopinath"
sh['B2'] = "Jayakumar"
sh['C2'] = "gopithri@gmail.com"

# for saveing the file
wb.save(r"D:\Gopi.xlsx")