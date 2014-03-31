from setuptools import setup, find_packages
version = '0.0.1'


requires = [
    'anyblok',
]

setup(
    name="ExampleBlok",
    version=version,
    author="Anybox",
    author_email="jssuzanne@anybox.fr",
    description="Anyblok is a dynamic injection blok framework",
    license="GPL",
    long_description="",
    url="",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    tests_require=requires + ['nose'],
    classifiers=[
    ],
    entry_points={
        'console_scripts': [
            'exampleblok=exampleblok.scripts:exampleblok',
        ],
        'ExampleBlok': [
            'exampleblok=exampleblok.bloks.example_blok:ExampleBlok',
        ],
    },
    extras_require={},
)
