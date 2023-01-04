<h1 align="center" style="border-bottom: none">
    <b>
        <a href="https://github.com/cookiecutter/cookiecutter/">🥠 Cookiecutter</a> Template for Modern Python Package Projects 🐍<br>
    </b>
</h1>

<div align="center">

![](https://img.shields.io/badge/Cookiecutter-D4AA00.svg?style=for-the-badge&logo=Cookiecutter&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)

![](https://img.shields.io/badge/pnpm-F69220.svg?style=for-the-badge&logo=pnpm&logoColor=white)
![](https://img.shields.io/badge/commitlint-000000.svg?style=for-the-badge&logo=commitlint&logoColor=white)
![](https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black)
![](https://img.shields.io/badge/Conventional%20Commits-FE5196.svg?style=for-the-badge&logo=Conventional-Commits&logoColor=white)

![](https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white)

![](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white)

</div>

## About

Cookiecutter templates enables developers to create projects from a predefined template. This template is a modern Python package project structure that utilizes a number of tools to automate and enforce best practices.

* [Faq](faq.md) for more information on choice of tools and how to use them.
* [Project structure](structure.md) for more information on the project structure.

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
