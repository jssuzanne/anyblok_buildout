from anyblok.blok import Blok


class DeskBlok(Blok):

    version = '1.0.0'

    def install(self):
        """ this method is call at the installation of this blok """
        address = self.registry.Address.insert(street='14-16 rue Soleillet',
                                               zip='75020', city='Paris')
        self.registry.Room.insert(number=308, address=address)
