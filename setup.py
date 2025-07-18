from setuptools import find_packages, setup

from lakshmi.constants import NAME, VERSION

with open('README.md', 'r', encoding='utf-8') as fh:
    # Replace relative links to absolute links.
    long_description = (
        fh.read()
        .replace('](./', '](https://sarvjeets.github.io/lakshmi/')
        .replace('lak.md', 'lak.html'))

setup(
    name=NAME,
    version=VERSION,
    author='Sarvjeet Singh',
    author_email='sarvjeet@gmail.com',
    description=('Investing library and command-line interface '
                 'inspired by the Bogleheads philosophy'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sarvjeets/lakshmi',
    license="MIT",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['lakshmi'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'click~=8.0',
        'curl_cffi~=0.10',
        'ibonds>=1.0.2,<2.0',
        'numpy>=1.22,<3.0',
        'pyxirr~=0.6',
        'PyYAML>=5.4,<7.0',
        'requests~=2.25',
        'tabulate~=0.8',
        'yfinance>=0.2.38,<0.3',
    ],
    entry_points={
        'console_scripts': [
            'lak = lakshmi.lak:lak',
        ],
    },
    test_suite='tests',
    python_requires='>=3.7',
)
