import anyblok
from logging import getLogger
from anyblok._argsparse import ArgsParseManager

logger = getLogger(__name__)


def exampleblok():
    registry = anyblok.start(
        'Example Blok', '1.0',
        argsparse_groups=['config', 'database', 'message', 'logging'],
        parts_to_load=['AnyBlok', 'WorkBlok'])
    message_before = ArgsParseManager.get('message_before')
    message_after = ArgsParseManager.get('message_after')

    if message_before:
        logger.info(message_before)

    for address in registry.Address.query().all():
        for room in address.rooms:
            for worker in room.workers:
                logger.info(worker)

    if message_after:
        logger.info(message_after)
