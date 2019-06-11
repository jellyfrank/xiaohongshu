
from .comm import Comm


class CommApi(Comm):

    def get_express_list(self):
        """
        获取快递公司列表
        """
        url = "/ark/open_api/v0/express_companies"
        return self.get(url).json()

    def get_express_mode(self):
        """
        获取物流模式
        """
        url = "/ark/open_api/v0/package/logistics"
        return self.get(url).json()
