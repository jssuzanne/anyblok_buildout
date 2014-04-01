from AnyBlok import target_registry, Model
from AnyBlok.Column import String, Integer
from AnyBlok.RelationShip import Many2One


@target_registry(Model)
class Worker:

    name = String(label="Number of the room", primary_key=True)
    room_id = Integer(label="Desk", nullable=False,
                      foreign_key=(Model.Room, 'id'))
    room = Many2One(label="Desk", model=Model.Room,
                    foreign_keys="room_id")

    def __str__(self):
        return "%s in %s" % (self.name, self.room)
