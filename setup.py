from distutils.core import setup
setup(
    name='codeshot',
    packages=['codeshot'],
    version='0.1',
    description='convert code file to image',
    author='Zhongqiang Shen',
    author_email='shenzhongqiang@msn.com',
    url='https://github.com/pythonml/codeshot',
    packages=setuptools.find_packages(),
    install_requires=['selenium', 'pygments']
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console+scripts': [
            'codeshot= codeshot:main'
        ],
    },
)
