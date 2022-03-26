#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Chase M Clark",
    author_email="chasingmicrobes@gmail.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        "console_scripts": [
            "clusterrule_json=clusterrule.cli.entry_json_template:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="clusterrule",
    name="clusterrule",
    packages=find_packages(include=["clusterrule", "clusterrule.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/chasemc/clusterrule",
    version="0.1.0",
    zip_safe=False,
)
