# weather_yz5410

[![CI](https://github.com/QMSS-G5072-2026/weather_zhu_yijin/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/QMSS-G5072-2026/weather_zhu_yijin/actions/workflows/ci.yml)

A Python package for converting temperatures, summarizing readings, and cleaning weather data.

## Installation

```bash
$ uv add weather_yz5410
```

or, without uv, `pip install weather_yz5410`.

## Development

```bash
$ uv sync                       # create .venv and install the package with its dev and docs groups
$ uv run pytest                 # run the tests
$ uv run make html -C docs      # build the documentation
$ uv build                      # build the sdist and wheel into dist/
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`weather_yz5410` was created by Yijin Zhu. It is licensed under the terms of the MIT license.

## Credits

`weather_yz5410` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `qmss-pkgs-cookiecutter` [template](https://github.com/QMSS-G5072-2026/qmss-pkgs-cookiecutter), a uv-based fork of [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter).
