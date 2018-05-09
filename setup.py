import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='book-python-wrappers',
      version='0.0.0',
      install_requires=requirements,
      description='ZohoBooks Python Client Library',
      long_description=read('README.md'),
      url='https://github.com/zoho/books-python-wrappers',
      download_url='',
      author='SahayaRamesh',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
     )
