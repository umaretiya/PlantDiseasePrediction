from cmath import log
from pathlib import Path
import logging, os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s :')

package_name = "PlantDisease"

list_of_files = [
    ".github/workflows/.geetkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constant/__init__.py",
    ".gitignore",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/initegration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini",
    # "init_setup.sh",
    "setup.py",
    "README.md",
    "setup.cfg",
    "LICENSE",
    "Dockerfile",
    ".dockerignore",
    ".dvcignore",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a dir {filedir} & file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file {filename}")
            
    else:
        logging.info(f"file already exist {filename}")
        