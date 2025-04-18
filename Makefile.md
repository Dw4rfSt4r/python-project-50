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
gendiff:
    uv run gendiff