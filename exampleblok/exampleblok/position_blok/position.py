from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
String = Declarations.Column.String


@register(Model)
class Position:

    name = String(label="Position", primary_key=True)

    def __str__(self):
        return self.name

    @classmethod
    def import_declaration_module(cls):
        from . import position  # noqa
