import turtle as t

t.setup(width=1800,height=1000, startx=0, starty=0) # resolution
t.setworldcoordinates(0,1000,1800,0) # (0,0) coordinates at top-left
t.hideturtle()
t.pensize(5)
t.delay(0) # Uncomment this line if you want fast drawing

# VARIABLES CONSTANTES
PADDING = 15 # Relleno
FONT_SIZE = 30

def class_diagram(x, y, name, attributes, methods):
    # Calcular el ancho del cuadro
    box_width = 0
    for atr in attributes:
        if len(atr) > box_width:
            box_width = len(atr) * FONT_SIZE + PADDING

    # Variables
    text_height = PADDING + FONT_SIZE * 1.4 # Altura de cada texto

    # Class title box (altura)
    title_box_bottom = y + text_height

    # Attributes box (altura)
    attr_num = len(attributes) # number of attributes on the box
    attr_box_top = title_box_bottom
    attr_box_bottom = attr_box_top + attr_num * (text_height)

    # Methods box (altura)
    meth_num = len(methods)
    meth_box_top = attr_box_bottom
    meth_box_bottom = meth_box_top + (meth_num * text_height)

    # Configuración inicial
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
    t.write(name, align = 'center', font = ('serif', FONT_SIZE, 'bold'))

    # Draw the attributes box ...
    t.teleport(x, attr_box_top)
    t.goto(x, attr_box_bottom)
    t.goto(x + box_width, attr_box_bottom)
    t.goto(x + box_width, attr_box_top)

    # ... Then write the attributes & types.
    for i,attr in enumerate(attributes):
        # Spacing between attribute
        extra_attr = (i + 1) * text_height - PADDING/2 
        t.teleport(x + PADDING, attr_box_top + extra_attr)
        t.write(attr, font = ('serif', FONT_SIZE, 'normal'))
    
    # Draw the methods box ...
    t.teleport(x, meth_box_top)
    t.goto(x, meth_box_bottom)
    t.goto(x + box_width, meth_box_bottom)
    t.goto(x + box_width, meth_box_top)
    
    # ... Then write the methods.
    for i,meth in enumerate(methods):
        # Spacing between methods
        extra_meth = (i + 1) * text_height - PADDING/2 
        t.teleport(x + PADDING, meth_box_top + extra_meth)
        t.write(meth, font = ('serif', FONT_SIZE, 'normal'))

# Cuidado a la hora de elegir las coordenadas iniciales de cada diagrama de clase.
# Recomendadación con valores predeterminados: x: 500, y: 60, por cada texto
class_diagram(0, 0, "Car", ["+brand: string", "+name: string", "+model: string", "+color: string"], ["honk(time: int)"])
class_diagram(500, 0, "Pet", ["+name: string", "+race: string", "+age: int", "+fur: string"], ["bark()", "sleep(time: int)", "eat()", "poo()"])
class_diagram( 1000, 0, "Microwave", ["+brand: string", "+name: string", "+model: int", "+power rating: string"], ["turnOn()", "turnOff()"])
t.mainloop()