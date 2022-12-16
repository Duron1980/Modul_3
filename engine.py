from models import Enemy, Player
from exceptions import Enemy_down, Game_over


def play():
    enemy_health_level = 2
    enemy = Enemy(enemy_health_level)
    player_name = input('Please enter your name: ')
    player = Player(player_name)
    print('Start Game\n'
          f'Health points of {player.player_name} is {player.health_points}\n'
          f'Health points of Enemy is  {enemy.health_points}')
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except Enemy_down as error:
            print(f'YOUR ATTACK IS SUCCESSFUL! {error}')
            exit = input('Do you wont to continue (y/n):')
            if exit == 'n':
                break
            enemy_health_level += 1
            enemy = Enemy(enemy_health_level)
            player.health_points += 1
        except Game_over as error:
            print(f"Game over. {error}")
            break


if __name__ == '__main__':
    play()
