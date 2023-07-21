import now as now
import pytest
import openpyxl
from datetime import datetime
import ddddocr
import verificationCode

#
# # 定义测试数据文件路径
# TEST_DATA_FILE = r"C:\Users\Administrator\Desktop\test_data.xlsx"
#
# # 读取测试数据
# def read_test_data(sheet_name):
#     wb = openpyxl.load_workbook(TEST_DATA_FILE)
#     sheet = wb[sheet_name]
#     data = []
#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         data.append(row)
#     return data
#
# data = read_test_data("Sheet1")
# print(data)
r = verificationCode.codeApi()
code = r[0]
print(code)
