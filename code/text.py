"""Classes to display text information. Texts are represented as sprites."""


from pygame import sprite, freetype


class Text(sprite.Sprite):
    def __init__(self, text, fontname, size, color, pos):
        super().__init__()
        self._text = text
        self._fonttype = freetype.Font(fontname, size)
        self._color = color
        self.rect = self.image.get_rect(midtop=pos)
    
    @property
    def image(self):
        return self._fonttype.render(self._text, self._color)[0]


class Score(sprite.Sprite):
    def __init__(self,fontname, size, color, pos):
        super().__init__()
        self._text = "score: {:07}".format(0)
        self._fonttype = freetype.Font(fontname, size)
        self._color = color
        self.rect = self.image.get_rect(topleft=pos)
    
    @property
    def image(self):
        return self._fonttype.render(self._text, self._color)[0]

    def update(self, score=0):
        self._text = "score: {:07}".format(score)


class HiScore(sprite.Sprite):
    def __init__(self, fontname, size, color, pos):
        super().__init__()
        self._text = "hiscore: {:07}".format(0)
        self._fonttype = freetype.Font(fontname, size)
        self._color = color
        self.rect = self.image.get_rect(topright=pos)
    
    @property
    def image(self):
        return self._fonttype.render(self._text, self._color)[0]

    def update(self, score=0):
        self._text = "hiscore: {:07}".format(score)
