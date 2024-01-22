# inheritance - 1
# 상속

class Monster:

    def __init__(self, hp, name, damage):
        self.hp = hp
        self.name = name
        self.damage = damage

    def attack(self, character):
        character.hp -= self.damage

class Slime(Monster):

    def __init__(self, hp, name, damage, poison):
        super().__init__(hp, name, damage)
        self.poison = poison

    def sprayPoison(self, character):
        character.hp -= self.damage + self.poison

a = Slime(50, '귀여운 슬라임', 30, 5)