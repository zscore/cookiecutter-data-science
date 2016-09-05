.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = {{ cookiecutter.s3_bucket }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

requirements:
	pip install -q -r requirements.txt

data: requirements
	python src/data/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

lint:
	flake8 --exclude=lib/,bin/ .

sync_data_to_s3:
	aws s3 sync data/ s3://$(BUCKET)/data/

sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ data/

{% if cookiecutter.include_virtualenv == 'yes' %}
create_venv:
	pip install -q virtualenv,virtualenvwrapper
	mkvirtualenv {{ cookiecutter.repo_name }}

start_venv:
	workon {{ cookiecutter.repo_name }}
{% endif %}

{% if cookiecutter.include_virtualenv == 'yes' %}
create_venv:
	pip install -q virtualenv,virtualenvwrapper
	mkvirtualenv {{ cookiecutter.repo_name }}

start_venv:
	workon {{ cookiecutter.repo_name }}
{% endif %}

{% if cookiecutter.include_virtualenv == 'yes' %}
create_venv:
	pip install -q virtualenv,virtualenvwrapper
	mkvirtualenv {{ cookiecutter.repo_name }}

start_venv:
	workon {{ cookiecutter.repo_name }}
{% endif %}

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
