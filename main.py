class Character:
    def __init__(self,name: str,life: int,damage: int):
        if life <= 0:
            raise ValueError(f"Life: {life} must be greater than zero.")
        if damage <= 0:
            raise ValueError(f"Damage: {damage} cannot be negative.")
        self.name = name 
        self.life = life
        self.damage = damage
        self.max_life = life
        self.level = 1
        self.xp = 0

    @property
    def is_alive(self) -> bool:
        return self.life > 0

    def take_damage(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError(f"Damage: {amount} cannot be negative.")
        self.life = max(0, self.life - amount)
        return amount

    def attack(self, enemy: "Character") -> str:
        if not self.is_alive:
            return f"{self.name} is dead and cannot attack."
        if not enemy.is_alive:
            return f"{enemy.name} is already defeated."
        if enemy is self:
            return f"{self.name} cannot attack itself."
        damage_dealt = enemy.take_damage(self.damage)
        return f"{self.name} attacked {enemy.name} for {damage_dealt} damage."

    def heal(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError(f"healing value: {amount} cannot be negative or zero")
        if not self.is_alive:
            raise ValueError(f"{self.name} It is dead and cannot be cured.")
        life_before = self.life
        self.life = min(self.max_life, self.life + amount)
        result_life = self.life - life_before
        return f"the cure rate was: {result_life}"


hero = Character("hero", 100, 10)
hero.take_damage(90)
print(hero.life)
print(hero.heal(100))

superman = Character("superman", 100, 30)
lex = Character("lex lutor", 50, 10)
goblin = Character("goblin", 20, 5)
witch = Character("witch of the castle",100,45)
fairy = Character("fairy",100,35)

print("Battle 1: superman vs lex")
print(superman.attack(lex))
print(superman.attack(lex))
print(superman.attack(lex))
print(lex.attack(superman))

print("Battle 2: hero vs goblin")
while goblin.is_alive and hero.is_alive:
    print(hero.attack(goblin))
    print(goblin.attack(hero))
print(hero.heal(20))

print("Battle 3: superman vs hero")
while hero.is_alive:
    print(superman.attack(hero))
print(hero.attack(superman))

print("Battle 4: invalid attack")
print(superman.attack(superman))

print("Battle 5: witch vs fairy")
print(witch.attack(fairy))
print(fairy.life)
print(fairy.attack(witch))
print(fairy.life)
print(witch.life)
while witch.is_alive:
    print(fairy.attack(witch))
print(witch.life)