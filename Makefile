install:
	poetry install

start:
	poetry run brain-games

game-even:
	poetry run brain-even

game-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install lint build