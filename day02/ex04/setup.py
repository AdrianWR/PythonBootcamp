import setuptools

setuptools.setup(
    name="ai42",
    version="1.0.0",
    author="Adrian Roque",
    author_email="aroque@student.42sp.org.br",
    description="A small example package for Python Bootcamp",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
