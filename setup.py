import sys
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

MAJOR               = 0
MINOR               = 2
MICRO               = 5
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


class PyTest(TestCommand):
    """Handle test execution from setup."""

    user_options = [('pytest-args=', 'a', "Arguments to pass into pytest")]

    def initialize_options(self):
        """Initialize the PyTest options."""
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def finalize_options(self):
        """Finalize the PyTest options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run the PyTest testing suite."""
        try:
            import pytest
        except ImportError:
            raise ImportError('Running tests requires additional dependencies.'
                              '\nPlease run (pip install moviepy[test])')

        errno = pytest.main(self.pytest_args.split(" "))
        sys.exit(errno)


cmdclass = {'test': PyTest}  # Define custom commands.


# Define the requirements for specific execution needs.
requires = [
    "google-api-python-client>=1.7.7",
    "google-auth>=1.6.2",
    "google-auth-httplib2>=0.0.3",
    "oauth2client>=4.1.3",
    "pytube3>=9.5.11",
    "decorator>=4.4.0",
    "progressbar2>=3.42.0"
]

test_reqs = [
    'pytest-cov>=2.5.1',
    'pytest>=3.0.0',
    'coveralls>=1.1,<2.0',
    'docutils>=0.14',
    'rstvalidator'
]

with open('README.rst', 'r', 'utf-8') as fh:
    long_description = fh.read()

setup(
    name="simple-youtube-api",
    version=VERSION,
    author="Jonne Kaunisto",
    author_email="jonneka@gmail.com",
    description="A python YouTube API wrapper",
    long_description=long_description,
    url="https://github.com/jonnekaunisto/simple-youtube-api",
    license='MIT License',
    keywords="youtube",
    packages=find_packages(exclude='docs'),
    cmdclass=cmdclass,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    tests_require=test_reqs,
)
