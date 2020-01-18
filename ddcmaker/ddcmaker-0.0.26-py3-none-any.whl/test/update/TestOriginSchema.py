import unittest
from marshmallow.exceptions import ValidationError
from ddcmaker.update.configure import OriginSchema


class OriginSchemaTestCase(unittest.TestCase):
    def test_empty(self):
        # 测试空数据
        schema = OriginSchema()
        with self.assertRaises(ValidationError):
            schema.load({})

    def test_ok(self):
        schema = OriginSchema()
        origin = schema.load({
            "name": "tsinghua",
            "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
        }
        )
        self.assertEqual(origin.name, "tsinghua")
        self.assertEqual(origin.url, "https://pypi.tuna.tsinghua.edu.cn/simple")

    def test_name_type(self):
        schema = OriginSchema()
        with self.assertRaises(ValidationError):
            schema.load({
                "name": 1,
                "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
            })

    def test_url_type(self):
        schema = OriginSchema()

        with self.assertRaises(ValidationError):
            schema.load({
                "name": "tsinghua",
                "url": 1
            })


if __name__ == '__main__':
    unittest.main()
