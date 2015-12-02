class Flower:
    """A botanical flower"""

    def __init__(self, name, petals, price):
        """Create new flower instance.

        name    the name of the flower
        petals  the number of petals that the flower has
        price   the price of the flower
        """
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        """Return name of the flower"""
        return self._name

    def get_petals(self):
        """Return number of petals that the flower has"""
        return self._petals

    def get_price(self):
        """Return the price of the flower"""
        return self._price

    def set_name(self, name):
        """Set the name of the flower"""
        self._name = name

    def set_petals(self, petals):
        """Set the number of petals for the flower"""
        self._petals = petals

    def set_price(self, price):
        """Set the price of the flower"""
        self._price = price
