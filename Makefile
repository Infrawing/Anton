################################################################################
# Project		: Raptor
# File			: Makefile
# Version		: v1.0
# Created By		: Chirag <infrawing@gmail.com>
# Description		: Makefile to automate tasks
################################################################################

ENVIRONMENT = venv

environment:
	virtualenv -p /usr/bin/python3 $(ENVIRONMENT)

install-dep:
	pip install -r dependencies

export-dep:
	pip freeze > dependencies

clean: 
	py3clean .