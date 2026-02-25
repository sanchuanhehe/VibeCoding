project = "VibeCoding Docs"
author = "VibeCoding"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]

root_doc = "index"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
