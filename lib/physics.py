def limit(vector, topSpeed):
    """ limits a vectors magnitude """
    if vector.magnitude() > topSpeed:
        return vector.setMag(topSpeed)
    else:
        return vector

def applyFroce(vector, *arg):
    """accumulates all the force vectors together before applying them"""
    for i in range(len(arg)):
        # print type(i)
        vector += arg[i]
    return vector
