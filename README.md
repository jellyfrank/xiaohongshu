# 小红书 Python SDK

小红书Python SDK

## requirement

python >= 3.6

# 安装使用

## 安装

pypi:

```python
pip install xiaohongshu
```


## Usage

使用示例：
```
from xiaohongshu.api.api import ARK

ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28")

# 获取物流公司列表
ark.comm.get_express_list()
```

## 接口说明

公共接口封装在comm中
订单相关接口封装在order
库存相关接口封装在stock
商品相关封装在product.

## changelog

[0.0.3] 添加物流模式接口的说明，官方文档存在错误。
