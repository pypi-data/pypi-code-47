import requests


def avatar(usuario):

    """
    Busca o avatar de um usuário no Github
    :param usuario: string com nome do usuario no github
    :return: string com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(avatar('adilmarmorandi'))
