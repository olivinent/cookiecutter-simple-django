.PHONY: install app

install:
	pip install -r requirements.txt

# Derived from http://stackoverflow.com/a/6273809/2390312
app:
	python manage.py create_app -p {{cookiecutter.repo_name}}/apps $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
