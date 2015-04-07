import os
import re
import shutil
import subprocess
import unittest
from os.path import dirname, exists, isdir, join

from cookiecutter.main import cookiecutter
from cookiecutter.utils import make_sure_path_exists, work_in


class TestAppCreation(unittest.TestCase):
    """Tests for the make app command"""

    destpath = join(dirname(dirname(__file__)), 'my-awesome-project')

    def tearDown(self):
        if exists(self.destpath):
            shutil.rmtree(self.destpath)

    def test_make_app_command_runs_successfully(self):
        cookiecutter(dirname(dirname(__file__)), no_input=True)

        with work_in(self.destpath):
            assert subprocess.call(["make", "app", "testing"]) == 0

        assert make_sure_path_exists(
            join(self.destpath, 'my-awesome-project', 'apps', 'testing')) == True
