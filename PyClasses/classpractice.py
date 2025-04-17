"""Module that produces a projectile to be fired."""
class Projectile:
    """ docstring """

    size = 0
    colour = "grey"

    def __init__(self, size, colour):

        self.size = size
        self.colour = colour

    def getsize(self):
        """ docstring """
        return self.size

    def getcolour(self):
        """ docstring """

        return self.colour
    
    def setsize(self, value):
        """ docstring """

        self.size = value

        return self.size

    def setcolour(self, value):
        """ docstring """

        self.colour = value

        return self.colour

projectile1 = Projectile(size=5, colour="red")
projectile2 = Projectile(10, "Blue")

print(Projectile.colour) # grey
print(Projectile.size)  # 0
print(projectile1.getcolour()) # red
print(projectile1.getsize()) # 5

projectile1.setcolour("Orange")
projectile1.setsize(100)
projectile2.setcolour("Purple")
projectile2.setsize(50)

print(projectile1.getcolour())
print(projectile1.getsize())
print(projectile2.getcolour())
print(projectile2.getsize())
