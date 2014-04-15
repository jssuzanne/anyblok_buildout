from anyblok import Declarations
target_registry = Declarations.target_registry
Model = Declarations.Model
String = Declarations.Column.String
Many2One = Declarations.RelationShip.Many2One


@target_registry(Model)
class Worker:

    name = String(label="Number of the room", primary_key=True)
    room = Many2One(label="Desk", model=Model.Room, one2many="workers")

    def __str__(self):
        return "%s in %s" % (self.name, self.room)
