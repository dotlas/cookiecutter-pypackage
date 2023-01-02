# [Cookiecutter](https://github.com/cookiecutter/cookiecutter/) template for Python Package Projects

* Includes `husky`, `node` and `pnpm`
* Uses `pyproject.toml` and `pre-commit` hooks

- [Cookiecutter template for Python Package Projects](#cookiecutter-template-for-python-package-projects)
  - [🍪 Setup](#-setup)
  - [🧰 Usage](#-usage)

## 🍪 Setup

- Clone the repository

  ```bash
  git clone https://github.com/dotlas/cookiecutter-pypackage
  cd cookiecutter-template
  ```

- Initialize `base` conda environment for cookiecutter dependencies and install requirements

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
