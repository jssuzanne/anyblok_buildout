import anyblok
from logging import getLogger

logger = getLogger(__name__)


def exampleblok():
    registry = anyblok.start(
        'Example Blok', '1.0',
        argsparse_groups=['config', 'database'],
        parts_to_load=['AnyBlok', 'WorkBlok'])
    for address in registry.Address.query().all():
        for room in address.rooms:
            for worker in room.workers:
                logger.info(worker)
