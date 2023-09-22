from setuptools import setup, find_packages

with open("app/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='natlanutils',
    version='0.1',
    description='Essential tools for text preprocessing and text distribution analysis.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/liminalfever/NatLanUtils',
    author='Francesco Ortame',
    author_email='francesco.ortame@gmail.com',
    packages=find_packages(),
    # add requirements
    install_requires=[
        'tqdm',
        'collections',
        'pandas',
        're']
)
