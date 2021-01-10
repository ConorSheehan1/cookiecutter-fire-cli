[![Build Status](https://github.com/ConorSheehan1/cookiecutter-fire-cli/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/cookiecutter-fire-cli/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repo contains a [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating a new python package with a  [fire](https://github.com/google/python-fire) command line interface.

# Usage
For full cookiecutter instructions see https://github.com/audreyr/cookiecutter#features

To create a new project using this cookiecutter template:

```bash
pip install cookiecutter
cookiecutter gh:ConorSheehan1/cookiecutter-fire-cli
```

### Local/Dev install
```
poetry install
poetry run cookiecutter .
# poetry run cookiecutter . --overwrite-if-exists --no-input
```

# Configuration provided
1. testing
    1. pytest
    1. github actions
1. linting
    1. black
    1. mypy
1. docs
    1. sphinx
1. license
    1. MIT