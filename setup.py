from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("dataanalysis/version.py", "r") as version_file:
    __version__ = version_file.read().split("=")[1].strip().strip('"')

setup(
    name="dataanalysis-kd",
    version=__version__,
    author="David Kane",
    author_email="david@dkane.net",
    packages=["dataanalysis", "dataanalysis.utils"],
    description="Python utilities for doing data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kanedata/data-analysis",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "xlsxwriter",
        "openpyxl",
    ],
)
