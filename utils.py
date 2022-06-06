from manim import *

def distance(dotA: Dot, dotB: Dot):
    """Returns the distance between two dots
    """
    return ((dotA.get_x() - dotB.get_x()) ** 2 + (dotA.get_y() - dotB.get_y()) ** 2) ** 0.5

def deg(degree):
    return degree / 180 * PI
