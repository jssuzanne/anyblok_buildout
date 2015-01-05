from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
Many2One = Declarations.RelationShip.Many2One


@register(Model)
class Worker:

    position = Many2One(label="Position", model=Model.Position, nullable=False)

    def __str__(self):
        res = super(Worker, self).__str__()
        return "%s (%s)" % (res, self.position)
