def limit(vector, topSpeed):
    if vector.magnitude() > topSpeed:
        return vector.setMag(topSpeed)
    else:
        return vector
