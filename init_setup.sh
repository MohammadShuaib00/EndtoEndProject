echo [$(date)]: "START"

echo [$(date)]: "Creating env with Python 3.11"
conda create --prefix ./env python=3.11 -y

echo [$(date)]: "Activating the environment"
conda activate ./env

echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt

echo [$(date)]: "End"


