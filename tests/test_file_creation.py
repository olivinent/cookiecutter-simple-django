import filecmp
import shutil
import subprocess
import tempfile
import unittest
from os.path import abspath, dirname, exists, join


class TestTreeCreation(unittest.TestCase):

    destpath = join(tempfile.gettempdir(), 'my-awesome-project')
    comparepath = join(
        dirname(__file__),
        'sample_app',
        'my-awesome-project')

    def setUp(self):
        if exists(self.destpath):
            shutil.rmtree(self.destpath)

    def test_files_created(self):
        status = subprocess.call(
            ['cookiecutter', '--no-input', dirname(dirname(__file__))])

        if status == 0:
            shutil.move(
                join(dirname(dirname(__file__)), 'my-awesome-project'),
                self.destpath)

        self.assertEqual(
            filecmp.dircmp(self.comparepath, self.destpath).diff_files,
            [])

if __name__ == '__main__':
    unittest.main()
