from manim import *

class Title(Scene):
    def construct(self):
        # Load the map image
        europe = ImageMobject("worldmap.png")  # Scale if needed

        # Create dots
        you = Dot(LEFT * 3 + UP, color=PURPLE_A)
        vpnserver = Dot(RIGHT * 2.3 + DOWN * 0.8, color=YELLOW_A)
        destination = Dot(LEFT * 3 + DOWN * 2, color=PURPLE_A)

        # Create a traced path for "you"
        youline = TracedPath(you.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        # Add objects to the scene
        self.play(FadeIn(europe, shift=DOWN * 2))
        self.play(FadeIn(you), FadeIn(vpnserver), FadeIn(destination))

        # Add traced path
        self.add(youline)

        # Animate movements
        self.play(you.animate.move_to(vpnserver.get_center()))
        self.play(you.animate.move_to(destination.get_center()))
        self.play(you.animate.move_to(vpnserver.get_center()))
        self.play(you.animate.move_to(LEFT * 3 + UP))  # Return to start

        self.wait(2)

        self.play(FadeOut(you), FadeOut(vpnserver), FadeOut(destination))

        self.wait(2)