
# class Monster:
#     print("I am inside the class body")
    
#     def first_param(self):
#         print("I am the first loop")    
        
#     def second_param(self, second):
#         sum = second + 100
#         print(sum)
        
#     def third_param(self, num1, num2):
#         quotient = num1/ num2
#         print(quotient)
        
        
        
# monst = Monster()
# monst.first_param()
# monst.second_param(1)
# monst.third_param(3,6)

# MONSTER = Monster()
# MONSTER.first_param()
# MONSTER.second_param(10)
# MONSTER.third_param(3,5)

# exercise
class Entity:
    def attack(self):
        print(f"Attack with {self.damage} damage")
        print(self.Monster.damage())
        
class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    

monster = Monster(100, 5)

print(monster.health)
monster.attack()