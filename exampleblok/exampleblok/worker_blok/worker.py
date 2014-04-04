from AnyBlok import target_registry, Model
from AnyBlok.Column import String
from AnyBlok.RelationShip import Many2One


@target_registry(Model)
class Worker:

    name = String(label="Number of the room", primary_key=True)
    room = Many2One(label="Desk", model=Model.Room, remote_column="id",
                    one2many="workers")

    def __str__(self):
        return "%s in %s" % (self.name, self.room)
