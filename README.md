[![CC BY 4.0][cc-by-shield]][cc-by]

# ACTRIS-CCRES documentation

Source for the documentation https://ccres.ipsl.fr/docs/

The documentation is build using [sphinx](https://www.sphinx-doc.org), [Myst-Parser](https://github.com/executablebooks/MyST-Parser) and [sphinx book theme](https://github.com/executablebooks/sphinx-book-theme)

## Install

### Clone the repository

```bash
git clone https://github.com/ACTRIS-CCRES/docs ccres-docs
```

### Create python environment

#### With conda

```bash
conda create -n ccres-docs python=3.12
conda activate ccres-docs
```

#### With venv

```bash
python -m venv ccres-docs
source ccres-docs/bin/activate
```

### Install dependencies

```bash
cd ccres-docs
pip install -r requirements.txt
```

### Build documentation

```bash
make html
```

### Serve locally

```bash
sphinx-autobuild source build/html
```

then go to http://127.0.0.1:8000


## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
