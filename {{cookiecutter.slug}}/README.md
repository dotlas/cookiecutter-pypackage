<h1 align="center" style="border-bottom: none">
{{cookiecutter.name}} {{cookiecutter.emoji}}
</h1>
<p align="center">{{cookiecutter.description}}</p>

- [📓 Prerequisites](#-prerequisites)
- [📦 Setup](#-setup)

## 📓 Prerequisites

Go through the [onboarding guide](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/22085636/Onboarding) to setup the following tools:

- A [`conda`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/75628545/anaconda) environment, `dotlas`, equipped with [`python==3.10`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/21528577/python)
- A [`node`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/18317411/node) environment with the latest LTS version
- [`pnpm`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/75595793/pnpm), the node package manager

## 📦 Setup

- Clone the repository

  ```bash
  git clone {{cookiecutter.github_repo}}
  cd {{cookiecutter.slug}}
  ```

- Activate the `dotlas` `conda` environment

  ```bash
  conda activate dotlas
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
