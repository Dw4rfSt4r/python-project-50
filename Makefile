.PHONY: install build package-install package-reinstall test gendiff lint lint-fix

install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=diff_generator --cov-report xml --cov-report term
	
gendiff:
	uv run gendiff

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix
