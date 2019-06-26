from .comm import Comm
from .exceptions import ArgsException
import json


class StockApi(Comm):

    def sync_inventory(self, qty, barcode=None, item_id=None):
        """
        同步库存
        参数：
        qty: 要更新的数量
        barcode: 商品条码
        item_id: 商品ID
        barcode和item_id必须传入一个，两个都传时以barcode优先
        return:
        True或False
        """
        if not barcode and not item_id:
            raise ArgsException("Barcode或item_id必须传入一个参数")

        if barcode:
            url = f"/ark/open_api/v0/inventories/{barcode}"
        else:
            url = f"/ark/open_api/v0/inventories/item/{item_id}"

        data = {
            "qty": qty
        }

        res = self.put(url, data=data).json()
        return True if res.get("success", False) else False

    def add_inventory(self, qty, barcode=None, item_id=None):
        """
        增减库存
        参数： 
        qty: 增加或减少的数量（正增负减）
        barcode: 商品条码
        item_id: 商品ID
        barcode和item_id必须传入一个，两个都传时以barcode优先
        return:
        True或False
        """
        if not barcode and not item_id:
            raise ArgsException("Barcode或item_id必须传入一个参数")

        if barcode:
            url = f"/ark/open_api/v0/inventories/{barcode}"
        else:
            url = f"/ark/open_api/v0/inventories/item/{item_id}"

        data = {
            "qty": qty
        }

        res = self.patch(url, data=data).json()
        return True if res.get("success", False) else False

    def get_inventory(self, item_id):
        """
        获取商品当前可售库存量
        参数:
        item_id: 商品ID
        return:
        qty: 商品当前可售数量
        """

        url = f"/ark/open_api/v0/items/{item_id}/stock"
        res = self.get(url).json()
        return res.get("data", 0) if res.get("success", False) else 0

    def order_create_callback(self, url, headers, data, callback=None):
        """
        库存变动回调(订单创建)
        参数：
        url: 回调的URL（不包括host)
        headers: 小红书推送的请求头
        data: 小红书推送的数据
        callback: 要调用的处理方法
        return:
        返回给小红书的数据
        """
        data = {
            "data": "",
            "error_code": "",
            "error_msg": ""
        }
        if self._check_sign(url, headers, data):
            callback(data)
            data["success"] = True
        else:
            data["success"] = False
        return json.dumps(data)

    def order_cancel_callback(self, url, headers, data, callback=None):
        """
        库存变动回调（订单取消）
        参数：
        url: 回调的URL（不包括host)
        headers: 小红书推送的请求头
        data: 小红书推送的数据
        callback: 要调用的处理方法
        return:
        返回给小红书的数据
        """

        data = {
            "data": "",
            "error_code": "",
            "error_msg": ""
        }
        if self._check_sign(url, headers, data):
            callback(data)
            data["success"] = True
        else:
            data["success"] = False
        return json.dumps(data)
