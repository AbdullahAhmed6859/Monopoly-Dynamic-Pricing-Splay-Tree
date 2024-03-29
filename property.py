class Property:
    def __init__(self, key, name, price, rent):
        self.key = key  # key references the index of the property in the board list and the splay Tree
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    # for debugging
    def __str__(self):
        return self.name + ": " + str(self.value) + " (" + str(self.owner) + ")"
