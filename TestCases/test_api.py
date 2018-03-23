"""
-------------------------------------------------
   File Name：     test_api
   Description :
   Author :       zws
   date：          2018/3/13
-------------------------------------------------
   Change Activity:
                   2018/3/13:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.DoExcel import DoExcel
from Common import myRequest
import os
import unittest
import ddt
from Common import dir_config
from Common.my_logger import *

#获取所有的测试数据
excel_path = dir_config.testcase_dir + "/jm_api_info.xlsx"
de = DoExcel(excel_path)
all_case_datas = de.get_caseDatas_all()

@ddt.ddt
class Test_Api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        de.modify_phone()
        de.save_excelFile()

    @classmethod
    def tearDownClass(cls):
        pass

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):

        # print(eval(case_data["request_data"]))
        # print(case_data)
        logging.info('request_data' in case_data.keys())

        if 'request_data' in case_data.keys():
            res = myRequest.myRequest(case_data["url"],case_data["method"],request_data=eval(case_data["request_data"]))
        else:
            res = myRequest.myRequest(case_data["url"], case_data["method"])

        if int(case_data['compare_type']) == 0:
            self.assertEqual(res.text,case_data["expected_data"])
        else:
            self.assertIn(case_data["expected_data"],res.text)

if __name__ == '__main__':
    unittest.main()






