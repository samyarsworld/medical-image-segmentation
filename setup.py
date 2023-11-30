import setuptools

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

__version__ = "0.0.0"

NAME = "image_segmentation"
REPO_NAME = "image-segmentation"

# Installs all directories with initializer (e.g., __init__.py)
setuptools.setup(
    name=NAME,
    version=__version__,
    author="samyarsworld",
    author_email="samyarfarjam@outlook.com",
    description="A image segmentation tool for computer vision applications",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/samyarsworld/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/samyarsworld/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)