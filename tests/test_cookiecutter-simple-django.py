import shutil
import unittest
from os.path import abspath, dirname, exists, isdir, join

from cookiecutter.main import cookiecutter


class TestHook(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
