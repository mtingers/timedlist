from distutils.core import setup
import setuptools

setup(
    name='timedlist',
    version='1.0.0',
    author='Matthew Ingersoll',
    author_email='matth@mtingers.com',
    packages=['timedlist',],
    license='MIT License',
    long_description='A self-pruning list based off of time.',
    url='https://github.com/mtingers/timedlist',
    install_requires=open('requirements.txt').read().strip().split('\n'),
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)