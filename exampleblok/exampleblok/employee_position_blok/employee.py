from anyblok import Declarations
from anyblok.relationship import Many2One

register = Declarations.register
Model = Declarations.Model


@register(Model)
class Employee:

    position = Many2One(label="Position", model=Model.Position, nullable=False)

    def __str__(self):
        res = super(Employee, self).__str__()
        return "%s (%s)" % (res, self.position)
