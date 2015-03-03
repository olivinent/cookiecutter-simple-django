import filecmp
import os
import shutil
import subprocess
import tempfile
import unittest

class TestTreeCreation(unittest.TestCase):

    destpath = os.path.join(tempfile.gettempdir(), 'my-awesome-project')
    comparepath = os.path.join(os.path.dirname(__file__), 'sample_app', 'my-awesome-project')

    def setUp(self):
        if os.path.exists(self.destpath):
            shutil.rmtree(self.destpath)

    def test_files_created(self):
        status = subprocess.call(
            ['cookiecutter', '--no-input', os.path.dirname(os.path.dirname(__file__))])

        if status == 0:
            shutil.move(
                os.path.join(os.path.dirname(os.path.dirname(__file__)),'my-awesome-project'),
                self.destpath
                )
        self.assertEqual(
            filecmp.dircmp(
                self.comparepath,
                self.destpath).diff_files,
            [])

if __name__ == '__main__':
    unittest.main()
