import anyblok
from logging import getLogger
from anyblok._argsparse import ArgsParseManager
from anyblok.scripts import interpreter as anyblok_interpreter
from anyblok.scripts import sqlschema as anyblok_sqlschema
from anyblok.scripts import modelschema as anyblok_modelschema

logger = getLogger(__name__)


def exampleblok():
    # Initialise the application, with a name and a version number
    # select the groupe of options to display
    # select the groups of bloks availlable
    # return a registry if the database are selected
    registry = anyblok.start(
        'Example Blok', '1.0',
        argsparse_groups=['config', 'database', 'message'],
        parts_to_load=['AnyBlok', 'WorkBlok'])
    message_before = ArgsParseManager.get('message_before')
    message_after = ArgsParseManager.get('message_after')

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


def interpreter():
    anyblok_interpreter(
        'Interpreter', '1.0',
        argsparse_groups=['config', 'database', 'interpreter'],
        parts_to_load=['AnyBlok', 'WorkBlok'])


def sqlschema():
    anyblok_sqlschema(
        'SQL Schema', '1.0',
        argsparse_groups=['config', 'database', 'schema'],
        parts_to_load=['AnyBlok', 'WorkBlok'])


def modelschema():
    anyblok_modelschema(
        'UML Schema', '1.0',
        argsparse_groups=['config', 'database', 'schema'],
        parts_to_load=['AnyBlok', 'WorkBlok'])
