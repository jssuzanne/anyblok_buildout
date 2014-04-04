from AnyBlok import target_registry, Model
from AnyBlok.Column import String, Integer
from AnyBlok.RelationShip import Many2One


@target_registry(Model)
class Address:

    id = Integer(label="Identifying", primary_key=True)
    street = String(label="Street", nullable=False)
    zip = String(label="Zip", nullable=False)
    city = String(label="City", nullable=False)

    def __str__(self):
        return "%s %s %s" % (self.street, self.zip, self.city)


@target_registry(Model)
class Room:

    id = Integer(label="Identifying", primary_key=True)
    number = Integer(label="Number of the room", nullable=False)
    address = Many2One(label="Address", model=Model.Address, nullable=False,
                       remote_column="id", one2many="rooms")

    def __str__(self):
        return "Room %d at %s" % (self.number, self.address)
