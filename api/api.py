
from .comApi import CommApi


class ARK(object):

    def __init__(self, appkey, appsecret, sandbox=False):
        self._appkey = appkey
        self._secret = appsecret
        self._sandbox = sandbox

    comm = CommApi()
