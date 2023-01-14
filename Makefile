install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

#game-even:
#	poetry run brain-even

#game-calc:
#	poetry run brain-calc

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

#package-reinstall:
#	pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build