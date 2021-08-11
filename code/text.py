"""Classes to display text information. Texts are represented as sprites."""


from pygame import sprite, Surface, font


class Text(sprite.Sprite):
    def __init__(self, text, fontname, size, color, pos):
        super().__init__()
        fonttype = font.Font(fontname, size)
        self.image = fonttype.render(text, True, color)
        self.rect = self.image.get_rect(midtop=pos)


class Score(sprite.Sprite):
    def __init__(self,fontname, size, color, pos):
        super().__init__()
        self._text = "score: {:07}".format(0)
        fonttype = font.Font(fontname, size)
        self.image = fonttype.render(self._text, True, color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, score=0):
        self._text = "score: {:07}".format(score)


class HiScore(sprite.Sprite):
    def __init__(self, fontname, size, color, pos):
        super().__init__()
        self._text = "hiscore: {:07}".format(0)
        fonttype = font.Font(fontname, size)
        self.image = fonttype.render(self._text, True, color)
        self.rect = self.image.get_rect(topright=pos)

    def update(self, score=0):
        self._text = "hiscore: {:07}".format(score)
