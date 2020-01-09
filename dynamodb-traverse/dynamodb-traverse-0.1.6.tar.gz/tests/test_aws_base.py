import unittest

__dt__ = __import__("dynamodb-traverse")


class TestAwsBase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = __dt__.AWSBase(
            my_aws_path="./tests/resources/fake_aws_creds.txt", profile="my-profile"
        )

        self.test_subject_with_region = __dt__.AWSBase(
            my_aws_path="./tests/resources/fake_aws_creds.txt",
            profile="my-profile-with-region",
        )

    def test_config_store(self):
        self.assertEqual(self.test_subject.my_aws_access_key_id, "myId")
        self.assertEqual(self.test_subject.my_aws_secret_access_key, "myKey")
        self.assertEqual(self.test_subject.my_region, "us-east-1")
        self.assertEqual(self.test_subject_with_region.my_region, "us-west-2a")
