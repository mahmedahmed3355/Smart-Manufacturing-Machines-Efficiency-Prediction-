from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-9",
    version="0.1",
    author="Mohamed Ahmed",
    packages=find_packages(),
    install_requires = requirements,
)
