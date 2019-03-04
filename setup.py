import setuptools

# Define the requirements for specific execution needs.
requires = [
	"cachetools>=3.1.0",
	"google-api-python-client>=1.7.7",
	"google-auth>=1.6.2",
	"google-auth-httplib2>=0.0.3",
	"httplib2>=0.12.1",
	"oauth2client>=4.1.3",
	"pyasn1>=0.4.5",
	"pyasn1-modules>=0.2.4",
	"rsa>=4.0",
	"six>=1.12.0",
	"uritemplate>=3.0.0"
]

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-youtube-api",
    version="0.0.3",
    author="Jonne Kaunisto",
    author_email="jonneka@gmail.com",
    description="A python YouTube API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonnekaunisto/simple-youtube-api",
    license='MIT License',
    keywords="youtube",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires
)