from .comm import Comm
from .exceptions import ArgsException


class OrderApi(Comm):

    def get_current_order_list(self, order_time_from, order_time_to, page_no=1, page_size=50):
        """
        即时订单列表
        order_time_from:查询订单创建时间的开始时间
        order_time_to:查询订单创建时间的结束时间(与创建时间之差不得超过30分钟)
        """

        url = "/ark/open_api/v0/packages/latest_packages"
        data = {
            "order_time_from": order_time_from,
            "order_time_to": order_time_to,
            "page_no": page_no,
            "page_size": page_size
        }
        return self.get(url, data=data).json()

    def get_order_status(self, package_ids):
        """
        订单状态
        package_ids: 查询的订单号，以“,”分隔，一次最多可查询20条
        """

        url = "/ark/open_api/v0/packages/packages_status"
        data = {
            "package_ids": package_ids
        }
        return self.get(url, data=data).json()

    def get_order_list(self, logistics=None, status=None, page_no=1, page_size=50, start_time=None, end_time=None, time_type=None):
        """
        订单列表
        该接口支持除三方保税（red_bonded)之外的任何物流模式，包裹为何种物流模式由其中商品决定，商品的物流模式取决于商家所配置的可选物流模式。需要传入的物流模式参数值可以通过公共接口获取。
        按照条件查询商家在小红书系统中被确认(Confirmed)的订单信息列表，该接口只能获取订单的基本信息，如需包括商品信息在内的详细信息，请使用订单详情接口。
        """

        if page_size > 100:
            raise ArgsException("分页大小不能大于100")

        url = "/ark/open_api/v0/packages"
        data = {
            "logistics": logistics,
            "status": status,
            "page_no": page_no,
            "page_size": page_size,
            "start_time": start_time,
            "end_time": end_time,
            "time_type": time_type
        }

        return self.get(url, data=data).json()

    def get_order_detail(self, package_id):
        """
        订单详情
        该接口支持第三方商家自主发货和小包转运，以及小红书物流(RED Express, RED Domestic Trade, RED Standard)
        根据订单ID查询商家在小红书系统中的订单详情信息并导出。
        package_id： 订单ID
        """

        url = f"/ark/open_api/v0/packages/{package_id}"
        return self.get(url).json()

    def order_send(self, package_id, express_company_code, express_no):
        """
        订单发货
        第三方商家调用该接口对订单做发货操作，发货时需要添加快递公司以及相应的快递公司单号。
        """

        url = f"/ark/open_api/v0/packages/{package_id}"
        data = {
            "status": "shipped",
            "express_company_code": express_company_code,
            "express_no": express_no
        }
        return self.put(url, data=data).json()

    def create_batches(self, package_id, weight):
        """
        创建批次
        该接口仅支持小包转运物流模式
        第三方商家调用该接口将包裹号和重量传至小红书，生成小包批次。请保存小包批次号(TPS号)以创建发运
        """
        url = "/ark/open_api/v0/packages/transfer_batches"
        data = {
            "package_id": package_id,
            "weight": weight
        }
        return self.post(url, data=data).json()

    def send_batches(self, batch_no):
        """
        小包批次发运
        该接口仅支持小包转运物流模式
        第三方商家调用该接口将对已生成的小包批次创建发运。
        """

        url = f"/ark/open_api/v0/packages/transfer_batches/{batch_no}"
        return self.put(url).json()

    def cancel_audit(self, package_id, audit_result, audit_reason=None):
        """
        取消订单审核
        package_id:订单ID
        audit_result: 审核结果，当值为"refused"时为拒绝，当值为"canceled"为取消成功
        该接口支持 第三方商家自主发货(red_auto)，小包转运/一单到底(red_box) 物流模式
        用于审核取消申请中的订单
        """
        url = "/ark/open_api/v0/packages/canceling/audit"
        data = {
            "package_id": package_id,
            "audit_result": audit_result,
            "audit_reason": audit_reason
        }
        return self.put(url, data=data).json()

    def get_cancel_orders(self, logistics=None, status=None, page_no=1, page_size=50, start_time=None, end_time=None):
        """
        取消订单列表
        该接口支持 第三方商家自主发货(red_auto)，小包转运/一单到底(red_box) 物流模式
        """
        url = "/ark/open_api/v0/packages/canceling/list"
        data = {
            "logistics": logistics,
            "status": status,
            "page_no": page_no,
            "page_size": page_size,
            "start_time": start_time,
            "end_time": end_time
        }
        return self.get(url, data=data).json()
