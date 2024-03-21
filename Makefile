install:
	# pip install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	black *.py chapter7/*.py
lint:
	# run lint
	pylint --disable=R,C *.py chapter7/*.py
test:
	# test code
	python -m pytest -vv --cov=chapter7 test_cases.py
build:
	# build containers
deploy:
	# deploy code
all: install format lint test deploy
