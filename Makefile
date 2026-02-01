run-dev:
# 	uvicorn fastapi_study.app:app --reload
# 	fastapi dev fastapi_study.app:app
	fastapi dev fastapi_study/app.py

run-docs:
	mkdocs serve

lint:
	ruff check .

format-code:
	ruff format .

test:
	pytest -s -vv

test-coverage:
	pytest --cov=fastapi_study -vv

test-coverage-report:
	pytest --cov=fastapi_study --cov-report=html -vv

.PHONY: run-dev
