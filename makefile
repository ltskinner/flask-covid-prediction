
setup:
	python -m venv ~/.flask-covid

source:
	. ~/.flask-covid/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint-force:
	isort .
	black .

lint-check:
	isort . --check-only
	black --check .
	flake8 .
	pylint --disable=R,C,pointless-string-statement ./*.py ./tests

test:
	coverage run -m pytest -vv ./tests
	coverage report -m

train:
	python train.py

run:
	python application.py