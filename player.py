again = 0
import time
import worldMap
import items
class Player:
    def __init__(self):
        self.inventory = [items.Gold(5), items.Stick()]
        self.health = 20
        self.y = 1
        self.x = 0

#dx and dy stand for change in x and change in y 
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(0, -1)
        if worldMap.tile_at(self.x, self.y) is None:
            self.move(0, 1)
            worldMap.s_print("That's a wall. Try again.")
            time.sleep(0.5)
            worldMap.s_print("What will you do?")
            again = 1

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(0, -1)
        if worldMap.tile_at(self.x, self.y) is None:
            self.move(0, 1)
            worldMap.s_print("That's a wall. Try again.")
            time.sleep(0.5)
            worldMap.s_print("What will you do?")


    #get_location is to be used for debugging purposes only. get_x and get_y are for functions
    def get_location(self):
        return "X: {} Y: {}".format(self.x, self.y)

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x


    def get_room(self):
         return worldMap.world_map[self.y][self.x]

    def check_inventory(self):
        for i in self.inventory:
            worldMap.s_print("* " + i.__str__())
        worldMap.s_print("What will you do?")

    def check_condition(self):
        if self.health > 15 or self.health == 15:
            worldMap.s_print("You're slightly confused, but you aren't really hurt at all. You can definitely manage like this.")
        if 10 < self.health < 15:
            worldMap.s_print("You're feeling pretty bad. You can't survive long like this.")
        if self.health < 10 or self.health == 10:
            worldMap.s_print("You're in critical condition. You need help soon, or you'll perish.")