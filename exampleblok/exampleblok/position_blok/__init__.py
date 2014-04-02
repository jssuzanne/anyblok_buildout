from anyblok.blok import Blok


class PositionBlok(Blok):

    def install(self):
        for position in ('DG', 'Comercial', 'Secrétaire', 'Chef de projet',
                         'Developper'):
            self.registry.Position.insert(name=position)
