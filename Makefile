format: style lint type

style:
	isort --atomic . tests
	black . tests

lint:
	flake8 . tests
	autoflake  --recursive . tests

type:
	mypy --strict settings.py conftest.py tests

