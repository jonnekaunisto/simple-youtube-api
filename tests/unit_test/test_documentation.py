import os
import pytest
import rstcheck
from docutils.utils import Reporter

README_FILE_NAME = "README.rst"
file_path = os.path.dirname(os.path.realpath(__file__))
project_path = file_path + os.sep + ".." + os.sep + ".."
README_PATH = project_path + os.sep + README_FILE_NAME


def test_readme_format():
    with open(README_PATH, "r") as rst_file:
        text = rst_file.read()
    errors = list(rstcheck.check(text, report_level=Reporter.WARNING_LEVEL))
    assert len(errors) == 0, errors


if __name__ == "__main__":
    pytest.main()
