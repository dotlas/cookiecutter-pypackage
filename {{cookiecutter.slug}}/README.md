<h1 align="center" style="border-bottom: none">
{{cookiecutter.name}} {{cookiecutter.emoji}}
</h1>
<p align="center">{{cookiecutter.description}}</p>

- [📓 Prerequisites](#-prerequisites)
- [📦 Setup](#-setup)
- [🏞 Workflow](#-workflow)
- [🧪 Tests](#-tests)

## 📓 Prerequisites

- A [`conda`](https://continuum.io/) environment, equipped with [`python==3.10`](https://www.python.org/downloads/release/python-3100/)
- A [`node`](https://github.com/nvm-sh/nvm) environment with the latest LTS version
- [`pnpm`](https://pnpm.io/), the node package manager

## 📦 Setup

- Clone the repository

  ```bash
  git clone {{cookiecutter.github_repo}}
  cd {{cookiecutter.slug}}
  ```

- Create a `conda` environment for the project

  ```bash
  conda create --name {{cookiecutter.package_name}} python=3.10 -y
  conda activate {{cookiecutter.package_name}}
  ```

- Install `node` dependencies

  ```bash
  pnpm i
  ```

- Install `{{cookiecutter.package_name}}` and all dependencies

  ```bash
  pip install -e ".[dev,doc,test]"
  ```

  > Alternatively,
  >
  > ```bash
  > flit install --deps develop --symlink
  > ```

  > **Warning**
  >
  > It is crucial to include the `-e` flag when installing with `pip` (or `--symlink` with `flit`).
  > This makes the installed package `editable`, meaning changes to the codebase are reflected in the installation.

- Verify installation

  ```python
  import {{cookiecutter.package_name}}
  ```

## 🏞 Workflow

- Format code (runs `black` and `isort` on `.py` and `.ipynb` files)

    ```bash
    pnpm format
    ```

- Commits use `conventional commits` and `pre-commit` hooks configured with `husky`

    ```bash
    git add <files>
    pnpm commit
    ```

- If a commit fails for some reason (`pre-commit` hooks, etc.), you don't need to retype the commit details. Just run the following command to use the previous commit message and re-run the hooks.

    ```bash
    pnpm commit --retry
    ```

- **Not recommended:** If a commit does not go through the `pre-commit` hooks, you can bypass them by using the `--no-verify` flag

    ```bash
    git commit -m "<message>" --no-verify
    ```

- Docs generated automatically based on function docstrings. Uses `mkdocs material` theme. View docs locally with the following command

    ```bash
    pnpm docs
    ```

## 🧪 Tests

- Run all tests with a coverage report

    ```bash
    pnpm test
    ```

- Speedtest (runs in parallel) without coverage report

    ```bash
    pytest -n auto
    ```

- Run a specific test file. Ex: `test_dataframe.py`

    ```bash
    pytest tests/functions/test_dataframe.py   # pytest -v for verbose
    ```

> Built with [Dotlas PyPackage Cookiecutter](https://github.com/dotlas/cookiecutter-pypackage): a template to create modern python packages.
