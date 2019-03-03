import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-youtube-api",
    version="0.0.1",
    author="Jonne Kaunisto",
    author_email="jonneka@gmail.com",
    description="A python YouTube API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonnekaunisto/simple-youtube-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)