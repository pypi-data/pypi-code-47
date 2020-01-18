import unittest
from marshmallow.exceptions import ValidationError
from ddcmaker.update.configure import FeatureSchema


class FeatureSchemaTestCase(unittest.TestCase):
    def test_empty(self):
        # 测试空数据
        schema = FeatureSchema()
        with self.assertRaises(ValidationError):
            schema.load({})

    def test_ok(self):
        schema = FeatureSchema()
        feature = schema.load({
            "name": "action_groups",
            "url": "",
            "save_dir": "/home/pi/human_code",
            "temp_dir": "/home/pi/feature_temp"
        })
        self.assertEqual(feature.name, "action_groups")
        self.assertEqual(feature.url, "")
        self.assertEqual(feature.save_dir, "/home/pi/human_code")
        self.assertEqual(feature.temp_dir, "/home/pi/feature_temp")

    def test_name_type(self):
        schema = FeatureSchema()
        with self.assertRaises(ValidationError):
            schema.load({
                "name": 1,
                "url": "",
                "save_dir": "/home/pi/human_code",
                "temp_dir": "/home/pi/feature_temp"
            })

    def test_url_type(self):
        schema = FeatureSchema()

        with self.assertRaises(ValidationError):
            schema.load({
                "name": "action_groups",
                "url": 1,
                "save_dir": "/home/pi/human_code",
                "temp_dir": "/home/pi/feature_temp"
            })

    def test_save_dir_type(self):
        schema = FeatureSchema()

        with self.assertRaises(ValidationError):
            schema.load({
                "name": "action_groups",
                "url": "",
                "save_dir": 1,
                "temp_dir": "/home/pi/feature_temp"
            })

    def test_temp_dir_type(self):
        schema = FeatureSchema()

        with self.assertRaises(ValidationError):
            schema.load({
                "name": "action_groups",
                "url": "",
                "save_dir": "/home/pi/human_code",
                "temp_dir": 1
            })


if __name__ == '__main__':
    unittest.main()
