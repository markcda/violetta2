import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vio2",
    version="0.1.4",
    author="titoffklim",
    author_email="titoffklim@cclc.tech",
    description="Translator from Python to Russian pseudo-language and vice versa. Makes programming more accessible.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kollieartwolf/violetta2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
