#!/usr/bin/python3
# @Time    : 2019-12-30
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from xiaohongshu.api.api import ARK, OrderApi


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28")

    def test_get_order_list(self):
        """
        测试获取订单列表接口
        """
        res = self.ark.order.get_order_list()
        self.assertEqual(res["error_code"], 0, res)

    def test_get_order_detail(self):
        """
        测试订单详情接口
        """
        res = self.ark.order.get_order_detail("P576162149188951551")
        self.assertEqual(res["error_code"], 0, res)


if __name__ == "__main__":
    unittest.main()
