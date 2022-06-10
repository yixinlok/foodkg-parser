.PHONY: setup

env = env/bin/activate
python = . $(env); LC_CTYPE=C.UTF-8 python

all: run

run: 
	$(python) main.py

setup: requirements.txt
	python -m pip install --user virtualenv
	python -m virtualenv -p python3 env
	$(python) -m pip install -r requirements.txt
	$(python) load_index.py