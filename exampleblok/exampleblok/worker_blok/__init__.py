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
        workers = [dict(name=worker, room=room)
                   for worker in ('Georges Racinet', 'Christophe Combelles',
                                  'Sandrine Chaufournais', 'Pierre Verkest',
                                  u"Simon André", 'Florent Jouatte',
                                  'Clovis Nzouendjou',
                                  u"Jean-Sébastien Suzanne")]
        self.registry.Worker.multi_insert(*workers)
