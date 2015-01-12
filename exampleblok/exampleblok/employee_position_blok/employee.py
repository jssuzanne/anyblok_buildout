from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
Many2One = Declarations.RelationShip.Many2One


@register(Model)
class Employee:

    position = Many2One(label="Position", model=Model.Position, nullable=False)

    def __str__(self):
        res = super(Employee, self).__str__()
        return "%s (%s)" % (res, self.position)
