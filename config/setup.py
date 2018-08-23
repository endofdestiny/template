from setuptools import setup, find_packages
import json


with open('./config/config.json') as config_file:
    config = json.load(config_file)

setup(
    name=config['name'],
    version=config['version'],
    description=config['description'],
    packages=find_packages('src'),
    package_dir={'':'src'},
    long_description=open('README.md').read()
)
