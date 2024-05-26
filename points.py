class Points:
    def __init__(self, health, happy, relation, money):
        self.health = health
        self.happy = happy
        self.relation = relation
        self.money = money
    def  __str__(self):
        return f"Sua pontuação nessa vida foi de: {(self.health+self.happy+self.relation+self.money)/4+1}"