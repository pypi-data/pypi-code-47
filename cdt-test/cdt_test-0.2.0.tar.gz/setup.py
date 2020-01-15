from setuptools import find_packages, setup
setup(
    name='cdt_test',
    version='0.2.0',
    description='This is a cdt test to assist doctor',
    url='https://github.com/ZihaoLian/CDT',
    author='zihaoLian',
    author_email='2043740417@qq.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={'': ['*.m', '*.model', '*.csv', 'cdt.ckpt-31300.data-00000-of-00001', 'cdt.ckpt-31300.index',
                       'cdt.ckpt-31300.meta', 'checkpoint']},
    install_requires=['scikit-learn==0.21.0', 'numpy>=1.15.2', 'matplotlib>=3.0.3', 'scipy>=1.3.1',
                      'tensorflow==1.14.0', 'pillow==6.1.0', 'lime==0.1.1.36', 'opencv-python==3.4.2.16']
)
