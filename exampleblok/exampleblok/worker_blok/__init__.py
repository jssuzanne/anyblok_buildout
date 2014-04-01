from anyblok.blok import Blok


class WorkerBlok(Blok):

    autoinstall = True

    required = [
        'desk',
    ]

    optional = [
        'position',
    ]

    def install(self):
        room = self.registry.Room.query().filter(
            self.registry.Room.number == 308).first()
        for worker in ('Georges Racinet', 'Christophe Combelles',
                       'Sandrine Chaufournais', 'Pierre Verkest',
                       u"Simon André", 'Florent Jouatte', 'Clovis Nzouendjou',
                       u"Jean-Sébastien Suzanne"):
            self.registry.Worker.insert(name=worker, room=room)
