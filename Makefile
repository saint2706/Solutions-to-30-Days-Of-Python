.PHONY: lint format

NB_FILES := $(shell git ls-files '*.ipynb')
MD_FILES := $(shell git ls-files '*.md')

lint:
	ruff check .
	ruff format --check .
	@if [ -n "$(NB_FILES)" ]; then \
		nbqa black --check $(NB_FILES); \
		nbqa ruff $(NB_FILES); \
	else \
		echo "No notebooks found."; \
	fi
	@if [ -n "$(MD_FILES)" ]; then \
		mdformat --check $(MD_FILES); \
	else \
		echo "No Markdown files found."; \
	fi

format:
	ruff check --fix .
	ruff format .
	@if [ -n "$(NB_FILES)" ]; then \
		nbqa black $(NB_FILES); \
		nbqa ruff --fix $(NB_FILES); \
	else \
		echo "No notebooks found."; \
	fi
	@if [ -n "$(MD_FILES)" ]; then \
		mdformat $(MD_FILES); \
	else \
		echo "No Markdown files found."; \
	fi
