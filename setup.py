# -*- encoding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cityloc",
    version="0.1.1",
    author="Sveinbjorn Thordarson",
    author_email="sveinbjorn@sveinbjorn.org",
    license='BSD',
    url="https://github.com/sveinbjornt/cityloc",
    description="Look up world city coordinates and country codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=['cityloc'],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    zip_safe=False
)
