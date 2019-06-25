
import requests
from time import time
from hashlib import md5

SANDBOX_URL = "http://flssandbox.xiaohongshu.com"
PRODUCT_URL = "https://ark.xiaohongshu.com"


class Comm(object):

    def __get__(self, instance, owner):
        self._appkey = instance._appkey
        self._secret = instance._secret
        self._apihost = SANDBOX_URL if instance._sandbox else PRODUCT_URL
        return self

    def _sign(self, url, data=None):
        """
        小红书验签算法
        """
        qstring = f"{url}?{'&'.join(f'{key}={data[key]}' for key in sorted(data.keys()) if data[key] is not None)}{self._secret}"
        return md5(qstring.encode("utf-8")).hexdigest()

    def _check_sign(self, url, headers, data):
        """
        验证推送的数据
        """
        sign = headers.pop("sign")
        return sign == self._sign(url, headers+data)

    def _get_headers(self, url, data=None):
        """
        获取请求头
        """

        if data is None:
            data = {}
        timestamp = str(int(time()))
        sign_data = data.copy()
        sign_data['timestamp'] = timestamp
        sign_data['app-key'] = self._appkey

        headers = {
            "timestamp": timestamp,
            "app-key": self._appkey,
            "content-type": "application/json;charset=utf-8",
            "sign": self._sign(url, sign_data)
        }

        return headers

    def post(self, url, data=None):
        """
        使用post方法请求接口        
        url: 接口地址(相对路径)
        data: 请求数据
        """
        headers = self._get_headers(url, data)
        url = f"{self._apihost}{url}"
        return requests.post(url, json=data, headers=headers)

    def get(self, url, data=None):
        """
        使用get方法请求接口        
        url: 接口地址
        data: 请求数据
        """
        headers = self._get_headers(url, data)
        url = f"{self._apihost}{url}"
        return requests.get(url, params=data, headers=headers)

    def put(self, url, data=None):
        """
        使用put方法请求接口        
        url: 接口地址
        data: 请求数据
        """
        headers = self._get_headers(url, data)
        url = f"{self._apihost}{url}"
        return requests.put(url, json=data, headers=headers)

    def patch(self, url, data=None):
        """
        使用patch方法请求接口
        url: 接口地址
        data: 请求数据
        """
        headers = self._get_headers(url, data)
        url = f"{self._apihost}{url}"
        return requests.patch(url, json=data, headers=headers)
