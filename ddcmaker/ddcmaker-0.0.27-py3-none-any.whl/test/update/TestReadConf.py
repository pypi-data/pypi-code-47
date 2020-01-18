import unittest
from ddcmaker.update import ConfigDamage
from ddcmaker.update import read_conf, Config


class ConfigureTestCase(unittest.TestCase):
    def setUp(self) -> None:
        import pathlib
        path = pathlib.Path(__file__).absolute()
        self.conf_path = path.parent.joinpath('test_conf.json')

    def tearDown(self) -> None:
        self.conf_path.unlink()

    def test_empty_file(self):
        # 测试空文件
        self.conf_path.write_text('')
        with self.assertRaisesRegex(ConfigDamage, 'ddcmaker损坏，请执行ddcmaker更新'):
            read_conf(self.conf_path.as_posix())

    def test_empty_dict(self):
        self.conf_path.write_text("""{}""")
        with self.assertRaisesRegex(ConfigDamage, 'ddcmaker损坏，请执行ddcmaker更新'):
            read_conf(self.conf_path.as_posix())

    def test_file_ok(self):
        self.conf_path.write_text("""
         {
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
         """)
        conf = read_conf(self.conf_path.as_posix())
        self.assertEqual(type(conf), Config)
        origin = conf.origins[0]
        self.assertEqual(origin.name, "tsinghua")
        self.assertEqual(origin.url, "https://pypi.tuna.tsinghua.edu.cn/simple")

        feature = conf.features[0]
        self.assertEqual(feature.name, "action_groups")
        self.assertEqual(feature.url, "")
        self.assertEqual(feature.save_dir, "/home/pi/human_code")
        self.assertEqual(feature.temp_dir, "/home/pi/feature_temp")

    def test_origin_empty(self):
        self.conf_path.write_text("""
        {
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
        }""")
        config = read_conf(self.conf_path.as_posix())
        self.assertEqual(config.origins, [])

    def test_feature_empty(self):
        self.conf_path.write_text("""
       {
            "origins": [
                {
                    "name": "tsinghua",
                    "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
                }
            ],
            "features": []
        }""")
        config = read_conf(self.conf_path.as_posix())
        self.assertEqual(config.features, [])

    def test_no_origins(self):
        self.conf_path.write_text("""{"features": []}""")
        with self.assertRaises(ConfigDamage):
            read_conf(self.conf_path.as_posix())

    def test_no_features(self):
        self.conf_path.write_text("""{"origins": []}""")
        with self.assertRaises(ConfigDamage):
            read_conf(self.conf_path.as_posix())


if __name__ == '__main__':
    unittest.main()
