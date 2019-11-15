# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vPhon",
    version="0.3.2",
    author="James Kirby",
    author_email="j.kirby@ed.ac.uk",
    description="A Vietnamese phonetizer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirbyj/vPhon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)
