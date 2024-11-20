from manim import *

class Title(Scene):

    def construct(self):

        europe = ImageMobject("worldmap.png")
        you = Dot(LEFT*3, color = PURPLE_A)
        you.shift(UP*1)

        
        '''
        c = Circle(2, color = RED, fill_opacity = 0.1)
        
        self.play(DrawBorderThenFill(c), run_time = 0.5)

        title = Text("Tailscale", font_size = 72, slant="ITALIC").shift(UP * 0.3)

        subtitle = Text("What is a VPN anyway", slant = "ITALIC", color = PURPLE_A).shift(DOWN * 0.5)

        self.play(Write(title), Write(subtitle))

        a = Arc(2.2, TAU * 1 / 4, -TAU * 2.6 / 4, color = BLUE, stroke_width=15)

        self.play(Create(a))

        self.wait(3)

        self.play(FadeOut(c, shift=DOWN * 2, scale=1.5))
        self.play(ReplacementTransform(a, c))
        self.play(FadeOut(title, shift=DOWN * 2, scale=1.5))
        self.play(FadeOut(subtitle, shift=DOWN * 2, scale=1.5))
        self.play(FadeOut(c, shift=DOWN * 2, scale=1.5))
        self.wait(1)
        '''

        self.play(FadeIn(europe, shift=DOWN * 2, scale=1))
        self.play(FadeIn(you, shift=DOWN * 2, scale=1))
        self.wait(2)
        


