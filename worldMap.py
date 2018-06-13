#Sample map:
#format is map[y][x]
#
#    X       X       X
#Y	(0,0)---(0,1)---(0,2)
#Y	(1,0)---(1,1)---(1,2)
#Y 	(2,0)---(2,1)---(2,2)

import time
import sys

def s_print(text):
    for i in range(len(text)):
        sys.stdout.flush()
        sys.stdout.write(text[i])
        time.sleep(0.1)
        sys.stdout.flush()
    print("")

class Maptile:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

#Starting room
class StartRoom(Maptile):
    def intro_text(self):
        s_print('''You're in a dimly lit room, and there is a nice cabinet and a table with a candle on top.
What will you do?''')

    def description(self):
        s_print("You decide to look around some more.")
        time.sleep(0.5)
        s_print("Your eyes glance upon the door, which is locked with a large padlock. The cabinet next to the wall is made of wood and has vine-like patterns imprinted on it.")


    def __str__():
        return "StartRoom is located at coordinates 1, 0"







class Secretroom(Maptile):

    def intro_text(self):
        s_print('After crawling through the secret path, you find a small room, with a chest in the back of the room.')


    def __repr__():
        play_secretroom()


hallway1, hallway2, hallway3, dining_hall, secret_shortcut, win_tile = "this is hallway1", "this is hallway2", "this is hallway3", "this is the dining hall", "this is the secret shortcut", "this is the win tile"

world_map = [
[Secretroom, None, None, None],
[StartRoom, None, None, None],	
[hallway1, hallway2, dining_hall, secret_shortcut, None],
[hallway3, None, None, None, None],
[win_tile, None, None, None, None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None