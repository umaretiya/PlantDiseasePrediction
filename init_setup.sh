echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.9 version"
conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating a env"
source activate ./env 

echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"
