import anyblok
from logging import getLogger
from anyblok.config import Configuration

logger = getLogger()


def exampleblok():
    # Initialise the application, with a name and a version number
    # select the groupe of options to display
    # return a registry if the database are selected
    registry = anyblok.start(
        'Example Blok', configuration_groups=['message', 'logging'])
    message_before = Configuration.get('message_before')
    message_after = Configuration.get('message_after')

    if not registry:
        logger.warning("No database database selected")
        exit(0)

    if message_before:
        logger.info(message_before)

    for address in registry.Address.query().all():
        for room in address.rooms:
            for worker in room.workers:
                logger.info(worker)

    if message_after:
        logger.info(message_after)
