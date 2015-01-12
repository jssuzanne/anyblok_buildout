from setuptools import setup, find_packages
version = '0.0.1'


requires = [
    'anyblok',
]

WorkBlok = [
    'office=exampleblok.office_blok:OfficeBlok',
    'employee=exampleblok.employee_blok:EmployeeBlok',
    'position=exampleblok.position_blok:PositionBlok',
    'employee-position=exampleblok.employee_position_blok:EmployeePositionBlok',
],

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
            'exampleblok_interpretor=exampleblok.scripts:interpreter',
            'exampleblok_sqlschema=exampleblok.scripts:sqlschema',
            'exampleblok_modelschema=exampleblok.scripts:modelschema',
        ],
        'WorkBlok': WorkBlok,
    },
    extras_require={},
)
