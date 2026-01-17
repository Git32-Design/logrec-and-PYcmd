# This is a setup script for a Python package using setuptools.
import setuptools import setup, find_packages

with open("About logrec and PYcmd.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description += "\n" + fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()


setup(
    name="lrapc",
    version="3.7.3",
    author="Git32-Design",
    author_email="git32mail@qq.com",
    description="A quick record log's lib, Can search log file, And record(Or write) logs to a file. It's easy, Please use \"logging\" library. I know, My lib is sucks, But I well publish it to github."
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Git32-Design/logrec-and-PYcmd",

    packages=find_packages(),
    install_requires=requirements,

    classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Logging",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
    ],
    python_requires=">=3.8"
)