def limit(vector, topSpeed):
    """ limits a vectors magnitude """
    if vector.magnitude() > topSpeed:
        return vector.setMag(topSpeed)
    else:
        return vector

def applyFroce(vector, mass, *arg):
    """accumulates all the force vectors together before applying them"""
    for i in range(len(arg)):
        # print type(i)
        vector += arg[i]/mass
    return vector

def checkEdges(thing, width, height):
    """keeps an object inside the screen"""
    if thing.location.x > width:
        thing.location.x = width
        thing.velocity.x *= -1
    if thing.location.x < 0:
        thing.location.x = 0
        thing.velocity.x *= -1
    if thing.location.y > height:
        thing.location.y = height
        thing.velocity.y *= -1
    if thing.location.y < 0:
        thing.location.y = 0
        thing.velocity *= -1
