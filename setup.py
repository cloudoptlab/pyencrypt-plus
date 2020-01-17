"""
@file: setup.py.py
@time: 2020/1/17 14:21
@description: Helper for upload to pipy.
"""

from setuptools import setup, find_packages

setup(
    name="pyencrypt-plus",
    version="1.0.0",
    keywords=["pip", "encrypt", "rsa", "aes", "md5", "base64"],
    description="This is a powerful and simple Python encryption library.",
    long_description="This is a powerful and simple Python encryption library."
                     "https://github.com/cloudoptlab/pyencrypt-plus",
    license="Apache-2.0",

    url="https://github.com/cloudoptlab/pyencrypt-plus",
    author="Cloudopt",
    author_email="support@cloudopt.net",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pycryptodome==3.9.4"]
)
