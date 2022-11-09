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
  flit install --deps develop --symlink
  ```

- Verify installation

  ```python
  import {{cookiecutter.package_name}}
  ```
