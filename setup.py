from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="comandi",
    version="0.0.2",
    author="Sagnik Bhattacharjee",
    author_email="bhattacharjeesagnik910@gmail.com",
    description="A CLI tool for command-line instructions and code analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datavorous/comandi",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'comandi': ['prompt.json'],
    },
    install_requires=[
        "rich",
        "meta_ai_api",  
    ],
    entry_points={
        "console_scripts": [
            "comandi=comandi.main:cli_main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)