.PHONY: install test lint data train evaluate

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

data:
	python -m forecast.ingest.eirgrid

train:
	@echo "TODO: training entrypoint"

evaluate:
	@echo "TODO: evaluation entrypoint"
