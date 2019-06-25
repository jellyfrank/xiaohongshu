
import unittest
from xiaohongshu.api.api import ARK


class TestSign(unittest.TestCase):

    def test_sign(self):
        ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28")

        data = {
            "status": 0,
            "page_no": 1,
            "page_size": 50,
            "timestamp": 1469902537,
            "app-key": "xhs",
        }

        self.assertEqual(ark.comm._sign(
            "/ark/open_api/v1/items", data), "72be6fad4dd0e5104dbdebbcdadb2a06")

    def test_comApi(self):

        ark = ARK("xhs", "9a539709cafc1efc9ef05838be468a28", sandbox=True)
        self.assertEqual(ark.comm.get_express_list()["error_code"], 0)


if __name__ == "__main__":
    unittest.main()
