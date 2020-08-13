import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alveolus",
    version="0.0.2b1",
    author="Ioannis Kozaris",
    author_email="ioanniskozaris@gmail.com",
    description="Alveolus Docs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['alveolus', 'exhale'],
    package_dir={'alveolus': 'alveolus', 'exhale': 'exhale'},
    package_data={"alveolus": ["tools/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    keywords='documentation sphinx doxygen C++ docs',
    install_requires=['sphinx', 'breathe'],
    python_requires='~=3.3',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'alveolus-build=alveolus.main:build',
            'alveolus-create=alveolus.main:create',
            'alveolus-clean=alveolus.main:clean',
        ],
    },

)
