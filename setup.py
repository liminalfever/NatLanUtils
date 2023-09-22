from setuptools import setup, find_packages

setup(
    name='natlanutils',
    version='0.1',
    description='Essential tools for text preprocessing and text distribution analysis.',
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