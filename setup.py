import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="buffy",
    version="0.0.1",
    author="Bram Wiggers, Owen Terpstra, Matthijs Tadema, Noa Leijdesdorff",
    author_email="M.J.Tadema@gmail.com",
    description="An automated buffer adjusting system for IGEM teams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ezmagon/buffy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires =['numpy', 'tk-tools', 'imutils', 'matplotlib', 'opencv-python', 'IPython'],
    scripts = [
        "bin/buffy_run.py"
    ],
    package_data = {
        "buffy":["data/pic7.jpeg"]
    },
    #python_requires = '~=3.5'

)
print("run using \"buffy_run.py\"")