from setuptools import setup, find_packages

VERSION = "1.0.0"


setup(
    maintainer="Alex Clark",
    maintainer_email="aclark@aclark.net",
    name='Products.ifQuotes',
    packages=find_packages(),
    namespace_packages=[
        'Products'
    ],
    install_requires=[
        'setuptools',
    ],
    url="https://github.com/collective/Products.ifQuotes",
    version=VERSION,
)