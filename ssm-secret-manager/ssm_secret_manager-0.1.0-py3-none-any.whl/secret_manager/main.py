import boto3


class SecretManager:
    def __init__(self, region_name='us-east-1', secrets_mapping={}):
        self.ssm = boto3.client('ssm', region_name=region_name)
        self.secrets = {}
        self.load_secrets(secrets_mapping)

    def get_secret(self, secret_name):
        if not self.secrets.get(secret_name):
            print(
                'Secret not loaded yet. Please load the secret using '
                '.load_secret("{}", secret_key) first or update the config to include this secret'.format(
                    secret_name
                )
            )
            return None

        return self.secrets[secret_name]

    def load_secret(self, secret_name, secret_key):
        self.load_secrets({
            secret_name: secret_key
        })

    def load_secrets(self, secrets_dict):
        for secret_name, secret_key in secrets_dict.items():
            self.secrets[secret_name] = self.ssm.get_parameter(
                Name=secret_key,
                WithDecryption=True
            ).get('Parameter', {}).get('Value', '')
