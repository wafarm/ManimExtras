from manim import *
from .utils import distance
import numpy

class ArcByTwoDots(Arc):
    """Circle by two dots

    The first dot is the origin of the circle.
    The second dot is a dot on the circle.

    Animations like `Create()` will start from the second point. 

    """
    def __init__(self, dotA: Dot, dotB: Dot, angle, **kwargs):
        super().__init__(distance(dotA, dotB), start_angle=self._get_angle(dotA, dotB), angle=angle, **kwargs)

    def _get_angle(self, dotA: Dot, dotB: Dot):
        disx = dotB.get_x() - dotA.get_x()
        disy = dotB.get_y() - dotA.get_y()
        if disx == 0 and disy > 0:
            return PI / 2
        elif disx == 0 and disy < 0:
            return - PI / 2
        base_angle = numpy.arctan(abs(disy / disx))

        if disx > 0 and disy >= 0:
            return base_angle
        elif disx > 0 and disy < 0:
            return -base_angle
        elif disx < 0 and disy >= 0:
            return PI - base_angle
        else:
            return base_angle - PI