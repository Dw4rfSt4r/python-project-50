install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
gendiff:
	poetry run gendiff
lint:
	poetry run flake8 gendiff
test-gendiff:
	poetry run pytest
test-verbose:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov
