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
        lineiter = (line.strip() for line in requirements_file)
        return [line for line in lineiter if line and not line.startswith("#")]


def setup():
    setuptools.setup(
        name="gym_eyesim",
        version=read_version(),
        packages=setuptools.find_packages(),
        install_requires=read_requirements(),
        description="EyeSim Gym Env",
        long_description=read_readme(),
        long_description_content_type="text/markdown",
        url="https://gitlab.com/felixwege/gym-eyesim",
        author="Felix Wege",
        author_email="felix.wege@tuhh.de",
        license="GPLv3",
    )


if __name__ == "__main__":
    setup()
