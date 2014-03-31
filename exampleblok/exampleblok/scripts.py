import anyblok


def exampleblok():
    registry = anyblok.start(
        'Example Blok', '1.0',
        argsparse_groups=['config', 'database'],
        parts_to_load=['AnyBlok', 'ExampleBlok'])
    #TODO check if blok is installed to installed it
    print(registry)
