from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='Artwrk-Backend',
    version='0.0.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    package_dir={'': 'artwrk','':'tests'},
    packages=find_packages(where=''),
    python_requires='>=3.7, <4',
    install_requires=['pynamodb','pyjwt','schema'],
)