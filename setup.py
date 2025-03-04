from setuptools import setup, find_packages

setup(
    name="volumentations",
    version="0.1.8",
    author="kumuji",
    author_email="alexey@nekrasov.dev",
    description="Point augmentations library as hard-fork of albu-team/albumentations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kumuji/volumentations",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=["pyyaml", "numpy", "importlib-metadata"],
    python_requires=">=3.6.1",
    include_package_data=True,
    # Specify the source directory
    package_dir={"": "src"},
    # Automatically find all packages in the specified directory
    packages=find_packages(where="src"),
)
