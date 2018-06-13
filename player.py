from worldMap import world_map
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

    #get_location is to be used for debugging purposes only. get_x and get_y are for functions
    def get_location(self):
        return "X: {} Y: {}".format(self.x, self.y)

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x


    def get_room(self):
         return world_map[self.y][self.x]
