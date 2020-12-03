import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ciphers",
    version="0.0.2",
    author="Anderson Evitt",
    author_email="andersonevitt@protonmail.com",
    description="A library containing many ciphers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andersonevitt/ciphers",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires='>=3.0',
)
