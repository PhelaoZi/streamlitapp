from setuptools import setup, find_packages

setup(
    name="your-project-name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "chromadb",
        "chroma-hnswlib",
    ],
)