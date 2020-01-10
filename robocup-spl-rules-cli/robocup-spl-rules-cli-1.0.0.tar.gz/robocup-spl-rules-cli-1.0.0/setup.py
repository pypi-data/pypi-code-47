import setuptools


def read_version():
    with open("VERSION.txt") as version_file:
        version = version_file.readline()
        return version


def read_readme():
    with open("README.md") as readme_file:
        readme = readme_file.read()
        return readme


def read_requirements():
    with open("requirements.txt") as requirements_file:
        line_iter = (line.strip() for line in requirements_file)
        return [
            line for line in line_iter if line and not line.startswith("#")
        ]


def setup():
    setuptools.setup(
        name="robocup-spl-rules-cli",
        version=read_version(),
        packages=setuptools.find_packages(),
        install_requires=read_requirements(),
        scripts=["rules"],
        description="RoboCup SPL Rules CLI",
        long_description=read_readme(),
        long_description_content_type="text/markdown",
        url="https://gitlab.com/felixwege/robocup-spl-rules-cli",
        author="Felix Wege",
        author_email="felix.wege@tuhh.de",
        license="MIT",
    )


if __name__ == "__main__":
    setup()
