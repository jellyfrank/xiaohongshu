
from .comApi import CommApi
from .orderApi import OrderApi
from .stockApi import StockApi
from .productApi import ProductApi


class ARK(object):

    def __init__(self, appkey, appsecret, sandbox=False):
        self._appkey = appkey
        self._secret = appsecret
        self._sandbox = sandbox

    comm = CommApi()
    order = OrderApi()
    stock = StockApi()
    product = ProductApi()
