[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SHervoe-Hansen/Caffeine_solubility/Japan?filepath=Caffeine_solubility.ipynb)
# Supporting information

### Caffeine Solvation in Electrolyte Solutions
This is supporting information for an unpublished scientific manuscript by _Hervø-Hansen et al._ on the solvation free energy of caffeine in various electrolyte solutions using the energy-representation theory of solvation in combination with all-atom simulations. All figures within the analysis are publication ready and can be reproduced by running the provided Jupyter notebook (`.ipynb`). For running the simulation we recommend you clone the repository, else the original dataset can be analyzed through the use of [Binder](https://mybinder.org), which will open the notebook in an executable environment and can be accessed [here](https://mybinder.org/v2/gh/SHervoe-Hansen/Caffeine_solubility/Japan?filepath=Caffeine_solubility.ipynb).

### Layout
- `PDB_files` PDB files for various chemical species utilized.
- `Simulations` Directory containing raw ermod results and processed results. The directory is also used for location of trajectories and corresponding analysis upon reproduction.
- `force_fields` Directory containing force parameters files (in gromacs format) for the various chemical species utilized.
- `images` Directory containing publication ready figures and images imported in the Juypter notebooks.
- `Simulations.ipynb` Jupyter notebook for running molecular dynamics simulations using OpenMM.
- `Analysis.ipynb` Jupyter notebook for analysis of simulations and production of publication ready figures.
- `Auxiliary.py` Python file containing assisting functions to conduct non-parametric bootstrapping and calculate mean volumes over multiple trajectories.
- `environment.yml` Conda environment file to recreate the simulation environment. Predominantly contains Numpy, Scipy, OpenMM, OpenMMTools, parmed, and Packmol.

### Usage
To open the notebook, install Python via [Miniconda](https://conda.io/miniconda.html) and make sure all required packages are loaded by issuing the following terminal commands
```bash
   conda env create -f environment.yml
   conda activate openMM
   jupyter-notebook
```
