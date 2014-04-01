from AnyBlok import target_registry, Model
from AnyBlok.Column import String


@target_registry(Model)
class Position:

    name = String(label="Position", primary_key=True)

    def __str__(self):
        return self.name
