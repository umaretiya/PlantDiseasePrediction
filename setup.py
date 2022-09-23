import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "PlantDiseasePredict"
AUTHOR_USER_NAME = "umaretiya"
SRC_REPO = "PlantDisease"
AUTHOR_EMAIL = "umaretiya@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A Deep Learning CNN Model with computer vision and tensorflow-keras",
    long_description=long_description,

    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)