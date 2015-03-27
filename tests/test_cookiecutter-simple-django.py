import os
import re
import shutil
import unittest
from os.path import dirname, exists, isdir, join

from cookiecutter.main import cookiecutter


class TestCookiecutterSubstitution(unittest.TestCase):
    """Test that all cookiecutter instances are substituted"""

    cookiecutter(dirname(dirname(__file__)), no_input=True)

    destpath = join(dirname(dirname(__file__)), 'my-awesome-project')

    def tearDown(self):
        if exists(self.destpath):
            shutil.rmtree(self.destpath)

    def test_all_cookiecutter_instances_are_substituted(self):
        # Build a list containing absolute paths to the generated files
        paths = [os.path.join(dirpath, file_path)
                 for dirpath, subdirs, files in os.walk(self.destpath)
                 for file_path in files]

        # Construct the cookiecutter search pattern
        pattern = "{{(\s?cookiecutter)[.](.*?)}}"
        re_obj = re.compile(pattern)

        # Assert that no match is found in any of the files
        for path in paths:
            for line in open(path, 'r'):
                match = re_obj.search(line)
                self.assertIsNone(
                    match,
                    "cookiecutter variable not replaced in {}".format(path))


class TestHook(unittest.TestCase):
    """Tests that the custom hook deletes the docs folder successfully"""

    destpath = join(dirname(dirname(__file__)), 'my-awesome-project')

    def tearDown(self):
        if exists(self.destpath):
            shutil.rmtree(self.destpath)

    def test_project_tree_created_successfully(self):
        cookiecutter(dirname(dirname(__file__)), no_input=True)

        # Assert that the command runs successfully
        self.assertTrue(exists(self.destpath))

    def test_docs_folder_added_by_default(self):
        cookiecutter(dirname(dirname(__file__)), no_input=True)

        # The folder exists and is a directory
        self.assertTrue(exists(join(self.destpath, 'docs')))
        self.assertTrue(isdir(join(self.destpath, 'docs')))

    def test_docs_folder_removed_if_docs_opted_out(self):
        cookiecutter(
            dirname(dirname(__file__)),
            no_input=True,
            extra_context={"with_documentation": "no"})

        self.assertFalse(exists(join(self.destpath, 'docs')))

if __name__ == '__main__':
    unittest.main()
