
import unittest
from xiaohongshu.api.api import ARK


class TestSign(unittest.TestCase):

    def test_sign(self):
        ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28")

        data = {
            "timestamp": 1560231372,
            "app-key": "5fdd748e36"
        }

        self.assertEqual(ark.comm._sign(
            "/ark/open_api/v0/package/logistics", data), "bbe165e2e8bbc0610ce17daae18b8bf8")

    def test_comApi(self):

        ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28", sandbox=False)
        self.assertEqual(ark.comm.get_express_list()["error_code"], 0)


if __name__ == "__main__":
    unittest.main()
