from setuptools import setup, find_packages

setup(
    name="pilkommedia",
    version="0.1.0",
    description="Modul untuk keperluan perkuliahan Program Studi Pendidikan Komputer Universitas Lambung Mangkurat",
    packages=find_packages(include=['statistika']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    url="https://github.com/ahmadyogi543/pypi_pilkommedia",
    author="Ahmad Yogi",
    author_email="ahmadyogi543@gmail.com",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    data_files=['data/statistik_iwak_papuyu.csv'],
)
