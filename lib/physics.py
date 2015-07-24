def limit(vector, topSpeed):
    """ limits a vectors magnitude """
    if vector.magnitude() > topSpeed:
        return vector.setMag(topSpeed)
    else:
        return vector
