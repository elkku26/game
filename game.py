#Super perpin seikkailut
import items
import time
import worldMap
from player import Player
Player = Player()
#While using move, DX comes before DY
worldMap.Startroom.intro_text()
this_again = False
def play():
    while True:
        action = input("").lower()

        if action in ["move", "walk"]:
            worldMap.s_print("Where will you move?")
            action = input("").lower()

            if action in ["north", "n"]:
                Player.move(0, -1)
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(0, 1)
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''

            if action in ["south", "s"]:
                Player.move(0, 1)
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(0, -1)
                    worldMap.s_print("That's a wall. Try again")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''
            if action in ["east", "e"]:
                Player.move(1, 0)
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(-1, 0)
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''
            if action in ["west", "w"]:
                Player.move(-1, 0)
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(1, 0)
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''

        if action in ["examine", "look around", "examine room", "examine area"]:
            worldMap.Startroom.description()

        if action in ["examine me", "examine self", "me", "self", "status"]:
            if Player.health > 15 or Player.health == 15:
                worldMap.s_print("You're slightly confused, but you aren't really hurt at all. You can definitely manage like this.")
            if 10 < Player.health < 15:
                worldMap.s_print("You're feeling pretty bad. You can't survive long like this.")
            if Player.health < 10 or Player.health == 10:
                worldMap.s_print("You're in critical condition. You need help soon, or you'll perish.")

        if action in ["inventory", "belongings", "examine inventory", "examine belongings", "check inventory", "check belongings"]:
            for i in Player.inventory:
                worldMap.s_print(i.__str__())
            worldMap.s_print("What will you do?")
            play()


        for i in Player.inventory:
            if action == i.name.lower() + ' info':
                worldMap.s_print(i.description)
        worldMap.s_print("What is your next move?")

        play()



play()

print(Player.get_location())
print(Player.get_room())
print(worldMap.StartRoom)