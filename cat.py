# cat_graphics
# require - PIL-1.1.7.win32-py2.7
# required module - cs1graphics
# compatable for python 2

from cs1graphics import*
import time
bura = Canvas(700,500)
bura.setBackgroundColor("skyBlue")
ear1=Polygon(Point(80,200),Point(100,30),Point(170,100))
ear1.setFillColor("orange")
ear1.setBorderColor("orange")
bura.add(ear1)

ear2=Polygon(Point(300,110),Point(380,30),Point(425,220))
ear2.setFillColor("orange")
ear2.setBorderColor("orange")
bura.add(ear2)

neck=Rectangle(140,100,Point(250,450))
neck.setFillColor("yellow")
bura.add(neck)

head=Circle(180,Point(250,250))
head.setBorderColor("yellow")
head.setFillColor("yellow")
bura.add(head)

eye1=Circle(44,Point(160,200))
eye1.setFillColor("white")
eye1.setBorderColor("black")
bura.add(eye1)
eye2=eye1.clone()
eye2.moveTo(310,200)
bura.add(eye2)

eyeb=Circle(10,Point(160,200))
eyeb.setFillColor("black")
bura.add(eyeb)
eyeb2=eyeb.clone()
eyeb2.moveTo(310,200)
bura.add(eyeb2)

covered=Circle(44,Point(160,200))
covered.setFillColor("orange")
covered.setBorderColor("black")

nose=Polygon(Point(210,280),Point(235,244),Point(260,280))
nose.setFillColor("orange")
nose.setBorderColor("orange")
bura.add(nose)

mouth=Layer()
moutha=Path(Point(235,295),Point(235,330),Point(230,335),Point(225,340),Point(220,342),Point(215,343),Point(210,344),Point(205,345),Point(195,345))
mouthb=Path(Point(235,330),Point(240,335),Point(245,340),Point(250,342),Point(255,343),Point(260,344),Point(265,345),Point(275,345))

mouthd=Polygon(Point(220,342),Point(235,330),Point(250,342))
mouthd.setFillColor("red")
mouth.add(moutha)
mouth.add(mouthb)

mouth.add(mouthd)
bura.add(mouth)

hair1=Path(Point(245,300),Point(345,300))
hair1.setBorderWidth(1)
hair2=hair1.clone()
hair2.moveTo(245,317)
hair3=hair1.clone()
hair3.moveTo(245,334)
hair4=hair1.clone()
hair4.moveTo(125,300)
hair5=hair1.clone()
hair1.moveTo(125,317)
hair6=hair1.clone()
hair6.moveTo(125,334)
bura.add(hair1)
bura.add(hair2)
bura.add(hair3)
bura.add(hair4)
bura.add(hair5)
bura.add(hair6)

hand=Layer()
arm=Rectangle(80,200,Point(450,640))
arm.setFillColor("yellow")
arm.setBorderColor("yellow")
arm.rotate(35)
palm=Circle(65,Point(500,585))
palm.setFillColor("orange")
thumb=Rectangle(30,60,Point(455,530))
thumb.setFillColor("yellow")
finger1=Rectangle(27,60,Point(475,545))
finger1.setFillColor("yellow")
finger1.rotate(35)
finger2=finger1.clone()
finger2.moveTo(505,565)
finger3=finger1.clone()
finger3.moveTo(535,585)
hand.add(arm)
hand.add(thumb)
hand.add(palm)
hand.add(finger1)
hand.add(finger2)
hand.add(finger3)
bura.add(hand)
dot=Path(Point(0,0),Point(2,0))
bura.add(dot)

for i in range (500):
    hand.move(0.2,-0.4)
for i in range (1000):
    dot.move(0.1,0)
bura.add(covered)
for i in range (600):
    dot.move(0.2,0)
bura.remove(covered)
