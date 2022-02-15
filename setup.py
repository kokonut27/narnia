from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "narnia",
  version = "0.0.4",
  description = "Journey across a vast expanse of experimental designs and data.",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/kokonut27/narnia",
  author = "kokonut27",
  author_email = "beol0127@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT License",
  packages=['narnia'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)