# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='gisa', # This is the name of the package
    version='1.0.2', # The release version
    description=(
        "Gisa is a Python package that converts numbers into Malagasy words."
        "Returns its corresponding Malagasy word representation."
    ),
    long_description=long_description, # README.md
    long_description_content_type="text/markdown",
    author='Matt Nix',
    author_email='dorints.mg@gmail.com',
    url='https://github.com/mattnix4/gisa',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.7",  # Name of the python package
)
