<h1 align="center" style="border-bottom: none">
    <b>
        <a href="https://github.com/cookiecutter/cookiecutter/">🥠 Cookiecutter</a> Template for Modern Python Package Projects 🐍<br>
    </b>
</h1>

<div align="center">

A package template that comes pre-configured with `pre-commit`, `conventional-commits`, `mkdocs` docs generation and hosting, `linting` frameworks and a `unit testing` suite out-of-the-box for better python project development.

<div align="center">

## About

</div>

<div align="center">

![](https://img.shields.io/badge/Cookiecutter-D4AA00.svg?style=for-the-badge&logo=Cookiecutter&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white)

</div>

Cookiecutter templates enables developers and data scientists to create projects from a predefined template. This template is a modern Python package project structure that utilizes a number of tools to automate and align with best practices in order to have smoother development. The project template can be viewed from the [structure](structure.md) document. The template creates a project that can be hosted on GitHub and deployed to [PyPI](https://pypi.org/).

<div align="center">

![](https://img.shields.io/badge/pnpm-F69220.svg?style=for-the-badge&logo=pnpm&logoColor=white)
![](https://img.shields.io/badge/commitlint-000000.svg?style=for-the-badge&logo=commitlint&logoColor=white)
![](https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black)
![](https://img.shields.io/badge/Conventional%20Commits-FE5196.svg?style=for-the-badge&logo=Conventional-Commits&logoColor=white)

</div>

This template uses `husky`, `commitlint` and `pre-commit` managed by `pnpm` to use `git` hooks to automate tasks such as linting, formatting, testing, etc. before a commit is made. This ensures that the code is always in a consistent state and that the commit history is clean and easy to read. The commit messages are also linted to ensure that they follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

<div align="center">

![](https://img.shields.io/badge/Material%20Design-757575.svg?style=for-the-badge&logo=Material-Design&logoColor=white)
![](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF.svg?style=for-the-badge&logo=Read-the-Docs&logoColor=white)

![](https://badgen.net/badge/mkdocs/material/red?icon=libraries)

</div>

`mkdocs` is used to generate a static site for documentation of the project from the `docs` folder. This is hosted on GitHub Pages through a GitHub Action in `.github`. The site is automatically built and deployed on every push to the `main` branch. [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/) is used as the theme for the documentation site.

<div align="center">

![](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white)

</div>

This project is primarily built for `.vscode` but can be used with other editors as well. The `.vscode` folder contains a number of settings and extensions that are recommended for the project. These are automatically installed when the project is opened in VS Code.

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<img src="https://raw.githubusercontent.com/pycqa/isort/main/art/logo_large.png" height="20" width="60"></img>
![](https://badgen.net/badge/linter/ruff/blue)
![](https://badgen.net/badge/linter/flake8/green)

![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)

</div>
</div>

This project uses Pytest as a testing framework with code coverage. A number of python linters are configured to run through [`pyproject.toml`](https://peps.python.org/pep-0518/).

---

* ⁉️ [Helper Resources](help.md) for more information on choice of tools and how to use them.
* 🎋 [Project structure](structure.md) for more information on the project structure.

---

## 🍪 Setup

* Clone the repository

  ```bash
  git clone https://github.com/dotlas/cookiecutter-pypackage
  cd cookiecutter-template
  ```

* Initialize `base` conda environment for cookiecutter dependencies and install requirements

  > Developers @Dotlas can directly use the `dotlas` environment instead of `base`

  ```bash
  conda activate base
  python -m pip install -r requirements.txt
  ```

## 🧰 Usage

Run the following command to create a new project:

```bash
cookiecutter .
```

Or use directly from source:

```bash
cookiecutter gh:dotlas/cookiecutter-pypackage
```
