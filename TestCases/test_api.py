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
import unittest
import ddt
from Common.Get_P import GetTicket
from Common.my_logger import *

#获取所有的测试数据
excel_path = dir_config.testcase_dir + "/jm_api_info.xlsx"
de = DoExcel(excel_path)
all_case_datas = de.get_caseDatas_all()

get_p = GetTicket()
init_1 = get_p.get_ticket('dpouZsutKOLW16qv20-Hlg')
init_2 = get_p.get_ticket('Emb2kCvMzTPW16qv20-Hlg')
init_3 = get_p.get_ticket('ULux2LZD6TfW16qv20-Hlg')
init_4 = get_p.get_ticket('AmOLe35r_9vW16qv20-Hlg')
init_5 = get_p.get_ticket('h71eFogmlxnW16qv20-Hlg')


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

        logging.info('==============开始执行第%d个测试用例=============' % case_data['case_id'])

        if case_data["request_data"] is not None:
            if case_data["request_data"].find("${init_1}") != -1:
                case_data["request_data"] = case_data["request_data"].replace('${init_1}', init_1)
            elif case_data["request_data"].find("${init_2}") != -1:
                case_data["request_data"] = case_data["request_data"].replace('${init_1}', init_2)
            elif case_data["request_data"].find("${init_3}") != -1:
                case_data["request_data"] = case_data["request_data"].replace('${init_1}', init_3)
            elif case_data["request_data"].find("${init_4}") != -1:
                case_data["request_data"] = case_data["request_data"].replace('${init_1}', init_4)
            elif case_data["request_data"].find("${init_5}") != -1:
                case_data["request_data"] = case_data["request_data"].replace('${init_1}', init_5)



        res = myRequest.myRequest(case_data["url"], case_data["method"], case_data["request_data"])

        logging.debug(case_data["url"])
        logging.debug(case_data["request_data"])
        logging.debug(case_data["method"])



        logging.info('期望结果是：' + case_data["expected_data"])
        logging.info('实际结果是：' + res.text)

        # 判断断言选择类型 是全值匹配 还是 包含匹配
        if int(case_data['compare_type']) == 0:
            logging.info('全值匹配模式')
            try:
                self.assertEqual(res.text, case_data["expected_data"])
                logging.info('结果对比成功，测试用例通过')
            except AssertionError:
                logging.exception("结果对比失败")
                raise AssertionError
        else:
            logging.info('部分匹配模式')
            try:
                self.assertIn(case_data["expected_data"], res.text)
                logging.info('结果对比成功，测试用例通过')
            except AssertionError:
                logging.exception("结果对比失败")
                raise AssertionError

if __name__ == '__main__':
    unittest.main()






