from anyblok import Declarations
target_registry = Declarations.target_registry
Model = Declarations.Model
Many2One = Declarations.RelationShip.Many2One


@target_registry(Model)
class Worker:

    position = Many2One(label="Position", model=Model.Position, nullable=False)

    def __str__(self):
        res = super(Worker, self).__str__()
        return "%s (%s)" % (res, self.position)
