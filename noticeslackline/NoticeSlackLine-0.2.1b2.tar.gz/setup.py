import setuptools

setuptools.setup(
    name="NoticeSlackLine",
    version="0.2.1b2",
    description="Notice to Slack or LINE.",
    author="yoshida",
    author_email="yoshida.pypi@gmail.com",
    url="https://github.com/yoshida121/NoticeSlackLine",
    packages=setuptools.find_packages(),
    install_requires=["requests"]
)