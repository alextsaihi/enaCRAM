import setuptools
with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "enaCRAM",
    version = "1.0",
    author = "Alex Tsai",
    author_email = "alextsaihi@gmail.com",
    description = "ENA CRAM Client",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/alextsaihi/enaCRAM",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires  = '>=3.6',
)