class Character:
    def __init__(self,name: str,life: int,damage: int):
        if life <= 0:
            raise ValueError(f"Life: {life} must be greater than zero.")
        if damage < 0:
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
        if amount < 0:
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
            raise ValueError(f"{self.name} is dead and cannot be healed.")
        life_before = self.life
        self.life = min(self.max_life, self.life + amount)
        result_life = self.life - life_before
        return result_life

    def battle(self, enemy: "Character") -> str:
        print(f"Battle: {self.name} vs {enemy.name}")
        if self.damage == 0 and enemy.damage == 0:
            return "draw"
        rounds = 0
        print("Starting Battle")
        while self.is_alive and enemy.is_alive and rounds < 100:
            print(f"attack: {self.attack(enemy)}")
            print(f"attack: {enemy.attack(self)}")
            rounds = rounds + 1
        if self.is_alive and enemy.is_alive:
            return "draw"
        if self.is_alive:
            winner = self.name
            return f"winner: {winner}"
        else:
            winner = enemy.name
            return f"winner: {winner}"


hero = Character("hero", 100, 10)
hero.take_damage(90)
print(hero.life)
print(hero.heal(100))

superman = Character("superman", 100, 30)
lex = Character("lex lutor", 50, 10)
goblin = Character("goblin", 20, 5)
witch = Character("witch of the castle",100,45)
fairy = Character("fairy",100,35)

pacifist1 = Character("monk", 100, 0)
pacifist2 = Character("priest", 100, 0)
print(pacifist1.battle(pacifist2))
print(pacifist2.battle(pacifist1))