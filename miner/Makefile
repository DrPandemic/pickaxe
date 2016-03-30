install:
	pip install -r requirements.txt

UNIT_TESTS=unittest discover -p '*_test.py'

test:
	python -m $(UNIT_TESTS)

coverage:
	coverage run -m --branch $(UNIT_TESTS)
