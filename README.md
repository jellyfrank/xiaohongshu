# 小红书 Python SDK

小红书Python SDK

## requirement

python >= 3.6

# 开发中

## 已完成

* 公共数据接口(comm)
* 订单接口(order)
* 库存接口(stock)

## Todo

...

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
