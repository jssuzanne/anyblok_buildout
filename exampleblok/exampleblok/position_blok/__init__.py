from anyblok.blok import Blok


class PositionBlok(Blok):

    def install(self):
        self.registry.Position.multi_insert({'name': 'DG'},
                                            {'name': 'Comercial'},
                                            {'name': 'Secrétaire'},
                                            {'name': 'Chef de projet'},
                                            {'name': 'Developper'})
