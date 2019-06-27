
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
        注意：小红书官方文档示例有误，本接口返回的数据结果包含在data节点下的data数据中，请用户注意。
        """
        url = "/ark/open_api/v0/package/logistics"
        return self.get(url).json()

    def search_brand(self, keyword, page_no=1, page_size=50):
        """
        品牌搜索
        keyword: 关键字
        page_no: 页码，默认1
        page_size: 分页大小，默认50
        """
        url = "/ark/open_api/v1/brand_search"
        data = {
            "keyword": keyword,
            "page_no": page_no,
            "page_size": page_size
        }

        return self.get(url, data).json()

    def get_category_list(self, category_ids=None):
        """
        分类列表
        category_ids: 父级分类，分类ID使用逗号隔开，高级分类在前，低级分类在后，如果该参数为空，则返回所有的一级分类
        """
        url = "/ark/open_api/v1/categories"
        data = {
            "category_ids": category_ids
        }
        return self.get(url, data).json()

    def get_variant_by_category(self, category_id):
        """
        由末级分类获取规格
        category_id: 末级分类
        """
        url = f"/ark/open_api/v1/category/{category_id}/variations"
        return self.get(url).json()

    def get_attributes_by_category(self, category_id):
        """
        由末级分类获取属性
        category_id: 末级分类
        """
        url = f"/ark/open_api/v1/categories/{category_id}/attribute_options"
        return self.get(url).json()

    def get_attribute_values_by_category(self, attribute_id):
        """
        由属性获取属性值
        attribute_id: 属性
        """
        url = f"/ark/open_api/v1/attributes/{attribute_id}/values"
        return self.get(url).json()

    def get_attribute_options_by_category(self, category_id):
        """
        由末级分类获取产品参数
        """
        url = f"/ark/open_api/v1/categories/{category_id}/attribute_options"
        return self.get(url).json()
