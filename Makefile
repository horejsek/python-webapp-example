.PHONY: all prepare-dev venv lint test run shell clean build install
SHELL=/bin/bash

VENV_NAME?=venv
VENV_BIN=$(shell pwd)/${VENV_NAME}/bin
VENV_ACTIVATE=. ${VENV_BIN}/activate

PYTHON=${VENV_BIN}/python3

FLASK=${VENV_BIN}/flask
export FLASK_ENV=development
export FLASK_APP=webapp.app

export WEBAPP_ENV?=dev
export WEBAPP_SECRET_KEY=devkey


all:
	@echo "make prepare-dev"
	@echo "    Create python virtual environment and install dependencies."
	@echo "make lint"
	@echo "    Run list on project."
	@echo "make test"
	@echo "    Run tests on project."
	@echo "make run"
	@echo "    Run server."
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."
	@echo "make build"
	@echo "    Creates debian package."
	@echo "make install"
	@echo "    Installs package in your system."


prepare-dev:
	which dpkg-buildpackage || apt install -y debhelper dh-virtualenv dh-systemd lintian

	which python3 || apt install -y python3 python3-pip
	which virtualenv || python3 -m pip install virtualenv
	make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip setuptools
	${PYTHON} -m pip install -e .[devel]
	touch $(VENV_NAME)/bin/activate

lint: venv
	${PYTHON} -m pylint --rcfile=pylintrc webapp
	${PYTHON} -m mypy --ignore-missing-imports webapp

test: venv
	${PYTHON} -m pytest -vv tests

run: venv
	${FLASK} run

shell: venv
	${FLASK} shell

clean:
	find . -name '*.pyc' -exec rm --force {} +
	rm -rf $(VENV_NAME) *.eggs *.egg-info dist build docs/_build .cache

build: venv
	dpkg-buildpackage -us -uc -b
	lintian ../webapp_1.0_all.deb

install:
	-dpkg -i ../webapp_1.0_all.deb
	apt install -f
