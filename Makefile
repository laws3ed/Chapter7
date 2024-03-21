install:
	# pip install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	black *.py chapter7/*.py
lint:
	# run lint
test:
	# test code
deploy:
	# deploy code
all: install format lint test deploy
