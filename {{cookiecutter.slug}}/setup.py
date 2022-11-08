"""Sets up package"""

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


with open("requirements.txt", "r", encoding="utf-8") as fs:
    install_requires = [str(r) for r in parse_requirements(fs.read())]

setup(
    name="{{cookiecutter.slug}}",
    version="0.0.1",
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    url="{{cookiecutter.github_repo}}",
    packages=find_packages(".", include=["{{cookiecutter.package_name}}*"]),
    install_requires=install_requires,
)
