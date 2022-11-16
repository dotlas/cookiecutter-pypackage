# `cookiecutter-template`

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for Python projects.

- [`cookiecutter-template`](#cookiecutter-template)
  - [🍪 Setup](#-setup)
  - [🧰 Usage](#-usage)

## 🍪 Setup

- Clone the repository

  ```bash
  git clone https://github.com/dotlas/cookiecutter-template
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
