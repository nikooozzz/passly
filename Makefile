.PHONY: setup run lint format test clean

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install .[dev]
	.venv/bin/pre-commit install

run:
	.venv/bin/passly --help

lint:
	flake8 src tests

format:
	black src tests

test:
	pytest tests

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache build/ dist/ pkg/
	find . -type d -name "*.egg-info" -exec rm -rf {} +