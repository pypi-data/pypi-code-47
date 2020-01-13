import setuptools

long_desc = "An easy to use python library consisting implementation of Continuous Density Hidden Markov Models.After studying Hidden Markov Models(HMM) for a while now, I have came across many python libraries which implements HMM algorithms like forward,  backward, Viterbi and Baum-Welch. However, most of these libraries work on discrete observations. Continuous Density Hidden Markov Models(CD-HMM) are a type of HMM which consists of Emission probabilities in the form of a distribution like gaussian or uniform distribution. Despite its use in Speech processing, very less codes are available on the internet regarding CD-HMM. This library has implementation of all HMM algorithms applied on continuous density observations."

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdhmm-ashishmokalkar", 
    version="0.0.2",
    author="Ashish Mokalkar",
    author_email="ashishmokalkar79@gmail.com",
    description="Python Library for Continuous Desity Hidden Markov Model which is widely used in Speech Recognition.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/ashishmokalkar/cdhmm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)