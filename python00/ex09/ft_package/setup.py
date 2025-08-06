from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='ssian',
    author_email='ssian@42mail.sutd.edu.sg',
    description='A simple package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ssian/ft_package',
    packages=find_packages(),
    python_requires='>=3.6',
    license='MIT',
)
