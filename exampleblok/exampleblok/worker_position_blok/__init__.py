# -*- coding: utf-8 -*-
from anyblok.blok import Blok


class WorkerPositionBlok(Blok):

    priority = 200

    conditional = [
        'worker',
        'position',
    ]

    def install(self):
        Worker = self.registry.Worker

        position_by_worker = {
            'Georges Racinet': 'DG',
            'Christophe Combelles': 'Comercial',
            'Sandrine Chaufournais': u"Secrétaire",
            'Pierre Verkest': 'Chef de projet',
            u"Simon André": 'Developper',
            'Florent Jouatte': 'Developper',
            'Clovis Nzouendjou': 'Developper',
            u"Jean-Sébastien Suzanne": 'Developper',
        }

        for worker, position in position_by_worker.items():
            Worker.query().filter(Worker.name == worker).update({
                'position_name': position})
