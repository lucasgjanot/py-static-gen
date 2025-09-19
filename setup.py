from setuptools import setup, find_packages

setup(
    name="py_static_gen",
    version="0.1.0",
    description="Static site generator in Python",
    author="Lucas G. Janot",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        # coloque aqui suas dependências, ex:
        # "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'py_static_gen=main:main',  # Exemplo se quiser criar comando shell
        ],
    },
)
