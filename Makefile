.PHONY: docs clean

docs:
	uv run sphinx-build -W --keep-going -b html docs docs/_build/html

clean:
	rm -rf docs/_build
