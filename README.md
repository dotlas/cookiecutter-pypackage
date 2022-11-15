# `cookiecutter-template`

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for Python projects.

- [`cookiecutter-template`](#cookiecutter-template)
  - [📓 Prerequisites](#-prerequisites)
  - [📦 Setup](#-setup)
  - [🧰 Usage](#-usage)

## 📓 Prerequisites

Go through the [onboarding guide](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/22085636/Onboarding) to setup the following tools:

- A [`conda`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/75628545/anaconda) environment, `dotlas`, equipped with [`python==3.10`](https://dotlas.atlassian.net/wiki/spaces/TECHDOTLAS/pages/21528577/python)

## 📦 Setup

- Clone the repository

  ```bash
  git clone https://github.com/dotlas/cookiecutter-template
  cd swarm
  ```

- Activate the `dotlas` `conda` environment

  ```bash
  conda activate dotlas
  ```

- Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

## 🧰 Usage

Run the following command to create a new project:

```bash
cookiecutter .
```
