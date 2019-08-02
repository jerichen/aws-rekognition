# -*- coding:utf-8 -*-
from settings import *
import xlrd
import xlwt

# 打開 xlsx 文件
excel_data = xlrd.open_workbook(os.getenv('EXCEL_PATH'))

# 取得第一張表的名稱
row_data = excel_data.sheets()[0]

# 取得第一個表單
sheet_0 = excel_data.sheet_by_index(0)

# 創建 xlsx 表單
new_excel = xlwt.Workbook()

# 新建一個表單
new_sheet = new_excel.add_sheet('sheet1')
