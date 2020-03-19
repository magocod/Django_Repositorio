from setuptools import find_packages, setup

from djrepo import __version__

setup(
    name="djrepo",
    version=__version__,
    url="https://github.com/magocod/djrepo",
    author="Yson",
    author_email="androvirtual12@gmail.com",
    description="Digital repository, UNEFA internship project",
    python_requires=">=3.7",
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
