from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One

register = Declarations.register
Model = Declarations.Model


@register(Model)
class Address:

    id = Integer(label="Identifying", primary_key=True)
    street = String(label="Street", nullable=False)
    zip = String(label="Zip", nullable=False)
    city = String(label="City", nullable=False)

    def __str__(self):
        return "%s %s %s" % (self.street, self.zip, self.city)


@register(Model)
class Room:

    id = Integer(label="Identifying", primary_key=True)
    number = Integer(label="Number of the room", nullable=False)
    address = Many2One(label="Address", model=Model.Address, nullable=False,
                       one2many="rooms")

    def __str__(self):
        return "Room %d at %s" % (self.number, self.address)
