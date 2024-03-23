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
	python -m pytest -vv --cov=chapter7 test_*.py
build:
	# build containers
	docker build -t deploy-web-services .
run:
	# docker run
	# Get the image id from "docker image ls" command and run the following command
	# docker run -p 127.0.0.1:8080:8080 your-image-id
deploy:
	# deploy code
	
all: install format lint test
