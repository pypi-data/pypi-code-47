import unittest
from marshmallow.exceptions import ValidationError
from ddcmaker.update.configure import ConfigSchema


class ConfigSchemaTestCase(unittest.TestCase):
    def test_empty(self):
        # 测试空数据
        schema = ConfigSchema()
        with self.assertRaises(ValidationError):
            schema.load({})

    def test_ok(self):
        schema = ConfigSchema()
        config = schema.load({
            "origins": [
                {
                    "name": "tsinghua",
                    "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
                }
            ],
            "features": [
                {
                    "name": "action_groups",
                    "url": "",
                    "save_dir": "/home/pi/human_code",
                    "temp_dir": "/home/pi/feature_temp"
                }
            ]
        }
        )
        origin = config.origins[0]
        self.assertEqual(origin.name, "tsinghua")
        self.assertEqual(origin.url, "https://pypi.tuna.tsinghua.edu.cn/simple")

        feature = config.features[0]
        self.assertEqual(feature.name, "action_groups")
        self.assertEqual(feature.url, "")
        self.assertEqual(feature.save_dir, "/home/pi/human_code")
        self.assertEqual(feature.temp_dir, "/home/pi/feature_temp")

    def test_origin_empty(self):
        schema = ConfigSchema()
        config = schema.load({
            "origins": [
            ],
            "features": [
                {
                    "name": "action_groups",
                    "url": "",
                    "save_dir": "/home/pi/human_code",
                    "temp_dir": "/home/pi/feature_temp"
                }
            ]
        }
        )
        self.assertEqual(config.origins, [])

    def test_feature_empty(self):
        schema = ConfigSchema()
        config = schema.load({
            "origins": [
                {
                    "name": "tsinghua",
                    "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
                }
            ],
            "features": []
        }
        )
        self.assertEqual(config.features, [])

    def test_no_origins(self):
        schema = ConfigSchema()
        with self.assertRaises(ValidationError):
            schema.load({"features": []})

    def test_no_features(self):
        schema = ConfigSchema()
        with self.assertRaises(ValidationError):
            schema.load({"origins": []})


if __name__ == '__main__':
    unittest.main()
