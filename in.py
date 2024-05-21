import pandas as pd
import os

import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook
from PIL import Image, ImageFont, ImageDraw


wb = openpyxl.load_workbook('mse3.xlsx')

f1 = 'mse3.xlsx'
df = pd.read_excel(f1, sheet_name=0)

msnv = list(df['MSNV'])
name = list(df['Họ & Tên'])
gp = list(df['Group'])

ws1 = wb['Total']
ws2 = wb['Sheet1']

def inf (data, letter):
    ind=11
    for i in data :
        num = 20
        ws2['{}{}'.format(letter,ind)] = i
        wb.save('mse3.xlsx')
        ind = ind + num
        
inf(msnv,'D')
inf(name,'E')
inf(gp,'F')


# for i in data :
#     num = 20
#     ws2['D{}'.format(ind)] = i
#     wb.save('mse3.xlsx')
#     ind = ind + num
    
    
    
    