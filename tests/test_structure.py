import os
import shutil
from tempfile import mkdtemp
from unittest import TestCase

from cookiecutter.main import cookiecutter

EXPECTED_STRUCTURE = [('../{{ cookiecutter.repo_name }}',
                       ['data', 'docs', 'models', 'notebooks', 'references', 'reports', 'src'],
                       ['.env', '.gitignore', 'LICENSE', 'Makefile', 'README.md', 'requirements.txt', 'tox.ini']),

                        ('../{{ cookiecutter.repo_name }}/data', ['external', 'interim', 'processed', 'raw'], []),
                            ('../{{ cookiecutter.repo_name }}/data/external', [], ['.gitkeep']),
                            ('../{{ cookiecutter.repo_name }}/data/interim', [], ['.gitkeep']),
                            ('../{{ cookiecutter.repo_name }}/data/processed', [], ['.gitkeep']),
                            ('../{{ cookiecutter.repo_name }}/data/raw', [], ['.gitkeep']),

                        ('../{{ cookiecutter.repo_name }}/docs',
                         [],
                         ['commands.rst', 'conf.py', 'getting-started.rst', 'index.rst', 'make.bat', 'Makefile']),

                        ('../{{ cookiecutter.repo_name }}/models', [], ['.gitkeep']),
                        ('../{{ cookiecutter.repo_name }}/notebooks', [], ['.gitkeep']),
                        ('../{{ cookiecutter.repo_name }}/references', [], ['.gitkeep']),
                        ('../{{ cookiecutter.repo_name }}/reports', ['figures'], ['.gitkeep']),
                            ('../{{ cookiecutter.repo_name }}/reports/figures', [], ['.gitkeep']),
                        ('../{{ cookiecutter.repo_name }}/src', ['data', 'features', 'model', 'visualization'], ['__init__.py']),
                            ('../{{ cookiecutter.repo_name }}/src/data', [], ['.gitkeep', 'make_dataset.py']),
                            ('../{{ cookiecutter.repo_name }}/src/features', [], ['.gitkeep', 'build_features.py']),
                            ('../{{ cookiecutter.repo_name }}/src/model', [], ['.gitkeep', 'predict_model.py', 'train_model.py']),
                            ('../{{ cookiecutter.repo_name }}/src/visualization', [], ['.gitkeep', 'visualize.py'])]

class TestStructure():
    """ Sanity test to make sure that expected project structure is created by cookiecutter.
    """
    @classmethod
    def setup_class(cls):
        cls.dir = mkdtemp()

    def test_structure(self):
        cookiecutter(os.path.join(os.path.split(__file__)[0], os.pardir),
                     no_input=True,
                     output_dir=self.dir)

        for i, walk in enumerate(os.walk(os.path.join(self.dir, 'project_name'))):
            root, dirs, files = walk

            assert dirs == EXPECTED_STRUCTURE[i][1]
            assert files == EXPECTED_STRUCTURE[i][2]

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls.dir)
