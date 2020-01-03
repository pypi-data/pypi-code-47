import glob
import os
import os.path
import pathlib
import sys

from setuptools import find_packages, setup
from distutils.command.build_py import build_py

if sys.version_info < (3, 6):
    sys.exit("Please use Python version 3.6 or higher.")

project_dir = os.path.dirname(os.path.abspath(__file__))
version_file_path = os.path.join(project_dir, "__version__.py")
readme_file_path = os.path.join(project_dir, "../README.md")

# path to xain proto
proto_path = "../src/"

# get version
version = {}
with open(version_file_path) as fp:
    exec(fp.read(), version)


# get readme
with open(readme_file_path, "r") as fp:
    readme = fp.read()


# Handle protobuf
class BuildPyCommand(build_py):
    def run(self):
        # we need to import this here or else these packages would have to be
        # installed in the system before we could run the setup.py
        import numproto
        import grpc_tools
        from grpc_tools import protoc

        # get the path of the numproto protofiles
        # this will give us the path to the site-packages where numproto is
        # installed
        numproto_path = pathlib.Path(numproto.__path__[0]).parent

        # get the path of grpc_tools protofiles
        grpc_path = grpc_tools.__path__[0]

        proto_files = [
            name.replace(f"{proto_path}/", "")
            for name in glob.glob("../src/xain_proto/fl/*.proto")
        ]

        os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

        for proto_file in proto_files:
            command = [
                "grpc_tools.protoc",
                # path to numproto .proto files
                f"--proto_path={numproto_path}",
                # path to google .proto files
                f"--proto_path={grpc_path}/_proto",
                f"--proto_path={proto_path}",
                "--python_out=./",
                "--grpc_python_out=./",
                # "--mypy_out=./",
                proto_file,
            ]

            print("Building proto_file {}".format(proto_file))
            if protoc.main(command) != 0:
                raise Exception("error: {} failed".format(command))

        build_py.run(self)


setup_requires = [
    "protobuf~=3.9",  # BSD
    "grpcio~=1.23",  # Apache License 2.0
    "grpcio-tools~=1.23",  # Apache License 2.0
    "numproto~=0.3",  # Apache License 2.0
    # "mypy==0.750",  # MIT License
    # "mypy-protobuf==1.16",  # Apache License 2.0
    "wheel==0.33.6",  # MIT
]

setup(
    name="xain-proto",
    version=version["__version__"],
    description="XAIN Protocol Buffers",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/xainag/xain-proto",
    author=["XAIN AG"],
    author_email="services@xain.io",
    license="Apache License Version 2.0",
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(),
    setup_requires=setup_requires,
    cmdclass={"build_py": BuildPyCommand},
    package_data={"xain_proto": ["fl/*.pyi"]},
)
