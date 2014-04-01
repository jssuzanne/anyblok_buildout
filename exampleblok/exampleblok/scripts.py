import anyblok


def exampleblok():
    registry = anyblok.start(
        'Example Blok', '1.0',
        argsparse_groups=['config', 'database'],
        parts_to_load=['AnyBlok', 'WorkBlok'])
    for worker in registry.Worker.query().all():
        print(worker)
