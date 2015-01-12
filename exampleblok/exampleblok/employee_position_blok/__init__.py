# -*- coding: utf-8 -*-
from anyblok.blok import Blok


class EmployeePositionBlok(Blok):

    version = '1.0.0'

    priority = 200

    conditional = [
        'employee',
        'position',
    ]

    def install(self):
        Employee = self.registry.Employee

        position_by_employee = {
            'Georges Racinet': 'DG',
            'Christophe Combelles': 'Comercial',
            'Sandrine Chaufournais': u"Secrétaire",
            'Pierre Verkest': 'Chef de projet',
            'Franck Bret': 'Chef de projet',
            u"Simon André": 'Developper',
            'Florent Jouatte': 'Developper',
            'Clovis Nzouendjou': 'Developper',
            u"Jean-Sébastien Suzanne": 'Developper',
        }

        for employee, position in position_by_employee.items():
            Employee.query().filter(Employee.name == employee).update({
                'position_name': position})

    def update(self, latest_version):
        if latest_version is None:
            self.install()
