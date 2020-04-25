import os
import pytest
import rstcheck
from docutils.utils import Reporter

README_FILE_NAME = "README.rst"
project_path = os.path.abspath(os.curdir)
README_PATH = project_path + os.sep + README_FILE_NAME


def test_readme_format():
    with open(README_PATH, "r") as rst_file:
        text = rst_file.read()
    errors = list(rstcheck.check(text, report_level=Reporter.WARNING_LEVEL))
    assert len(errors) == 0, errors


if __name__ == "__main__":
    pytest.main()
