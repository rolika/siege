"""The player in Siege! controlls a hero, who
- is placed on the bastion of his castle
- can move left and right, constrained by two towers on both ends of his bastion
- can pick up barrels at the towers
- can hurl barrels downwards at its enemies"""


from pygame import sprite, Surface  # this way, IntelliSense works in VS Code


class Player(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = Surface((20, 60))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom=pos)
