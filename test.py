from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(WHITE, opacity=0.5)  
        self.play(Create(circle))  # show the circle on screen
