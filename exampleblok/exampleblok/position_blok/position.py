from anyblok import Declarations
target_registry = Declarations.target_registry
Model = Declarations.Model
String = Declarations.Column.String


@target_registry(Model)
class Position:

    name = String(label="Position", primary_key=True)

    def __str__(self):
        return self.name
