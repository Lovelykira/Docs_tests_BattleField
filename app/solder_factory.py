from app.solder import Solder


class SolderFactory:
    """
    Class that creates Solder objects.
    """
    @classmethod
    def create(cls):
        """
        Create Solder.

        Creates Solder object
        :return: Solder object.
        """
        solder = Solder()
        return solder
