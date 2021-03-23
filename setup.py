from setuptools import setup

setup(
   name='web-text-reader',
   version='1.0',
   description='Python to extract information from web pages',
   author='tiwardus',
   packages=['web-text-reader'],
   install_requires=['requests', 'lxml'], #external packages as dependencies
)