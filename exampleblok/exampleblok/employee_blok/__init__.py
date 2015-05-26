from anyblok.blok import Blok
from . import config  # noqa


class EmployeeBlok(Blok):

    version = '1.0.0'

    autoinstall = True

    required = [
        'office',
    ]

    optional = [
        'position',
    ]

    def install(self):
        room = self.registry.Room.query().filter(
            self.registry.Room.number == 308).first()
        employees = [dict(name=employee, room=room)
                     for employee in ('Georges Racinet',
                                      'Christophe Combelles',
                                      'Sandrine Chaufournais',
                                      'Pierre Verkest',
                                      'Franck Bret',
                                      "Simon André",
                                      'Florent Jouatte',
                                      'Clovis Nzouendjou',
                                      "Jean-Sébastien Suzanne")]
        self.registry.Employee.multi_insert(*employees)

    def update(self, latest_version):
        if latest_version is None:
            self.install()

    @classmethod
    def import_declaration_module(cls):
        from . import employee  # noqa
