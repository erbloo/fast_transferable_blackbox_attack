from setuptools import setup
from setuptools import find_packages

requirements = [
    'numpy',
    'opencv-python'
]

setup(
    name='fta',
    description='Code for fast transferable blackbox adversarial attack.',
    version='1.0',
    url="https://github.com/anonymous202201/anonymous202201",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)
