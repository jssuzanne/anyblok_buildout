from anyblok.blok import Blok


class PositionBlok(Blok):

    version = '1.0.0'

    def install(self):
        self.registry.Position.multi_insert({'name': 'DG'},
                                            {'name': 'Comercial'},
                                            {'name': 'Secrétaire'},
                                            {'name': 'Chef de projet'},
                                            {'name': 'Developper'})

    def update(self, latest_version):
        if latest_version is None:
            self.install()
