"""AWS CLIをMFA付きで実行するため、MFA検証済みのアクセスキーを設定するためのスクリプト"""
from typing import Dict, List
from aws_mfa_util.credential import AwsCredential, convert_credential_dict


def make_credential_str_list(credential_path: str) -> List[str]:
    """引数で指定されたファイルからすべての文字列を読み取り、
    配列に格納する
    Args:
        credential_path: .aws/credentialへの絶対パス

    Returns:
        認証情報それぞれを一行の文字列にした配列
    """
    profile_list: List[str] = []
    with open(credential_path, mode='r') as fd:
        profile_str: str = ''
        for s_line in fd:
            if s_line[0] == '[':
                if profile_str != '':
                    profile_list.append(profile_str)
                profile_str = ''
            profile_str += s_line

        # 最後の要素を配列に追加する
        profile_list.append(profile_str)
    return profile_list


def convert_aws_credential(profile_list: List[str]) -> Dict[str, AwsCredential]:
    """.aws/credentialsファイルから読み取った情報をクラスに変換して、
    辞書として格納

    Args:
        profile_list: make_credential_str_list関数から取得した値

    Returns:
        AwsCredentialクラスを属性値として持つ辞書
    """
    aws_credential_dict: Dict[str, AwsCredential] = {}
    for profile in profile_list:
        splited_profile: List[str] = profile.split('\n')
        profile_processed_dict = {}
        profile_name: str = ''

        for part_of_profile in splited_profile:
            if '[' in part_of_profile and ']' in part_of_profile:
                profile_name = part_of_profile.strip('[]')
                profile_processed_dict['profile_name'] = profile_name
            if 'aws_access_key_id' in part_of_profile:
                profile_processed_dict['aws_access_key_id'] = part_of_profile.split(
                    '='
                )[1]
            if 'aws_secret_access_key' in part_of_profile:
                profile_processed_dict['aws_secret_access_key'] = part_of_profile.split(
                    '='
                )[1]
            if 'output' in part_of_profile:
                profile_processed_dict['output'] = part_of_profile.split('=')[1]
            if 'region' in part_of_profile:
                profile_processed_dict['region'] = part_of_profile.split('=')[1]
            if 'mfa_serial' in part_of_profile:
                profile_processed_dict['mfa_serial'] = part_of_profile.split('=')[1]

        aws_credential_dict[profile_name] = AwsCredential(
            *convert_credential_dict(profile_processed_dict)
        )
    return aws_credential_dict
