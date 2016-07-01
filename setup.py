from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='afilnet',
    version='1.0.1',
    packages=['afilnet'],
    description='This package is an easy way to use send sms, email and voice(texto-to-speech) using Afilnet services',
    long_description=long_description,
    author='Afilnet Cloud Marketing',
    author_email='soporte@afilnet.com',
    url='http://github.com/afilnet/api-python',
    license='MIT',
    keywords='afilnet sms email voice message phone call notification cloud marketing service',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


)