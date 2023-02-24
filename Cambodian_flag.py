from turtle import *
from pyautogui import*

back(180)
fd(360);
write('')
left(90);
forward(180);
write('')
left(90);
forward(180*2);
write('');
left(90);
forward(180)
write('')

#color of flag
write('')
def draw_rectangle(linecolor, length1=100, length2=150):
    color(linecolor)
    for i in range(2):
        back(45)
        left(90)
        fd(360);
        left(90);
begin_fill()
draw_rectangle('blue')
end_fill();
color('black')
#bow
back(135);
def draw_rectangle(linecolor, length1=100, length2=150):
    color(linecolor)
    for i in range(2):
        back(45)
        left(90)
        fd(360);
        left(90);
begin_fill()
draw_rectangle('blue')
end_fill();
color('black')

'''
#temple
'''
#red color of flag

def draw_rectangle(linecolor, length1=100, length2=150):
    color(linecolor)
    for i in range(2):
            fd(90);
            left(90);
            fd(360)
            left(90)
begin_fill();
draw_rectangle('red');
end_fill();

fd(90);
left(90);
color('blue')
fd(112.5)
color('black')
#temple

def draw_rectangle(linecolor, length1=100, length2=150):
    color(linecolor)
    for i in range(1):
            left(90)
            fd(10);
            #line1
            right(90);
            fd(10-1)
            #line2
            left(90)
            fd(10-2);
            #line3
            right(90);
            fd(10-3)
            #line4
            left(90)
            fd(10-4);
            #line5
            right(90);
            fd(10-5);
            #line6
            
            
            #top of temple
            
            left(75);
            fd(40)
            write('.')
            
            right(75*2)
            fd(40);
            
            left(75)
            fd(10)
            
            left(75);
            fd(68)
            #write('')
            right(75*2);
            fd(68)
            
            left(75)
            fd(10);
            
            left(75)
            fd(40)
            write('.')
            right(75*2);
            fd(40)
            
            left(75);
            fd(10-5);
            
            right(90);
            fd(10-4)
            
            left(90);
            fd(10-3);
            
            right(90);
            fd(10-2);
            
            left(90);
            fd(10-1);
            
            right(90);
            fd(10);
            
begin_fill();
draw_rectangle('white');
end_fill();
hideturtle();
color('blue')     
right(90);
fd(140)

color('black');


right(90)
fd(10);
#line1
right(90);
fd(10-1)
#line2
left(90)
fd(10-3);
#line3
right(90);
fd(10-3+0.5)
#line4
left(90)
fd(10-4);
#line5
right(90);
fd(10-5);
#line6


#top of temple
left(75);
fd(40)
write('.')

right(75*2)
fd(40);

left(75)
fd(10)

left(75);
fd(68)
write('')
right(75*2);
fd(68)

left(75)
fd(10);

left(75)
fd(40)
write('.')

right(75*2);
fd(40)

left(75);
fd(10-5);

right(90);
fd(10-4)

left(90);
fd(10-3);

right(90);
fd(10-2);

left(90);
fd(10-1);

right(90);
fd(10);

right(90);
fd(140)

###stair


right(90)
fd(10);
#line1
right(90);
fd(130)
#line2
left(90)
fd(10-1);
#line3
left(90);
fd(120)
#line4
right(180)
fd(10-3);
#line5
left(90);
fd(10-5);

right(90);
forward(109)
bgcolor('white');



exitonclick();










'''left(90);
fd(1)
color('white')
fd(44);
color('black');
right(90)
back(90)
fd(180)

left(110)
fd(90)
write('a')

left(135)
fd(60)
write('b')

right(135)
fd(90)
write('c')

left(135);
fd(90)
write('d')

right(135)
fd(60)
write('e')

left(139)
fd(97);
delay(10);
#hideturtle();

exitonclick();'''
