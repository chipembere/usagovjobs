test:
	poetry run pytest -vv

format-check:
	poetry run black --check usagovjobs/ tests/

black-format:
	poetry run black usagovjobs/ tests/