from AnyBlok import target_registry, Model
from AnyBlok.Column import String
from AnyBlok.RelationShip import Many2One


@target_registry(Model)
class Worker:

    position_name = String(label="Position name",
                           foreign_key=(Model.Position, 'name'))
    position = Many2One(label="Position", model=Model.Position,
                        foreign_keys="position_name")

    def __str__(self):
        res = super(Worker, self).__str__()
        return "%s (%s)" % (res, self.position)
