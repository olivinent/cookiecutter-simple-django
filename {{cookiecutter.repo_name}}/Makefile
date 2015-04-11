.PHONY: setup app

setup:
	pip install -r requirements.txt
	pip install -r requirements/local.txt
	python manage.py migrate

# Derived from http://stackoverflow.com/a/6273809/2390312
app:
	python manage.py create_app -p {{cookiecutter.repo_name}}/apps $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
