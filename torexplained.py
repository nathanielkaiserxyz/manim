from manim import *

class Title(Scene):
    def construct(self):
        # Load the map image
        europe = ImageMobject("worldmap.png")  # Scale if needed

        # Create dots
        you = Dot(LEFT * 3 + UP, color=PURPLE_A)
        tor1server = Dot(RIGHT * 5.3 + UP * 1, color=YELLOW_A)
        tor2server = Dot(RIGHT * 1.3 + DOWN * 2, color=YELLOW_A)
        tor3server = Dot(LEFT * 4 + UP * 1, color=YELLOW_A)
        destination = Dot(LEFT * 3 + DOWN * 2, color=PURPLE_A)

        # Create a traced path for "you"
        youline = TracedPath(you.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        # Add objects to the scene
        self.play(FadeIn(europe, shift=DOWN * 2))
        self.play(FadeIn(you), FadeIn(tor1server), FadeIn(tor2server), FadeIn(tor3server), FadeIn(destination))

        # Add traced path
        self.add(youline)

        # Animate movements
        self.play(you.animate.move_to(tor1server.get_center()))
        self.play(you.animate.move_to(tor2server.get_center())) 
        self.play(you.animate.move_to(tor3server.get_center())) 
        self.play(you.animate.move_to(destination.get_center()))
        self.play(you.animate.move_to(tor3server.get_center())) 
        self.play(you.animate.move_to(tor2server.get_center())) 
        self.play(you.animate.move_to(tor1server.get_center()))
        self.play(you.animate.move_to(LEFT * 3 + UP))  # Return to start

        self.wait(2)

        self.play(FadeOut(you), FadeOut(tor1server), FadeOut(tor2server), FadeOut(tor3server), FadeOut(destination))

        self.wait(2)