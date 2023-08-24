[![Build Status](https://github.com/ConorSheehan1/cookiecutter-fire-cli/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/cookiecutter-fire-cli/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tested python versions](https://img.shields.io/badge/dynamic/yaml?url=https://raw.githubusercontent.com/ConorSheehan1/cookiecutter-fire-cli/main/.github/workflows/ci.yml&label=Tested%20python%20versions&query=$.jobs.build.strategy.matrix.python)](https://github.com/ConorSheehan1/cookiecutter-fire-cli/blob/main/.github/workflows/ci.yml#L25)

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating a new python package with a [fire](https://github.com/google/python-fire) command line interface.

# Usage
To create a new project using this cookiecutter template:

```bash
pip install cookiecutter poetry
cookiecutter gh:ConorSheehan1/cookiecutter-fire-cli

# cd your_new_package
poetry install
poetry run task install_hooks
```

For full cookiecutter instructions see https://github.com/audreyr/cookiecutter#features

## Configuration provided
1. testing
    1. [pytest](https://github.com/pytest-dev/pytest)
    1. [github actions](https://github.com/features/actions)
        1. ci
        1. release (github release, optional)
        1. deploy (to pypi, requires additional steps, optional)
1. linting
    1. [black](https://github.com/psf/black) autoformatter
    1. [isort](https://github.com/PyCQA/isort) import sorter
    1. [mypy](https://github.com/python/mypy) type checker
1. dependency management / packaging
    1. [poetry](https://github.com/python-poetry/poetry)
1. version management
    1. [bump2version](https://github.com/c4urself/bump2version)
1. license
    1. MIT
1. githooks
    1. pre-commit (requires additional steps)

## Local/Dev install
```bash
poetry install
poetry run cookiecutter .
# poetry run cookiecutter . --overwrite-if-exists --no-input
```
