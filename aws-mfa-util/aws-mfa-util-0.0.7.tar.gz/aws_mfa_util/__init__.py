"""AWS CLIをMFA付きで実行するため、MFA検証済みのアクセスキーを設定するためのスクリプト"""
from typing import Dict, List
from pathlib import Path
from aws_mfa_util.credential import AwsCredential, convert_credential_dict
from aws_mfa_util.util import make_credential_str_list, convert_aws_credential

AWS_CREDENTIAL_PATH = str(Path.home() / '.aws/credentials')

try:
    from PyInquirer import prompt
except ImportError:
    print('PyInquirerがローカル環境にインストールされていません')
    exit(1)


def main():
    profile_list: List[str] = make_credential_str_list(AWS_CREDENTIAL_PATH)
    aws_credential_dict: Dict[str, AwsCredential] = convert_aws_credential(profile_list)

    # ========================================
    # プロファイルを新規作成するか、更新するかを質問する
    # ========================================
    action_questions = [
        {
            'type': 'list',
            'name': 'select_action',
            'message': '希望する処理を選択して下さい',
            'choices': ['MFA用プロファイルを新規作成', 'MFA用プロファイルの認証情報を更新'],
        }
    ]
    action_answers = prompt(action_questions)

    if action_answers['select_action'] == 'MFA用プロファイルを新規作成':
        # if: 新規でMFAユーザーを作成する場合

        # ========================================
        # どのプロファイルからMFAのプロファイルを作成するかを質問する
        # ========================================
        profile_questions = [
            {
                'type': 'list',
                'name': 'profile_name',
                'message': 'MFA用に新規作成するプロファイルを選択して下さい',
                'choices': [
                    profile_name
                    for profile_name in aws_credential_dict
                    if '-mfa' not in profile_name
                ],
            }
        ]
        # profile_answer = prompt(profile_questions)

        target_aws_credential: AwsCredential = aws_credential_dict[
            profile_answer['profile_name']
        ]
        if not target_aws_credential.check_mfa_serial():
            print('MFAデバイスのシリアルが登録されていません')
            exit(1)

        code_questions = [
            {'type': 'input', 'name': 'code', 'message': 'ワンタイムコードを入力して下さい'}
        ]
        code_answers = prompt(code_questions)

        # STSから一時クレデンシャルを取得する
        session_credential = target_aws_credential.get_sts_credential(
            code_answers['code']
        )

        # 取得した一時クレデンシャルを用いて、新規のAwsCredentialクラスを作成する
        new_aws_mfa_credential: AwsCredential = AwsCredential(
            profile_answer['profile_name'] + '-mfa',
            session_credential['aws_access_key_id'],
            session_credential['aws_secret_access_key'],
            aws_credential_dict[profile_answer['profile_name']].output,
            aws_credential_dict[profile_answer['profile_name']].region,
            '',
        )
        aws_credential_dict[
            new_aws_mfa_credential.profile_name
        ] = new_aws_mfa_credential

        final_message: str = 'MFA用プロファイルの新規作成が完了しました。'

    elif action_answers['select_action'] == 'MFA用プロファイルの認証情報を更新':
        # if: 既存のMFAプロファイルの情報を更新する

        # ========================================
        # どのプロファイルのMFA情報を更新するかを確認する
        # ========================================
        mfa_profile_list = [
            profile_name
            for profile_name in aws_credential_dict
            if '-mfa' in profile_name
        ]
        if not mfa_profile_list:
            print('MFA用のプロファイルがありません')
            exit(1)
        profile_questions = [
            {
                'type': 'list',
                'name': 'profile_name',
                'message': '更新するMFAプロファイルを選択して下さい',
                'choices': mfa_profile_list,
            }
        ]
        profile_answer = prompt(profile_questions)

        profile_name = profile_answer['profile_name']
        base_profile_name: str = profile_name.rstrip('-mfa')
        code_questions = [
            {'type': 'input', 'name': 'code', 'message': 'ワンタイムコードを入力して下さい'}
        ]
        code_answers = prompt(code_questions)

        session_credential = aws_credential_dict[base_profile_name].get_sts_credential(
            code_answers['code']
        )
        aws_credential_dict[profile_name].update_credential(
            session_credential['aws_access_key_id'],
            session_credential['aws_secret_access_key'],
        )

        final_message = 'MFA用プロファイルの認証情報更新が完了しました。'

    # 最終的なプロファイル情報をファイルに書き込む
    with open(AWS_CREDENTIAL_PATH, mode='w') as fd:
        for credential in aws_credential_dict.values():
            fd.write(credential.export_string() + '\n')
    
    print(final_message)


if __name__ == '__main__':
    main()
