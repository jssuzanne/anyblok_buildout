from anyblok.blok import Blok


class WorkerBlok(Blok):

    version = '1.0.0'

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
                                  'Franck Bret', u"Simon André",
                                  'Florent Jouatte', 'Clovis Nzouendjou',
                                  u"Jean-Sébastien Suzanne")]
        self.registry.Worker.multi_insert(*workers)

    def update(self, latest_version):
        if latest_version is None:
            self.install()
