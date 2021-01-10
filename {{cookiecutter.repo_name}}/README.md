[![Build Status](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/workflows/ci/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# {{ cookiecutter.repo_name }}

# Testing
```bash
# unit tests
poetry run task tests

# linter
poetry run task lint

# Generate documentation
poetry run task docs
```