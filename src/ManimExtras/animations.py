from manim import *
from .mobjects import ArcByTwoDots

def CircleCreationWithLine(scene: Scene, dotA: Dot, dotB: Dot, **kwargs) -> Arc:
    """Circle creation animation with a line
    """
    return ArcCreationWithLine(scene, dotA, dotB, TAU, **kwargs)

def ArcCreationWithLine(scene: Scene, dotA: Dot, dotB: Dot, angle, **kwargs) -> Arc:
    arc = ArcByTwoDots(dotA, dotB, angle, **kwargs).move_arc_center_to(dotA.arc_center)
    line = Line(dotA, dotB)
    scene.play(Indicate(dotA))
    scene.play(Create(line))
    scene.play(Create(arc), Rotate(line, angle, about_point=dotA.get_center()))
    scene.play(Uncreate(line))
    return arc