import turtle

screen = turtle.Screen()
alex = turtle.Turtle()

def generate(pattern, iteration):
    print("The initial pattern is", pattern)
    for i in range(iteration):
        pattern = pattern.replace("F", pattern)
        print("iteration", i+ 1, ":", pattern)

    return pattern
def draw(pattern, drawlength, angle):
    for i in pattern:
        if i == "F":
            #forward
            alex.forward(drawlength)
        elif i == "f":
            alex.penup()
            alex.forward(drawlength)
            alex.pendown()
        elif i == "+":
            #turn left
            alex.right(angle)
            alex.forward(drawlength)
        elif i == "-":
            #turn right
            alex.left(-angle)
            alex.forward(drawlength)

alex.penup()
alex.goto(0,0)
alex.pendown()


initialpattern = "F++F--" ; angle = 135
#initialpattern = "F++F--" ; angle = 45
#initialpattern = "F+F--" ang = 90 deg
#initialpattern = "F+F--" angle = 45 deg
#initialpattern = "F+F--"  angle = 43 deg
#initialpattern = "F+-f+F" Flower:)
#initialpattern = "F+F-f"
pattern = generate(initialpattern, 3)
draw(pattern, 10, angle)

# pattern = generate("F+F-f", 1)
# draw(pattern, 30, 120)
#
# pattern = generate("F+F-f", 2)
# draw(pattern, 40, 100)
#
# pattern = generate("F+F-f", 2)
# draw(pattern, 50, 80)
#
# pattern = generate("F+F-f", 2)
# draw(pattern, 60, 60)


screen.mainloop()