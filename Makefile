test:
	py.test -q tests/*.py

lint:
	pep8 --ignore E201,E202 --max-line-length=80 --exclude='{{cookiecutter.repo_name}}/docs' .
