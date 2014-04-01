from anyblok.blok import Blok


class PositionBlok(Blok):

    def install(self):
        for position in ('DG', 'Cormercial', 'Secrétaire', 'Chef de projet',
                         'Developper'):
            self.registry.Position.insert(name=position)
