.PHONY: install runserver venv help

help:
	@echo "Makefile targets: venv, install, runserver"

venv:
	python3 -m venv octofit-tracker/backend/venv

install: venv
	. octofit-tracker/backend/venv/bin/activate && pip install -r octofit-tracker/backend/requirements.txt

runserver:
	. octofit-tracker/backend/venv/bin/activate && python octofit-tracker/manage.py runserver 0.0.0.0:8000
