# setup.py
from setuptools import setup, find_packages


def read_requirements(file):
    """read the necessary dependencies from requirements.txt"""
    with open(file, "r", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="my_tool",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "my_tool=my_tool.main:main",  # Command name and entry point
        ],
    },
    install_requires=read_requirements("requirements.txt"),  # Read dependencies
)
