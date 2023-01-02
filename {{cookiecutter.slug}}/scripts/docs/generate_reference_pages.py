"""Generate the code reference pages."""


from pathlib import Path

import mkdocs_gen_files


nav = mkdocs_gen_files.Nav()

# Project source
project_dir = Path("src") / "{{ cookiecutter.slug }}"

# Documentation destination
ref_docs_dir = Path("reference")

# Set certain patterns to ignore
ignore_glob_patterns = [
    "__pycache__/*",
    "__main__.py",
]

ignored_files = {
    ignored_file
    for ignore_glob_pattern in ignore_glob_patterns
    for ignored_file in project_dir.rglob(ignore_glob_pattern)
}

# Recursively find all Python files
for path in list(project_dir.rglob("*.py")):
    if path in ignored_files:
        continue

    module_path = path.relative_to(project_dir).with_suffix("")  # Removes `.py`
    doc_path = path.relative_to(project_dir).with_suffix(".md")  # Adds `.md`
    full_doc_path = Path("reference", doc_path)

    parts = list(module_path.parts)

    # Handle `__init__.py` files
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")

    # Prepend "{{ cookiecutter.slug }}" to parts
    parts = ["{{ cookiecutter.slug }}", *parts]

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)

        content = f"""---
title: {parts[-1]}
---

::: {identifier}
"""

        print(content, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:  #
    nav_file.writelines(nav.build_literate_nav())
