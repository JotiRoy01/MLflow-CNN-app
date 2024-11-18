# MLflow-project-template
MLflow project template

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.10 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05 - Create conda.yaml file -
```bash
conda env export > conda.yaml
```
### Remember
 ```bash
 name: MLProject
conda_env: conda.yaml

entry_points:
  main:
    command: "python src/main.py"

  get_data:
    parameters:
      config: {type: str , default: "configs/config.yaml"}
    command: "python src/stage__01__template.py --config={config}"

  base_model_creation:
    parameters:
      config: {type: str , default: "configs/config.yaml"}
    command: "python src/stage_02_base_model_creation.py --config={config}"
    ```
### Example
```bash
conda MLprojects
if you try to execute mlflow project without conda environment ->>>
first try to : 
def main():
    with mlflow.start_run() as run :
        mlflow.run(".","get_data",env_manager="local")
        mlflow.run(".","base_model_creation",env_manager="local")

and comman line type:
mlflow run . --env-manager="local"
```
### Command
```bash
conda single command execution:
mlflow run . -e get_data -P config=configs/config.yaml --no-conda/--env-manager="local"
```
### STEP 06- commit and push the changes to the remote repository