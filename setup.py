import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Outcrop",
    version="1.0.0",
    author="-",
    description="API for Minecraft Bedrock websockets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["outcrop"],
    package_dir={'':'outcrop/src'},
    install_requires=["websockets"]
)