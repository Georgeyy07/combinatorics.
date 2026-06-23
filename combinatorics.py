from manim import *

'''
Named combinatorics for easier understanding, this manim file is a bunch of different Scenes and animations
using different types of scenes
'''

def make_card(value, suit, width=1.4, height=1.6):
    card = VGroup()
    bg = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.1,
        fill_color=WHITE, fill_opacity=1,
        stroke_color=GREY, stroke_width=2
    )
    color = RED if suit in ["♥", "♦"] else "#1A1A1A"
    label_text = Text(f"{value}\n{suit}", font_size=24, color=color, font="Arial", weight=BOLD)
    label_text.set_stroke(color=BLACK, width=0.5)
    
    top_label = label_text.copy().align_to(bg, UP + LEFT).shift(0.15 * (DOWN + RIGHT))
    bottom_label = label_text.copy().rotate(PI).align_to(bg, DOWN + RIGHT).shift(0.15 * (UP + LEFT))
    
    card.add(bg, top_label, bottom_label)
    return card

class shufflingCards(Scene):
    def construct(self):
        self.wait(3.3)
        comeback = Text("I can write a bigger one in two seconds.", color=WHITE, font_size=40)
        
        comeback.set_stroke(color=BLACK, width=1)

        self.play(Write(comeback)) # use Write for text instead of Create
        self.wait(1.5)
        self.play(FadeOut(comeback))

        my_card1 = make_card("A", "♥").center()
        c2 = make_card("4", "♣").move_to([2.5, 2.5, 0])
        c3 = make_card("K", "♠").move_to([-2.5, -2.5, 0])
        c4 = make_card("3", "♦").move_to([-2.5, 2.5, 0])
        c5 = make_card("7", "♥").move_to([2.5, -2.5, 0])

        self.play(Create(my_card1), Create(c2), Create(c3), Create(c4), Create(c5))
        self.wait(1)

        # collapse them into the middle
        # they all slide to the center sitting directly on top of my_card1
        self.play(
            c2.animate.move_to(ORIGIN),
            c3.animate.move_to(ORIGIN),
            c4.animate.move_to(ORIGIN),
            c5.animate.move_to(ORIGIN),
            run_time=0.5
        )

        # swap out the cards cleanly
        next_c1 = make_card("K", "♠").move_to(ORIGIN)
        next_c2 = make_card("2", "♠").move_to(ORIGIN)
        next_c3 = make_card("9", "♣").move_to(ORIGIN)
        next_c4 = make_card("J", "♦").move_to(ORIGIN)
        next_c5 = make_card("8", "♥").move_to(ORIGIN)

        # fade out the old stack and fade in the new stack instantly
        self.play(
            FadeOut(my_card1), FadeOut(c2), FadeOut(c3), FadeOut(c4), FadeOut(c5),
            FadeIn(next_c1), FadeIn(next_c2), FadeIn(next_c3), FadeIn(next_c4), FadeIn(next_c5),
            run_time=0.2
        )

        # shuffle again
        self.play(
            next_c2.animate.move_to([2.5, 2.5, 0]),
            next_c3.animate.move_to([-2.5, -2.5, 0]),
            next_c4.animate.move_to([-2.5, 2.5, 0]),
            next_c5.animate.move_to([2.5, -2.5, 0]),
            run_time=0.8,
        )
        self.wait(1)

        self.play(
            ReplacementTransform(next_c2, next_c1), 
            ReplacementTransform(next_c3, next_c1), 
            ReplacementTransform(next_c4, next_c1), 
            ReplacementTransform(next_c5, next_c1), 
        )

        # ----------------------------------------- third shuffle
        # swap out the cards cleanly
        last_c1 = make_card("Q", "♠").move_to(ORIGIN)
        last_c2 = make_card("A", "♠").move_to(ORIGIN)
        last_c3 = make_card("5", "♣").move_to(ORIGIN)
        last_c4 = make_card("4", "♦").move_to(ORIGIN)
        last_c5 = make_card("7", "♥").move_to(ORIGIN)

        # fade out the old stack and fade in the new stack instantly
        self.play(
            FadeOut(next_c1), FadeOut(next_c2), FadeOut(next_c3), FadeOut(next_c4), FadeOut(next_c5),
            FadeIn(last_c1), FadeIn(last_c2), FadeIn(last_c3), FadeIn(last_c4), FadeIn(last_c5),
            run_time=0.2
        )

        # shuffle again
        self.play(
            last_c2.animate.move_to([2.5, 2.5, 0]),
            last_c3.animate.move_to([-2.5, -2.5, 0]),
            last_c4.animate.move_to([-2.5, 2.5, 0]),
            last_c5.animate.move_to([2.5, -2.5, 0]),
            run_time=0.8,
        )
        self.wait(1)

        self.play(
            FadeOut(last_c2),
            FadeOut(last_c3),
            FadeOut(last_c4),
            FadeOut(last_c5),
            FadeOut(last_c1),
        )

class Factorial(Scene):
    def construct(self):
        self.wait(4.5)
        self.camera.background_color = "#0A0A0A"

        def num(txt, size=120, col=WHITE):
            m = Text(txt, font_size=size, color=col, weight=BOLD)
            m.set_stroke(BLACK, width=3, background=True)
            return m

        def mul(size=70):
            m = Text("×", font_size=size, color="#666666", weight=BOLD)
            m.set_stroke(BLACK, width=2, background=True)
            return m

        # 52 fades in centered
        n52 = num("52", 130)
        n52.move_to(ORIGIN)
        self.play(FadeIn(n52), run_time=0.7)

        sub52 = Tex("choices for the 1st card", font_size=36, color="#a8a5a5")
        sub52.set_stroke(BLACK, width=1, background=True)
        sub52.next_to(n52, DOWN, buff=0.35)
        self.play(FadeIn(sub52, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        # drift left then 51 comes in
        x1  = mul(80)
        n51 = num("51", 130)

        row1_ref = VGroup(num("52",130), mul(80), num("51",130))
        row1_ref.arrange(RIGHT, buff=0.45).move_to(ORIGIN)

        x1.move_to(row1_ref[1].get_center() + RIGHT * 7)
        n51.move_to(row1_ref[2].get_center() + RIGHT * 9)

        self.play(
            FadeOut(sub52, shift=DOWN*0.08, run_time=0.3),
            n52.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row1_ref[0].get_center()),
            x1.animate(rate_func=rate_functions.ease_out_cubic)
              .move_to(row1_ref[1].get_center()),
            n51.animate(rate_func=rate_functions.ease_out_cubic)
               .move_to(row1_ref[2].get_center()),
            run_time=0.75,
        )

        sub51 = Tex("choices for the 2nd card", font_size=36, color="#a8a5a5")
        sub51.set_stroke(BLACK, width=1, background=True)
        sub51.next_to(n51, DOWN, buff=0.35)
        self.play(FadeIn(sub51, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        # s51 shifts, have 50 come in
        x2  = mul(65)
        n50 = num("50", 110)

        row2_ref = VGroup(num("52",110), mul(65), num("51",110), mul(65), num("50",110))
        row2_ref.arrange(RIGHT, buff=0.35).move_to(ORIGIN)

        x2.move_to(row2_ref[3].get_center() + RIGHT * 7)
        n50.move_to(row2_ref[4].get_center() + RIGHT * 9)

        self.play(
            FadeOut(sub51, shift=DOWN*0.08, run_time=0.3),
            n52.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row2_ref[0].get_center())
               .scale(row2_ref[0].height / n52.height),
            x1.animate(rate_func=rate_functions.ease_in_out_quad)
              .move_to(row2_ref[1].get_center())
              .scale(row2_ref[1].height / x1.height),
            n51.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row2_ref[2].get_center())
               .scale(row2_ref[2].height / n51.height),
            x2.animate(rate_func=rate_functions.ease_out_cubic)
              .move_to(row2_ref[3].get_center()),
            n50.animate(rate_func=rate_functions.ease_out_cubic)
               .move_to(row2_ref[4].get_center()),
            run_time=0.8,
        ) # a bunch of vibe code slop that I left because it works

        sub50 = Tex("choices for the 3rd card", font_size=34, color="#a8a5a5")
        sub50.set_stroke(BLACK, width=1, background=True)
        sub50.next_to(n50, DOWN, buff=0.3)
        self.play(FadeIn(sub50, shift=UP*0.1), run_time=0.5)
        self.wait(1.0)

        # 49 eases in
        x3  = mul(55)
        n49 = num("49", 95)

        row3_ref = VGroup(
            num("52",95), mul(55), num("51",95), mul(55),
            num("50",95), mul(55), num("49",95)
        )
        row3_ref.arrange(RIGHT, buff=0.28).move_to(ORIGIN)

        x3.move_to(row3_ref[5].get_center() + RIGHT * 7)
        n49.move_to(row3_ref[6].get_center() + RIGHT * 9)

        self.play(
            FadeOut(sub50, shift=DOWN*0.08, run_time=0.3),
            n52.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row3_ref[0].get_center())
               .scale(row3_ref[0].height / n52.height),
            x1.animate(rate_func=rate_functions.ease_in_out_quad)
              .move_to(row3_ref[1].get_center())
              .scale(row3_ref[1].height / x1.height),
            n51.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row3_ref[2].get_center())
               .scale(row3_ref[2].height / n51.height),
            x2.animate(rate_func=rate_functions.ease_in_out_quad)
              .move_to(row3_ref[3].get_center())
              .scale(row3_ref[3].height / x2.height),
            n50.animate(rate_func=rate_functions.ease_in_out_quad)
               .move_to(row3_ref[4].get_center())
               .scale(row3_ref[4].height / n50.height),
            x3.animate(rate_func=rate_functions.ease_out_cubic)
              .move_to(row3_ref[5].get_center()),
            n49.animate(rate_func=rate_functions.ease_out_cubic)
               .move_to(row3_ref[6].get_center()),
            run_time=0.8,
        ) # more claude slop

        self.wait(0.7)

        # the rest of the 52!
        dots = Text("× 48 × 47 × 46 × ··· × 2 × 1",
                    font_size=32, color="#666666")
        dots.set_stroke(BLACK, width=1, background=True)

        all_mobs = [n52, x1, n51, x2, n50, x3, n49]

        compact_ref = VGroup(
            num("52",50), mul(36), num("51",50), mul(36),
            num("50",50), mul(36), num("49",50),
        )
        compact_ref.arrange(RIGHT, buff=0.16)

        full_line_ref = VGroup(compact_ref, dots.copy()).arrange(RIGHT, buff=0.2)
        full_line_ref.move_to(UP * 1.3)

        dots.move_to(full_line_ref[1].get_center())
        dots.set_opacity(0)

        self.play(
            *[all_mobs[i].animate(rate_func=rate_functions.ease_in_out_sine)
                .move_to(full_line_ref[0][i].get_center())
                .scale(full_line_ref[0][i].height / all_mobs[i].height)
              for i in range(len(all_mobs))],
            dots.animate.set_opacity(1),
            run_time=0.85,
        )
        self.wait(1.3)

        # have it come up to the top of the screen
        eq_text  = Text("=", font_size=46)
        fact_lbl = Text("52!", font_size=62, color="#FFD700", weight=BOLD)
        fact_lbl.set_stroke(BLACK, width=2, background=True)

        eq_row = VGroup(eq_text, fact_lbl).arrange(RIGHT, buff=0.3)
        eq_row.next_to(full_line_ref, DOWN, buff=0.5)

        self.play(
            FadeIn(eq_row, shift=UP*0.2),
            rate_func=rate_functions.ease_out_cubic,
            run_time=0.6,
        )
        self.wait(0.8)

        # 52! comes into the center have all mobjects FadeOut
        all_except_fact = VGroup(*all_mobs, dots, eq_text)
        self.play(
            FadeOut(all_except_fact),
            fact_lbl.animate(rate_func=rate_functions.ease_in_out_sine)
                    .scale(2.3).move_to(ORIGIN),
            run_time=0.8,
        )
        self.wait(2.7)

        # 52! goes back to the top and the large number comes
        self.play(
            fact_lbl.animate(rate_func=rate_functions.ease_in_out_cubic)
                    .scale(0.42).to_edge(UP, buff=1),
            run_time=0.6,
        )

        eq2 = Tex(r"\textbf{=}", font_size=40)
        eq2.set_stroke(BLACK, width=1, background=True)

        row_strs = [
            "80,658,175,170,943,",
            "878,571,660,636,856,",
            "403,766,975,289,505,",
            "440,883,277,824,000,",
            "000,000,000,000",
        ] # eighty unvigintillion (uhn-vij-in-til-yun)
        number_rows = VGroup(*[
            Tex(r, font_size=56, color=WHITE)
            for r in row_strs
        ])
        number_rows.set_stroke(BLACK, width=1, background=True)
        number_rows.arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        block = VGroup(eq2, number_rows).arrange(RIGHT, buff=0.3, aligned_edge=UP)
        block.move_to(DOWN * 0.25)

        self.play(FadeIn(eq2, shift=UP*0.1), run_time=0.35)

        for row in number_rows:
            self.play(
                FadeIn(row, shift=UP*0.08),
                rate_func=rate_functions.ease_out_sine,
                run_time=0.28,
            )

        self.wait(0.7)

        # 68 digits
        digit_note = Tex(r"\textbf{68 digits.}", font_size=40, color="#FFD700")
        digit_note.set_stroke(BLACK, width=1, background=True)
        digit_note.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(digit_note, shift=UP*0.1), run_time=0.5)
        self.wait(1.8)

        # fade all Mobjects out, can also do *[FadeOut(mob) for mob in self.mobjects]
        self.play(
            FadeOut(VGroup(fact_lbl, eq2, number_rows, digit_note)),
            run_time=0.8,
        )
        self.wait(0.5)

        chess_line = Tex(
            # say "but compared to the possibilities of chess games, it is, ..."
            "nothing", # "let me explain" < right after
            font_size=68, color=WHITE
        )
        chess_line.set_stroke(BLACK, width=2, background=True)
        chess_line.move_to(ORIGIN)

        self.play(FadeIn(chess_line, shift=UP*0.15), run_time=0.9)
        self.wait(3)
        self.play(FadeOut(chess_line), run_time=0.6)

class Chess(MovingCameraScene):
    # dont forget the chess gameplay scene
    def construct(self):
        self.wait(0.5)
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1000, 120],
            axis_config={"include_tip": True},
            tips=False
        ).add_coordinates()

        labels = axes.get_axis_labels(x_label="Moves", y_label="Possibilities")

        def chessFunc(x):
            return x**3 if x <= 3 else (x-3)**4 + 27*(x-3) + 27

        graph = axes.plot(chessFunc, x_range=[0, 40], color=BLUE, stroke_width=6)
        slow_graph = axes.plot(chessFunc, x_range=[0, 3], color=BLUE, stroke_width=6)
        fast_graph = axes.plot(chessFunc, x_range=[3, 30], color=BLUE, stroke_width=6)

        dot = Dot(color=YELLOW)
        dot.move_to(graph.get_start())

        self.play(Create(axes), Write(labels), Write(graph), Create(dot))

        # auto_zoom in at the start to focus on the dot margin for how zoomed out it is
        self.wait(2.5)
        self.play(self.camera.auto_zoom(dot, margin=10, animate=True))

        # cairo regenerates every frame automatically so just add updater and move
        self.camera.frame.add_updater(lambda m: m.move_to(dot.get_center()))

        self.play(MoveAlongPath(dot, slow_graph), run_time=3.5, rate_func=linear)
        self.play(MoveAlongPath(dot, fast_graph), run_time=3.5, rate_func=rate_functions.ease_in_quad)

        # "once moves create freedom for other pieces, possibilities can grow at quite the speed"

        self.camera.frame.clear_updaters()
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set_width(config.frame_width),
            run_time=0.1
        )
        self.wait(2)

        # IMAGE OF CLAUDE SHANNON - on the right 
        shannon = ImageMobject("shannon.png")
        self.play(FadeIn(shannon.move_to([5, 0, 0])))
        self.wait(4)

        # brief pause as it grows, then fade in Shannons number
        # split into two parts: the base "10^", and the exponent "{120}"
        factNum = MathTex("10^{", "120", "}")
        factNum.scale(1.5)
        # manim treats each part as an item in an array:
        
        factNum[1].set_color(BLUE) 
        factNum.move_to(ORIGIN) 
        self.play(Write(factNum))
        self.play(factNum.animate.move_to([-2,0,0]), run_time=3.5)
        #self.play(FadeOut(factNum), run_time=0.1)
        comparison = MathTex(
            "10^{", "120", "}", # 0 = 10^, 1 = 120
            ">",
            "10^{", "80", "}"
        )
        comparison.scale(1.5)
        comparison.set_weight(BOLD)
        comparison.move_to([-1, 0, 0])
        comparison[1].set_color(BLUE)

        self.play(
            ReplacementTransform(factNum, comparison[:3]),  # transforms old number into the first 3 pieces
            Write(comparison[3:]),                          # writes the "> 10^80" parts dynamically in the same frame
            run_time=5
        )
        self.wait(3)

        ref = Tex(
        r"For Reference: $10^{120}$ = \\",
        r"1,000,000,000,000,000,000,000,000, \\",
        r"000,000,000,000,000,000,000,000, \\",
        r"000,000,000,000,000,000,000,000, \\",
        r"000,000,000,000,000,000,000,000, \\",
        r"000,000,000,000,000,000,000,000",
        font_size=28
        )

        box = SurroundingRectangle(ref, color=WHITE, buff=0.2, stroke_width=1.5)

        VGroup(ref, box).to_corner(DL, buff=0.3)

        self.play(Write(ref), Create(box))

        # indicate flash that lhs > rhs
        self.play(Indicate(comparison[1], color=BLUE, scale_factor=1.3, run_time=1))
        self.play(Indicate(comparison[5], color=RED, scale_factor=0.7, run_time=1))

        # fun fact (after posted video: I realized FadeIn would've looked cooler)
        shannonFact = Text("* Fun Fact: Claude AI is named after  Claude  Shannon *", color="#D16908", font_size=16, weight=BOLD)
        shannonFact.move_to(UP*1.5)
        self.play(Indicate(shannonFact))

        '''
        so if even every atom in the universe was itself a universe,
        you still dont have enough atoms to reperesent every chess game. crazy fact
        '''

        self.wait(4.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        n = Tex("nothing", font_size=68)
        self.play(FadeIn(n))
        self.wait(2.5)
        self.play(FadeOut(n))

        # but again, still 'nothing' compared to Grahams number

class Graham(ThreeDScene):
    def construct(self):
        #self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES) <- not needed anymore but for future ref
        '''
        phi and theta camera angle for manim
        phi represents vertical angle, tilts cam up or down
        theta represents horizontal, tilts cam left or right 
        '''

        digits = VGroup() # to hold all digits together so you can animate them all at once
        num_rings = 12 # real RAM killer
        intro = Text("Grahams Number")
        for ring in range(1, num_rings + 1):
            radius = ring * 0.6          # each ring is 0.6 further out
            circumference = 2 * PI * radius
            num_digits = int(circumference / 0.25)   # space dots evenly around ring

            for j in range(num_digits):
                angle = j * 2 * PI / num_digits
                x = radius * np.cos(angle) # [cos, sin] identity angle
                y = radius * np.sin(angle)

                n = Tex(
                str(np.random.randint(0, 9)),
                font_size=27,
                color=WHITE,
                )
                n.set_opacity(1)
                n.move_to([x, y, 0])
                digits.add(n)


        self.play(GrowFromCenter(digits, lag_ratio=0.002), run_time=6) # reason for that throwing spiral affect
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(2)
        self.stop_ambient_camera_rotation(about="theta") # stop camera turning 
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, run_time=1) # puts camera quickly back to proper angle
        self.play(ReplacementTransform(digits, intro))
        self.wait(2.5)
        self.play(FadeOut(intro))

        # transition master

        '''
        "Every one of these digits is part of a number so large, 
        you cant look at it as a number but only logic now
        " 
        '''

        self.camera.background_color = "#0A0A0A"
 
        def tex(*args, size=42, color=WHITE, **kwargs):
            m = MathTex(*args, font_size=size, color=color, **kwargs)
            m.set_stroke(BLACK, width=2, background=True)
            return m

        def txt(s, size=32, color=WHITE, **kwargs):
            m = Text(s, font_size=size, color=color, **kwargs)
            m.set_stroke(BLACK, width=1, background=True)
            return m

        '''
        to start, we have to learn a completely different notation
        ... but lets start simple
        '''
        
        expr1 = tex(r"3^3 = 3 \times 3 \times 3 = 27", size=52)
        expr1.move_to(ORIGIN)
        self.play(Write(expr1), run_time=2.5)
        self.wait(3)

        # single arrow is regular exponentation
        expr1b = tex(r"3 \uparrow 3 = 27", size=56, color="#FFD700")
        expr1b.next_to(expr1, DOWN, buff=0.35)
        self.play(Write(expr1b), run_time=0.8)
        self.wait(3.5)
        self.play(Unwrite(VGroup(expr1, expr1b)))
        

        # 3↑↑3 
        # 'now what about two arrows?'
        # two arrows is tetration (repeated exponentation)

        self.wait(1.5)
        double = tex(r"3 \uparrow\uparrow 3", size=64, color="#FFD700")
        double.move_to(UP*0.8)
        self.play(Write(double), run_time=0.8)
        self.wait(5)

        eq2a = tex(r"= 3^{3^3}", size=52)
        eq2a.next_to(double, DOWN, buff=0.4)
        self.play(FadeIn(eq2a, shift=UP*0.1))
        self.wait(2.5)

        eq2b = tex(r"= 3^{27}", size=52)
        eq2b.next_to(eq2a, DOWN, buff=0.3)
        self.play(FadeIn(eq2b, shift=UP*0.1))
        self.wait(0.5)

        eq2c = tex(r"= 7{,}625{,}597{,}484{,}987", size=44, color="#5CE08A")
        eq2c.next_to(eq2b, DOWN, buff=0.4)
        self.play(FadeIn(eq2c, shift=UP*0.1))
        self.wait(1.5)
        self.play(FadeOut(VGroup(double, eq2a, eq2b, eq2c)))

        # 3↑↑↑3 
        # triple arrow is pentation (repeated tetration)
        # the fundamental rule for resolving a triple arrow is that it chains together double arrows, not single arrows
        # now it becomes unfathomable

        '''
        Even if every single atom in the universe was turned into a pen
        that could write a digit per second, the universe would end before
        you finished writing down the number of digits in 3 arrow arrow arrow 3
        '''

        triple = tex(r"3 \uparrow\uparrow\uparrow 3", size=64, color="#FFD700")
        triple.move_to(UP*0.8)
        self.play(Write(triple), run_time=0.8)
        self.wait(4)

        eq3a = tex(r"= 3 \uparrow\uparrow (3 \uparrow\uparrow 3)", size=44)
        eq3a.next_to(triple, DOWN, buff=0.4)
        self.play(FadeIn(eq3a, shift=UP*0.1))
        self.wait(2.4)

        eq3b = tex(r"= 3 \uparrow\uparrow\ 7{,}625{,}597{,}484{,}987", size=40)
        eq3b.next_to(eq3a, DOWN, buff=0.3)
        self.play(FadeIn(eq3b, shift=UP*0.1))
        self.wait(12)

        # a tower of 3's 7.6 trillion levels tall
        eq3c = MathTex(
        r"A \uparrow\uparrow\uparrow B = A \uparrow\uparrow (A \uparrow\uparrow (\dots \text{ repeated } B \text{ times}))"
        )
        eq3c.next_to(eq3b, DOWN, buff=0.3)
        self.play(FadeIn(eq3c, shift=UP*0.1))
        self.wait(5.0)

        self.play(FadeOut(VGroup(triple, eq3a, eq3b, eq3c)))

        # 3↑↑↑↑3 = G1 
        # four arrows. This is the start of getting TO grahams number

        four = tex(r"3 \uparrow\uparrow\uparrow\uparrow 3", size=64, color="#FFD700")
        four.move_to(UP*0.5)
        self.play(Write(four), run_time=0.8)
        self.wait(5)

        eq4 = tex(r"= 3 \uparrow\uparrow\uparrow (3 \uparrow\uparrow\uparrow 3)", size=40)
        eq4.next_to(four, DOWN, buff=0.4)
        self.play(FadeIn(eq4, shift=UP*0.1))
        self.wait(0.5)

        g1_lbl = txt("We call this  G1.", size=34, color="#5C9EE0", weight=BOLD)
        g1_lbl.next_to(eq4, DOWN, buff=0.45)
        self.play(FadeIn(g1_lbl, shift=UP*0.1))

        self.wait(6)
        self.play(FadeOut(VGroup(four, eq4, g1_lbl)))

        # NumberPhile Analogy
        self.wait(0.6)

        # node positions (matched to reference image)
        pts = [
            UP * 1.8 + LEFT * 0.5,    # 0 top-left
            UP * 1.8 + RIGHT * 0.5,   # 1 top-right
            UP * 0.9 + LEFT * 2.0,    # 2 upper-left
            UP * 0.9 + RIGHT * 2.0,   # 3 upper-right
            ORIGIN + LEFT * 1.3,      # 4 mid-left
            ORIGIN + RIGHT * 1.3,     # 5 mid-right
            DOWN * 0.9 + LEFT * 2.2,  # 6 lower-left
            DOWN * 0.9 + RIGHT * 2.8, # 7 lower-right (wide)
            DOWN * 2.0 + LEFT * 0.8,  # 8 bottom-left
            DOWN * 2.0 + RIGHT * 0.8, # 9 bottom-right
        ]
 
        # dots
        dots = VGroup(*[
            Dot(point=p, radius=0.12, color=WHITE)
            for p in pts
        ])
 
        self.play(
            LaggedStart(
                *[GrowFromCenter(d) for d in dots],
                lag_ratio=0.12
            ),
            run_time=1.4
        )
        self.wait(0.3)
 
        # edges
        edges = VGroup()
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                edge = Line(
                    pts[i], pts[j], # so from other dot created go to the next one
                    stroke_width=1.2,
                    stroke_color=WHITE,
                    stroke_opacity=0.85, # very fun sliding window sort of leetcode problem
                    # have all the dots connect to the one up next 
                )
                edges.add(edge)
 
        self.play(
            LaggedStart(
                *[Create(e) for e in edges],
                lag_ratio=0.04
            ),
            run_time=5.5
        )
 
        # bring dots to front so they sit on top of edges
        self.bring_to_front(dots)
 
        self.wait(2)

        hypercube_fact = Tex("* Actual Math Problem Involved Hypercubes *", font_size=30)
        hypercube_fact.move_to([0, -3, 0])
        self.play(FadeIn(hypercube_fact))

        self.wait(2)
        
        self.play(FadeOut(dots, edges, hypercube_fact))

        self.wait(0.5)

        # another quote
        quote = Tex(' "Complete Disorder Is Impossible" ', font_size=45)
        credits = Tex("- Theodore Motzkin", font_size=30)

        credits.next_to(quote, ([0, -1, 0]), buff=0.3)
        credits.align_to(quote, LEFT)
        self.play(FadeIn(quote)) 
        self.wait(1.5)
        self.play(FadeIn(credits))

        self.wait(2)

        self.play(FadeOut(quote, credits))

        self.wait(1)

        analogy_lines = VGroup(
            txt("Imagine a Scenario where: "),
            txt("1. You have n people at a party", size=26, color="#DDDDDD"),
            txt("2. From those people, you form every possible subset", size=26, color="#DDDDDD"),
            txt("3. Then you form pairs within each subset.", size=26, color="#DDDDDD"),
            txt("4. Then color every pair, red or blue.", size=26, color="#DDDDDD", t2c={"red": RED, "blue": BLUE}),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        analogy_lines.move_to(UP*2)
        analogy_lines.center().shift(LEFT*0.5)

        for line in analogy_lines:
            self.play(FadeIn(line, shift=RIGHT*0.08), run_time=2.7)
        self.wait(1)
        self.play(FadeOut(VGroup(analogy_lines)))

        '''
        "How many people do you need to
        GUARANTEE that
        1. Every pair among those four subsets has the same color
        2. Every person appears in an even number of those four subsets",
        '''

        # ---------------------------------------------------------------------------------
        def create_subset(pos, num_people=4):

            circle = Circle(radius=0.9)

            positions = [
                UP*0.28 + LEFT*0.28,
                UP*0.28 + RIGHT*0.28,
                DOWN*0.28 + LEFT*0.28,
                DOWN*0.28 + RIGHT*0.28,
                ORIGIN,
            ]

            people = Group()

            for i in range(num_people):

                p = (
                    ImageMobject("stick.png")
                    .scale(0.12)
                    .move_to(circle.get_center() + positions[i])
                )

                people.add(p)

            group = Group(circle, people)
            group.move_to(pos)

            return group


        # main stick
        center_stick = (
            ImageMobject("stick.png")
            .scale(0.35)
            .move_to(ORIGIN)
        )

        self.play(Indicate(center_stick))

        offset = 3

        # subsets - it used to be committees but my english for some reason couldnt pronounce that word
        NE_pos = offset*RIGHT + offset*UP
        NW_pos = offset*LEFT + offset*UP
        SE_pos = offset*RIGHT + offset*DOWN
        SW_pos = offset*LEFT + offset*DOWN

        # arrows

        arrows = VGroup(

            Arrow(
                center_stick.get_corner(UR),
                NE_pos,
                buff=1,
                stroke_width=4,
            ),

            Arrow(
                center_stick.get_corner(UL),
                NW_pos,
                buff=1,
                stroke_width=4,
            ),

            Arrow(
                center_stick.get_corner(DR),
                SE_pos,
                buff=1,
                stroke_width=4,
            ),

            Arrow(
                center_stick.get_corner(DL),
                SW_pos,
                buff=1,
                stroke_width=4,
            ),
        )

        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.15
            )
        )

        NE = create_subset(NE_pos, 4)
        NW = create_subset(NW_pos, 4)
        SE = create_subset(SE_pos, 4)
        SW = create_subset(SW_pos, 4)

        committees = Group(NE, NW, SE, SW)

        self.play(
            LaggedStart(
                *[
                    Create(c[0])
                    for c in committees
                ],
                lag_ratio=0.12
            )
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(c[1])
                    for c in committees
                ],
                lag_ratio=0.12
            )
        )

        self.play(*[FadeOut(u) for u in arrows])
        self.play(FadeOut(center_stick))

        # same color pair

        links = VGroup()

        circles = [
            NE[0],
            NW[0],
            SE[0],
            SW[0],
        ]

        for i in range(4):

            for j in range(i+1, 4):

                line = Line(
                    circles[i].get_center(),
                    circles[j].get_center(),
                    color=RED,
                    stroke_width=5,
                )

                links.add(line)

        self.play(
            LaggedStart(
                *[
                    Create(l)
                    for l in links
                ],
                lag_ratio=0.05
            )
        )

        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])


        # DONE main animation
        
        # answer
        ans_top = txt("The answer:", size=30, color="#AAAAAA")
        ans_top.move_to(UP*1.5)
        self.play(FadeIn(ans_top))

        ans_range = VGroup(
            txt("Smallest possible:  6", size=32, color="#5CE08A"),
            txt("Largest possible:  Graham's Number", size=32, color="#E05C5C"),
        ).arrange(DOWN, buff=0.4)
        ans_range.next_to(ans_top, DOWN, buff=0.5)

        self.play(FadeIn(ans_range[0], shift=UP*0.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ans_range[1], shift=UP*0.1), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(ans_range, ans_top))

        # the real problem involves hypercubes, not people — but same idea.


        # G1 - G64 
        '''
        so how do we build Grahams number
        '''

        self.wait(1.5)

        g_layers = VGroup(
            tex(r"G_1 = 3 \uparrow\uparrow\uparrow\uparrow 3", size=36, color="#FFD700"),
            tex(r"G_2 = 3\ \underbrace{\uparrow \cdots \uparrow}_{G_1 \text{ arrows}}\ 3", size=36, color="#F5A623"),
            tex(r"G_3 = 3\ \underbrace{\uparrow \cdots \uparrow}_{G_2 \text{ arrows}}\ 3", size=36, color="#E05C5C"),
            tex(r"G_4 = 3\ \underbrace{\uparrow \cdots \uparrow}_{G_3 \text{ arrows}}\ 3", size=36, color="#C0392B"), #  i couldnt fix the underbrace, unsure why it was choppy
            tex(r"\vdots", size=48, color="#888888"),
            tex(r"G_{64} = \text{Graham's Number}", size=40, color="#5C9EE0"),
        ).arrange(DOWN, buff=0.32)
        g_layers.move_to(UP*0.25)

        for layer in g_layers:
            self.play(FadeIn(layer, shift=UP*0.08), run_time=0.4)
            self.wait(2.7)

        self.wait(0.5)

        # highlight G64
        box = SurroundingRectangle(g_layers[-1], color="#FFD700", buff=0.15, stroke_width=2)
        self.play(Create(box))
        self.wait(11.5)
        self.play(FadeOut(VGroup(g_layers, box)))
        self.wait(0.5)

        # SAY 'G64. 64 layers of incomprehensible arrows.
        # A number that exists only as logic.'
