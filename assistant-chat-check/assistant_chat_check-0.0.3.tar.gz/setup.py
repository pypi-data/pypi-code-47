from setuptools import setup
import pathlib

requires = [
    "sklearn", "pymongo", "pubsub_ncs"
]
VERSION = ""
_ROOT = pathlib.Path(__file__).parent
with open(str(_ROOT / 'assistant_chat_check' / '__init__.py')) as f:
    for line in f:
        print(line)
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break
    if VERSION == "":
        raise RuntimeError(
            'unable to read the version from assistant_chat_check/__init__.py')

packages = [
    "assistant_chat_check"
]
setup(
    name='assistant_chat_check',
    version=VERSION,
    description='gensim生成モデルの評価',
    url='https://gitlab.com/assistant-service/assistant-chat-keras.git',
    author='nozomi.nishinohara',
    author_email='nozomi.nishinohara@n-creativesystem.com',
    keywords='',
    packages=packages,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        "console_scripts": [
            "chat_check = assistant_chat_check.main:main"
        ]
    }
)
