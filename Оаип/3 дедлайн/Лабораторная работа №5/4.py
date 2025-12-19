class Hero:
    def __init__(self,name,health=100,attack_power=20):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def strike(self,target):
        target.health-=self.attack_power