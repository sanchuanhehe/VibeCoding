.PHONY: docs clean lint-md lint-md-fix

docs:
	uv run sphinx-build -W --keep-going -b html docs docs/_build/html

lint-md:
	npx markdownlint-cli "**/*.md" --ignore docs/_build

lint-md-fix:
	npx markdownlint-cli "**/*.md" --ignore docs/_build --fix

clean:
	rm -rf docs/_build
