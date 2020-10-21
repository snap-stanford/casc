import setuptools

INSTALL_REQUIRES = ['sklearn',
                    'bitarray',
                    'sortedcontainers'
                    ]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="masa", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    #author_email="author@example.com",
    description="A minimal installable package for masa clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RWTH-EBC/masa",
    packages=setuptools.find_packages(),
    #packages="CASC_solver",
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=INSTALL_REQUIRES,
)