import dataclasses
from typing import Dict, List

try:
    # import boto3
    import botocore
    from boto3.session import Session
except ImportError:
    print('boto3がローカル環境にインストールされていません')
    exit(1)


# 取得する認証情報の期限は12時間に設定
DURATION_SECONDS = 43200


@dataclasses.dataclass
class AwsCredential:
    """認証情報クラス"""

    __profile_name: str
    __aws_access_key_id: str
    __aws_secret_access_key: str
    __output: str = ''
    __region: str = ''
    __mfa_serial: str = ''
    __aws_session_token: str = ''

    @property
    def profile_name(self) -> str:
        return self.__profile_name

    @property
    def output(self) -> str:
        return self.__output

    @property
    def region(self) -> str:
        return self.__region

    def check_mfa_serial(self) -> bool:
        print(self.__mfa_serial)
        if self.__mfa_serial:
            return True
        else:
            return False

    def get_sts_credential(self, token_code) -> Dict[str, str]:
        sesson = Session(
            aws_access_key_id=self.__aws_access_key_id,
            aws_secret_access_key=self.__aws_secret_access_key,
        )
        client = sesson.client('sts')
        try:
            response = client.get_session_token(
                DurationSeconds=DURATION_SECONDS,
                SerialNumber=self.__mfa_serial,
                TokenCode=token_code,
            )
        except botocore.exceptions.ClientError:
            print('STSからのクレデンシャルの取得に失敗しました')
            print('プロファイルの情報が正しいか、入力したコードが正しいことを確認して下さい')
            exit(1)
        return {
            'aws_access_key_id': response['Credentials']['AccessKeyId'],
            'aws_secret_access_key': response['Credentials']['SecretAccessKey'],
            'aws_session_token': response['Credentials']['SessionToken']
        }

    def export_string(self) -> str:
        profile_str: str = ''
        profile_str += '[{}]\n'.format(self.__profile_name)
        profile_str += 'aws_access_key_id={}\n'.format(self.__aws_access_key_id)
        profile_str += 'aws_secret_access_key={}\n'.format(self.__aws_secret_access_key)
        if self.__output:
            profile_str += 'output={}\n'.format(self.__output)
        if self.__region:
            profile_str += 'region={}\n'.format(self.__region)
        if self.__mfa_serial:
            profile_str += 'mfa_serial={}\n'.format(self.__mfa_serial)
        if self.__aws_session_token:
            profile_str += 'aws_session_token={}\n'.format(self.__aws_session_token)
        return profile_str

    def update_credential(self, aws_access_key_id, aws_secret_access_key, aws_session_token) -> None:
        self.__aws_access_key_id = aws_access_key_id
        self.__aws_secret_access_key = aws_secret_access_key
        self.__aws_session_token = aws_session_token


def convert_credential_dict(credential_dict) -> List[str]:
    required_attribute_list = [
        'profile_name',
        'aws_access_key_id',
        'aws_secret_access_key',
        'output',
        'region',
        'mfa_serial',
    ]
    converted_attribute_list: List[str] = []
    for attribute in required_attribute_list:
        if attribute in credential_dict:
            converted_attribute_list.append(credential_dict[attribute])
        else:
            converted_attribute_list.append('')
    return converted_attribute_list
