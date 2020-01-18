import setuptools

setuptools.setup(
    name="simimgs",
    version="0.0.15",
    author="Yefei Li",
    author_email='abc@gmail.com',
    description="A tool for compare image similarities using SSIM",
    long_description_content_type="text/markdown",
    url="https://github.com/liyefei737/simimgs",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'opencv-python', 'scikit-image'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
