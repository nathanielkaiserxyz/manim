from manim import *

class Title(Scene):

    def construct(self):
        """
        europe = ImageMobject("worldmap.png")
        
        you = Dot(LEFT*3, color = PURPLE_A)
        you.shift(UP*1)
        you2 = Dot(LEFT*3, color = PURPLE_A)
        you2.shift(UP*1)
        youline = TracedPath(you.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        vpnserver = Dot(RIGHT*2, color= YELLOW_A)
        vpnserver.shift(DOWN*1)
        destination = Dot(LEFT*3, color = PURPLE_A)
        destination.shift(DOWN*2)

        line1 = Line(you2.get_center(), vpnserver.get_center())
        line2 = Line(vpnserver.get_center(), destination.get_center())
        """

        
        
        c = Circle(2, color = RED, fill_opacity = 0.1)
        a = Arc(2.2, TAU * 1 / 4, -TAU * 2.6 / 4, color = BLUE, stroke_width=15)

        
        self.play(DrawBorderThenFill(c), run_time = 0.5)
        self.play(Create(a))
        title = Text("Tailscale", font_size = 72, slant="ITALIC").shift(UP * 0.3)

        subtitle = Text("What is a VPN anyway", slant = "ITALIC", color = WHITE).shift(DOWN * 0.5)

        self.play(Write(title), Write(subtitle))

       

        self.wait(3)

        self.play(FadeOut(c, shift=DOWN * 2, scale=1.5))
        self.play(ReplacementTransform(a, c))
        self.play(FadeOut(title, shift=DOWN * 2, scale=1.5))
        self.play(FadeOut(subtitle, shift=DOWN * 2, scale=1.5))
        self.play(FadeOut(c, shift=DOWN * 2, scale=1.5))
        self.wait(1)
        
        """ 
        self.play(FadeIn(europe, shift=DOWN * 2, scale=1))
        self.play(FadeIn(you, shift=UP * 2, scale=1))
        self.play(FadeIn(vpnserver, shift=UP * 2, scale=1))
        self.play(FadeIn(destination, shift=UP * 2, scale=1))
        self.add(you, you2, youline, vpnserver, destination)


        self.play(Succession(
            you.animate.move_to(vpnserver),
            you.animate.move_to(destination),
            you.animate.move_to(vpnserver),
            you.animate.move_to(you2)
        ))
        self.wait(2)
        """
        


