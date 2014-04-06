from AnyBlok import target_registry, Model
from AnyBlok.RelationShip import Many2One


@target_registry(Model)
class Worker:

    position = Many2One(label="Position", model=Model.Position)

    def __str__(self):
        res = super(Worker, self).__str__()
        return "%s (%s)" % (res, self.position)
