import turtle as t

t.setup(width=1600,height=1200) # resolution
t.setworldcoordinates(0,1080,1440,0) # (0,0) at top-left
t.hideturtle()
t.pensize(5)
#t.delay(0) # Uncomment this line if you want fast drawing

#def draw_section(x, y, width, ):
#    pass

def class_diagram(x, y, name, attributes, methods):
    # Variables
    box_width = 0
    padding = 15
    font_size = 30
    font_height = font_size * 1.4

    # Class title box
    title_box_bottom = y + padding + font_height

    # Attributes box
    attr_num = len(attributes) # number of attributes on the box
    attr_box_top = title_box_bottom
    # The height based on the n# of attributes
    attr_box_bottom = attr_box_top + attr_num * (font_height + padding)

    # Methods box
    meth_num = len(methods)
    meth_box_top = attr_box_bottom
    meth_box_bottom = meth_box_top + meth_num * (font_height + padding)

    # calculing box width
    for atr in attributes:
        if len(atr) > box_width:
            box_width = len(atr) * font_size + padding

    # Set up
    t.penup()
    t.teleport(x,y)
    
    # Draw the title class box ...
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.goto(x + box_width, y)
    t.goto(x + box_width, title_box_bottom)
    t.goto(x, title_box_bottom)
    t.goto(x, y)
    t.end_fill()

    # .. Then write the name of the class.
    t.teleport(x + (box_width / 2), title_box_bottom)
    t.write(name, align = 'center', font = ('serif', font_size, 'bold'))

    # Draw the attributes box ...
    t.teleport(x, attr_box_top)
    t.goto(x, attr_box_bottom)
    t.goto(x + box_width, attr_box_bottom)
    t.goto(x + box_width, attr_box_top)

    # ... Then write the attributes & types.
    for i,attr in enumerate(attributes):
        t.teleport(x + padding, attr_box_top + (i + 1) * (font_height + padding))
        t.write(attr, font = ('serif', font_size, 'normal'))
    
    # Draw the methods box ...
    t.teleport(x, meth_box_top)
    t.goto(x, meth_box_bottom)
    t.goto(x + box_width, meth_box_bottom)
    t.goto(x + box_width, meth_box_top)
    
    # ... Then write the methods.
    for i,meth in enumerate(methods):
        t.teleport(x + padding, meth_box_top + (i + 1) * (font_height + padding))
        t.write(meth, font = ('serif', font_size, 'normal'))


# Careful when choosing the coordinates or else i'll overwrite other diagrams
class_diagram(0, 50, "Car", ["+Brand: string", "+Name: string", "+Model: string", "+Color: String"], ["honk(time: int)"])
class_diagram(500, 50, "Pet", ["+Name: string", "+Race: string", "+Age: int", "+Fur: string"], ["bark()", "sleep(time: int)", "eat()", "poo()"])
class_diagram( 1000, 50, "Microwave", ["+Brand: string", "+Name: string", "+Model: int", "+Power Rating: string"], ["turnOn()", "turnOff()"])
t.mainloop()