#Super perpin seikkailut
import items
import time
import worldMap
from player import Player
import player
#While using move, DX comes before DY
Player = Player()


#Starts the game
#The player stays in this loop until they move
#-----------------------------------------------------------------------------------------------------------------------------------#
#Removed temporarily
#worldMap.Startroom.intro_text()
print("Startcoordinates: {},{}".format(Player.x, Player.y))
def play():
    while True:
        action = input("").lower()

        if action in ["move", "walk"]:
            worldMap.s_print("Where will you move?")
            action = input("").lower()

            if action in ["north", "n"]:
                Player.move(0, -1)
                print("Coordinates: {},{}".format(Player.x, Player.y))
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(0, 1)
                    print("Coordinates: {},{}".format(Player.x, Player.y))
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()
                return ''

            if action in ["south", "s"]:
                Player.move(0, 1)
                print("Coordinates: {},{}".format(Player.x, Player.y))
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(0, -1)
                    print("Coordinates: {},{}".format(Player.x, Player.y))
                    worldMap.s_print("That's a wall. Try again")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''

            if action in ["east", "e"]:
                Player.move(1, 0)
                print("Coordinates: {},{}".format(Player.x, Player.y))
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(-1, 0)
                    print("Coordinates: {},{}".format(Player.x, Player.y))
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''

            if action in ["west", "w"]:
                Player.move(-1, 0)
                print("Coordinates: {},{}".format(Player.x, Player.y))
                if worldMap.tile_at(Player.x, Player.y) is None:
                    Player.move(1, 0)
                    print("Coordinates: {},{}".format(Player.x, Player.y))
                    worldMap.s_print("That's a wall. Try again.")
                    time.sleep(0.5)
                    worldMap.s_print("What will you do?")
                    play()

                return ''

        if action in ["examine", "look around", "examine room", "examine area"]:
            worldMap.Startroom.description()

        if action in ["examine me", "examine self", "me", "self", "status"]:
            Player.check_condition()


        if action in ["inventory", "belongings", "examine inventory", "examine belongings", "check inventory", "check belongings"]:
            Player.check_inventory()
            play()


        play()
#IMPORTANT NOTE:
#Because most rooms are placeholders you can't move there yet.
#------------------------------------------------------------------------------------------------------------------------------------#
def play_secretroom():
    pass


play()