.PHONY: lint test all

test:
	py.test -q tests/*.py

lint:
	pep8 --ignore E201,E202 --max-line-length=85 --exclude='{{cookiecutter.repo_name}}/docs' .

all: lint test
