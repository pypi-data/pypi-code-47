from distutils.core import setup

setup(
    name='gmodviz',
    packages=['gmodviz'],  # Chose the same as "name"
    version='0.0.1',
    license='MIT',
    description='TYPE YOUR DESCRIPTION HERE',
    author='Josep de Cid',
    author_email='josep.de.cid@gmail.com',
    url='https://github.com/jdecid/gmodviz',
    download_url='https://github.com/jdecid/gmodviz/archive/v_01.tar.gz',
    keywords=['Generative', 'Model', 'Visualization', 'Visualizer', 'Viewer'],
    install_requires=[
        'Flask'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
