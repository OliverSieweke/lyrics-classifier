<!--suppress HtmlDeprecatedAttribute | JetBrains Inspection -->

<p align="center">
    <a title="Documentation" href="https://lyrics-classifier.readthedocs.io/">
        <img alt="Lyrics Logo" src="lyrics.svg"/>
    </a>
</p>

<h1 align="center">Lyrics Classifier</h1> 

<p align="center">
    <a title="MIT License" href="https://choosealicense.com/licenses/mit">
      <img alt="License: MIT" src="https://img.shields.io/github/license/OliverSieweke/lyrics-classifier" />
    </a>
    <a title="Documentation Status" href="https://lyrics-classifier.readthedocs.io/en/latest/?badge=latest">
        <img alt="Documentation Status" src="https://readthedocs.org/projects/lyrics-classifier/badge/?version=latest" />
    </a>
    <a title="MyBinder" href="https://mybinder.org/v2/gh/OliverSieweke/lyrics-classifier/master?filepath=notebooks">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg" />
    </a>
</p>

Welcome to *Lyrics Classifier*! This project explores machine learning models to predict an artist from song lyrics.

## User Guide

### Viewing the Project

The various notebooks in this project used for exploratory data analysis, visualizations and predictive modeling can be viewed online with [MyBinder](https://mybinder.org/v2/gh/OliverSieweke/lyrics-classifier/master?filepath=notebooks) (this may take some time to launch in case no container is currently deployed).

### Running the Project

If you have [Python 3](https://www.python.org/downloads/) installed, you may also run the notebooks on your local machine by executing the following commands from the terminal:

```bash
$ git clone https://github.com/OliverSieweke/lyrics-classifier.git
$ cd lyrics-classifier
$ pip install -r requirements.txt
$ jupyter notebook notebooks
```

## Developer Guide

<a title="Python 3.7" href="https://docs.python.org/3.7/">
  <img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-blue.svg" />
</a>
<a title="Black" href="https://github.com/psf/black">
  <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
</a>
<a title="Dependabot" href="https://dependabot.com/">
    <img alt="Dependabot" src="https://badgen.net/dependabot/OliverSieweke/lyrics-classifier/?icon=dependabot" />
</a>

To contribute or build on the project, please fork the repository, make sure you have [Python 3.8](https://www.python.org/downloads/) installed and set up your local copy as follows:

```bash
$ git clone https://github.com/<path_to_your_fork>
$ cd <your_local_repository>
$ python3.8 -m pip install -r requirements-dev.txt
$ pre-commit install
```

This will install required dependencies and set up git hooks to ensure that your commits conform to the project's standards and code style.

### Documentation


Documentation for the project is built with [Sphinx](https://www.sphinx-doc.org/en/master/#) and [Read the Docs](https://readthedocs.org/) and can be viewed [here](https://lyrics-classifier.readthedocs.io/en/latest/).
