import random

from settings import points, action_hero
from exceptions import Enemy_down, Game_over


class Enemy:
    def __init__(self, level: int):
        self.health_points = level
        self.action = str

    def descrease_health(self):
        self.health_points -= 1
        if self.health_points == 0:
            msg = f'Enemy is draw. His heals equal {self.health_points}'
            raise Enemy_down(msg)

    def select_attack(self):
        return random.choice(list(action_hero.values()))

    def select_defence(self):
        return random.choice(list(action_hero.values()))


class Player:
    def __init__(self, name: str):
        self.player_name = name
        self.health_points = points

    def select_attack(self):
        while True:
            try:
                attack = input('Select attack mode - Warrior as wa, Robber as ro, Wizard as wi: ')
                return action_hero[attack]
            except KeyError:
                print('You enter wrong value')

    def select_defence(self):
        while True:
            try:
                defence = input('Select defence mode - Warrior as wa, Robber as ro, Wizard as wi: ')
                return action_hero[defence]
            except KeyError:
                print('You enter wrong value')

    def descrease_health(self):
        self.health_points -= 1
        if self.health_points == 0:
            msg = f'Player {self.player_name} is draw. His heals equal {self.health_points}'
            raise Game_over(msg)

    @staticmethod
    def fight(attack, defence):
        if attack == 'Warrior' and defence == 'Robber' or attack == 'Robber' and defence == 'Wizard' \
                or attack == 'Wizard' and defence == 'Warrior':
            return True
        else:
            return False

    def attack(self, enemy_obj: object):
        if self.fight(attack=self.select_attack(), defence=enemy_obj.select_defence()):
            enemy_obj.descrease_health()
            self.health_points += 1
            print(
                f'YOUR ATTACK IS SUCCESSFUL! \n {self.player_name} health is: {self.health_points} \n Enemy health is: {enemy_obj.health_points}')
        else:
            print(
                f"YOUR ATTACK IS FAILED!\n{self.player_name} health is: {self.health_points} \n Enemy health is: {enemy_obj.health_points}")

    def defence(self, enemy_obj: object):
        if self.fight(attack=enemy_obj.select_attack(), defence=self.select_defence()):
            self.descrease_health()
            print(
                f'YOUR DEFENCE IS FAILED! \n {self.player_name} health is: {self.health_points}\n Enemy health is {enemy_obj.health_points}')
        else:
            print(f"YOUR DEFENCE IS SUCCESSFUL!\n {self.player_name} health is: {self.health_points}"
                  f"\n Enemy health is {enemy_obj.health_points}")
