from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
Integer = Declarations.Column.Integer
String = Declarations.Column.String
Many2One = Declarations.RelationShip.Many2One


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
