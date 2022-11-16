<h1 align="center" style="border-bottom: none">
{{cookiecutter.name}} {{cookiecutter.emoji}}
</h1>
<p align="center">{{cookiecutter.description}}</p>

- [📓 Prerequisites](#-prerequisites)
- [📦 Setup](#-setup)

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
