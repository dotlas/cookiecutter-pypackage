<h1 align="center" style="border-bottom: none">
{{cookiecutter.name}} {{cookiecutter.emoji}}
</h1>
<p align="center">{{cookiecutter.description}}</p>

## 📦 Setup

- Clone the repository

  ```bash
  git clone {{cookiecutter.github_repo}}
  cd {{cookiecutter.slug}}
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
