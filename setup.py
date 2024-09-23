import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "2.2.2"

REPO_NAME = "MLFlow"
AUTHOR_USER_NAME = "PRANAVV1107"
SRC_REPO = "MLFlow"
AUTHOR_EMAIL = "pranav.vishwanath99@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A Small Python Package For ML",
    long_description=long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src")
)