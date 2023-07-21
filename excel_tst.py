import xlrd
import xlwt
import os
import xlutils
from xlutils.copy import copy

# import xlrd
# import os
# from xlutils.copy import copy
# from xlwt import Style
# def writeExcel(row, col, str, styl=Style.default_style):
#     rb = xlrd.open_workbook(file, formatting_info=True)
#     wb = copy(rb)
#     ws = wb.get_sheet(0)
#     ws.write(row, col, str, styl)
#     wb.save(file)
#     style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center');
#     writeExcel(1, 1, 'hello world', style)

if __name__ == "__main__":
    fpath = 'D:/temp/py_test.xlsx'
    print(fpath)
    rd_book = xlrd.open_workbook(fpath)
    sh1 = rd_book.sheets()[0]
    print(sh1.nrows);

    wt_book = copy(rd_book)
    ws = wt_book.get_sheet(0)
    ws.write(2,3, 'hellow')
    wt_book.save(fpath)
