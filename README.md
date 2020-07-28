[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SHervoe-Hansen/Caffeine_solubility/Japan?filepath=Caffeine_solubility.ipynb)
# Supporting information

### Caffeine Solvation in Electrolyte Solutions
This is supporting information for an unpublished scientific manuscript by _Hervø-Hansen et al._ on the solvation free energy of caffeine in various electrolyte solutions using the energy representation description in combination with all-atom simulations. All figures within the analysis are publication ready and can be reproduced by running the provided Jupyter notebook (`.ipynb`). For running the simulation we recommend you clone the repository, else the original dataset can be analyzed through the use of [Binder](https://mybinder.org), which will open the notebook in an executable environment and can be accessed [here](https://mybinder.org/v2/gh/SHervoe-Hansen/Caffeine_solubility/Japan?filepath=Caffeine_solubility.ipynb).

### Layout

- `PDB_files` PDB files for various varients studied.
- `Caffeine_solubility.ipynb` Jupyter notebook for submission and analysis of simulation and production of publication ready figures.

### Usage
To open the notebook, install Python via [Miniconda](https://conda.io/miniconda.html) and make sure all required packages are loaded by issuing the following terminal commands
```bash
   conda env create -f environment.yml
   conda activate openMM
   jupyter-notebook
```
