import pytest
import openpyxl
import verificationCode
from tests.api import login_user
import sys
# 定义测试数据文件路径
TEST_DATA_FILE = r"C:\Users\Administrator\Desktop\test_data.xlsx"

# 读取测试数据
def read_test_data(sheet_name):
    wb = openpyxl.load_workbook(TEST_DATA_FILE)
    sheet = wb[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data

# 假设这里有一个fixture，用于设置测试环境，比如设置API的基本URL等
@pytest.fixture(scope="module")
def setup_api():
    # 在这里设置测试环境
    base_url = "http://192.168.1.8:7777"
    yield base_url

# 测试用例
@pytest.mark.parametrize("test_case, username, password, expected_status_code,msg", read_test_data("Sheet1"))
def test_login_user(setup_api, test_case, username, password, expected_status_code,msg):
    base_url = setup_api
    # 获取code和uuid
    r = verificationCode.codeApi()
    code = r[0]
    uuid = r[1]

    # 发送POST请求
    response = login_user(base_url, username, password, code, uuid)

    # 断言响应状态码
    assert response.json()["code"] == expected_status_code
    assert response.json()["msg"] == msg

    # 测试结果回写到execl中