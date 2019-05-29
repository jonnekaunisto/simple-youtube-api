import os
import pytest
import rstvalidator
from docutils.core import publish_parts

README_FILE_NAME = "README.rst"


def validate_rst_file(path):
    with open(path, 'r') as rst_file:
        text = rst_file.read()

    try:
        parts = publish_parts(source=text, writer_name="html4css1")
        print(parts)
    except:
        print("failed")


def test_readme_format():
    project_path = os.path.abspath(os.curdir)

    readme_path = project_path + os.sep + README_FILE_NAME

    if not os.path.isfile(readme_path):
        os.chdir('..')
        project_path = os.path.abspath(os.curdir)
        readme_path = project_path + os.sep + README_FILE_NAME

    errors = rstvalidator.rstvalidator(readme_path)

    assert len(errors) == 0, " | ".join(errors)

if __name__ == "__main__":
    pytest.main()
