from anyblok import Declarations
from anyblok.column import String
from anyblok.relationship import Many2One

register = Declarations.register
Model = Declarations.Model


@register(Model)
class Employee:

    name = String(label="Number of the room", primary_key=True)
    room = Many2One(label="Desk", model=Model.Room, one2many="workers")

    def __str__(self):
        return "%s in %s" % (self.name, self.room)
