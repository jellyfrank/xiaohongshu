#!/usr/bin/python3
# @Time    : 2019-06-26
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .exceptions import ArgsException
import json


class ProductApi(Comm):

    """商品类接口"""

    def create_spu(self, data):
        """
        创建SPU
        该接口可创建SPU及相应的SPL，SPL_ITEM, SPV和ITEM, 也可单独创建SPU后，其余信息使用对应的创建接口创建
        参数：
        data：要创建的数据，数据格式请参考：https://school.xiaohongshu.com/open/product/create-spu.html
        """
        url = "/ark/open_api/v1/spu"
        return self.post(url, data=data)

    def create_spl(self, spu_id, data):
        """
        创建SPL
        该接口可创建已存在的SPU下的SPL及相应的SPL_ITEM,SPV和ITEM, 也可单独创建SPL后，其余模块信息使用对应的创建接口创建。
        参数：
        data: 待创建的数据，格式请参考： https://school.xiaohongshu.com/open/product/create-spl.html
        """
        url = f"/ark/open_api/v1/spu/{spu_id}/spl"
        return self.post(url, data=data)

    def create_spl_item(self, spl_id, data):
        """
        创建spl item
        该接口可创建已存在的SPL下的SPL ITEM。
        参数：
        data: 待创建的数据，格式参考： https://school.xiaohongshu.com/open/product/create-spl-item.html
        """
        url = f"/ark/open_api/v1/spl/{spl_id}/spl_item"
        return self.post(url, data=data)

    def create_spv(self, spl_id, data):
        """
        创建spv
        该接口可创建已存在的SPL下的SPV及相应ITEM, 也可单独创建SPV后，ITEM模块信息使用对应的创建接口创建。
        参数：
        data: 待创建的数据，格式参考： https://school.xiaohongshu.com/open/product/create-spv.html
        """
        url = f"/ark/open_api/v1/spl/{spl_id}/spv"
        return self.post(url, data=data)

    def create_item(self, spv_id, data):
        """
        创建ITEM
        该接口可创建已存在的SPV下的ITEM。
        参数：
        data： 待创建的数据，格式参考 https://school.xiaohongshu.com/open/product/create-item.html
        """
        url = "/ark/open_api/v1/spv/{spv_id}/item"
        return self.post(url, data)

    def update_spu(self, spu_id, data):
        """
        编辑更新SPU
        通过该接口更新SPU模块信息，请注意更新时请求body中的所有字段必填做替换资源操作。
        """
        url = f"/ark/open_api/v1/spu/{spu_id}"
        return self.put(url, data=data)

    def update_spl(self, spl_id, data):
        """
        编辑更新SPL
        通过该接口更新SPL模块信息，请注意更新时请求body中的所有字段必填做替换资源操作。
        """
        url = f"/ark/open_api/v1/spl/{spl_id}"
        return self.put(url, data=data)

    def update_spl_item(self, spl_id, data):
        """
        编辑更新SPL ITEM
        通过该接口更新SPL ITEM模块信息，请注意更新时请求body中的所有字段必填做替换资源操作
        """
        url = f"/ark/open_api/v1/spl/{spl_id}/spl_item"
        return self.put(url, data=data)

    def update_spv(self, spv_id, data):
        """
        编辑更新SPV
        通过该接口更新SPV模块信息，请注意更新时请求body中的所有字段必填做替换资源操作
        """
        url = f"/ark/open_api/v1/spv/{spv_id}"
        return self.put(url, data=data)

    def update_customs(self, spv_id, import_cost, manufacturer, customs_specification, ingredient, usage, customs_photos_urls):
        """
        编辑更新海关备案信息
        参数：
        spv_id：
        import_cost:进口成本价(CNY)(可粗略估计)
        manufacturer:生产厂家(填写全称，中文／英文)
        customs_specification:规格型号(例如，液体：10ml，10ml/支 (等其他计量单位) ；固体：10g，10g/支 (等其他计量单位)；配饰/鞋子/服装：尺寸、尺码、颜色。)
        ingredient:材质或成分含量(例如，水、二氧化碳等；帆布、牛皮等)
        usage:用途(例如，护肤等；背包、双肩包、凉鞋等)
        customs_photos_urls:商品图片（用于海关备案）
        """
        url = f"/ark/open_api/v1/spv/{spv_id}/customs"
        data = {
            "import_cost": import_cost,
            "manufacturer": manufacturer,
            "customs_specification": customs_specification,
            "ingredient": ingredient,
            "usage": usage,
            "customs_photos_urls": customs_photos_urls
        }
        return self.put(url, data=data)

    def update_item(self, item_id, price, original_price, pre_tax_price, article_no):
        """
        编辑更新ITEM
        参数：
        item_id：已存在的ITEM ID
        price:商品售价，非跨境税商家必填
        original_price:商品原价
        pre_tax_price:税前价，跨境税商家必填
        article_no:货品编号，非必填
        """

        url = f"/ark/open_api/v1/item/{item_id}"
        data = {
            "item_id": item_id,
            "price": price,
            "original_price": original_price,
            "pre_tax_price": pre_tax_price,
            "article_no": article_no
        }
        return self.put(url, data=data)

    def update_logistics(self, item_id, logistics_name):
        """
        编辑ITEM物流模式
        参数：
        item_id： 已存在的ITEM ID
        logistics_name： 物流模式代码，对应物流模式接口列表内的logistics_code
        """
        url = f"/ark/open_api/v1/item/{item_id}/logistics"
        data = {
            "logistics_name": logistics_name
        }
        return self.put(item_id, logistics_name)

    def submit(self, spl_id, data):
        """
        商品提交审核
        Open API导入Ark的商品SPU SPV信息自动审核通过，需要提交审核的部分是SPL_ITEM，创意编辑（文描）信息。该接口可提交创意编辑（文描）信息审核。
        """
        url = f"/ark/open_api/v1/spl/{spl_id}/spl_item/submit"
        return self.put(spl_id, data=data)

    def enable(self, item_id, available):
        """
        上架/下架商品
        如果其余可售卖条件满足，该接口可作为被商家操作上架、下架商品。
        参数：
        item_id:商品 ID
        available: 是否可用
        """
        url = f"/ark/open_api/v1/item/{item_id}/availability"
        data = {
            "available": available
        }
        return self.put(url, data=data)

    def get_products(self, status=None, page_no=None, page_size=None, buyable=None, create_time_from=None, create_time_to=None, update_time_from=None, update_time_to=None, stock_gte=None, stock_lte=None):
        """
        商品列表基础版
        可通过不同的筛选条件获取相应的ITEM基本信息列表。
        """
        url = "/ark/open_api/v1/items/lite"
        data = {
            "status": status,
            "page_no": page_no,
            "page_size": page_size,
            "buyable": buyable,
            "create_time_from": create_time_from,
            "create_time_to": create_time_to,
            "update_time_from": update_time_from,
            "update_time_to": update_time_to,
            "stock_gte": stock_gte,
            "stock_lte": stock_lte
        }
        return self.get(url, data=data)

    def get_full_products(self, status=None, page_no=None, page_size=None, buyable=None, create_time_from=None, create_time_to=None, update_time_from=None, update_time_to=None, stock_gte=None, stock_lte=None):
        """
        商品列表完整版
        可通过不同的筛选条件获取相应的ITEM完整信息列表。
        """
        url = "/ark/open_api/v1/items"
        data = {
            "status": status,
            "page_no": page_no,
            "page_size": page_size,
            "buyable": buyable,
            "create_time_from": create_time_from,
            "create_time_to": create_time_to,
            "update_time_from": update_time_from,
            "update_time_to": update_time_to,
            "stock_gte": stock_gte,
            "stock_lte": stock_lte
        }
        return self.get(url, data=data)

    def get_spu_info(self, spu_id):
        """
        SPU详情
        该接口可通过SPU ID查询该SPU下全部SPL，SPL ITEM，SPV，ITEM的信息。
        """
        url = f"/ark/open_api/v1/spu/{spu_id}"
        data = {
            "spu_id": spu_id
        }
        return self.get(url, data=data)

    def get_product_info(self, id, barcode, skucode):
        """
        商品详情
        该接口可通过商品id，条形码或小红书编码查询商品详情。
        """
        url = f"/ark/open_api/v1/items"
        data = {
            "id": id,
            "barcode": barcode,
            "skucode": skucode
        }
        return self.get(url, data=data)
