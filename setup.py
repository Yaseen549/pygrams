# from distutils.core import setup
import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent

readme = (here / "README.md").read_text()

setup(
  name = 'pygrams',
  packages = ['pygrams'],
  version = '0.0.4',
  license='MIT',
  description = 'Get python programs handy as a function',
  long_description=readme,
  long_description_content_type="text/markdown",
  author = 'Yaseen',
  author_email = 'fantasticyaseenshariff@gmail.com',
  url = 'https://syberstar.com',
  download_url = 'https://github.com/Yaseen549/pygrams/archive/refs/tags/v0.0.4.tar.gz',
  keywords = ['PYTHONPROGRAMS', 'PROGRAMS', 'FUNCTIONS', 'PYGRAMS'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)