class Player:
    def __init__(self, name, cords: tuple[int, int], hero, img):
        self.hero = hero  # pygame object which will be displayed on the screen
        self.name = name
        self.properties = []
        self.money = 1500
        self.position = 0
        self.cords = cords
        self.in_jail = False
        self.jail_turns = 0
        self.get_out_of_jail_free = False
        self.img = img

    # for debugging
    def __str__(self):
        return f"Name: {self.name}, properties: {self.properties}"
    
    
