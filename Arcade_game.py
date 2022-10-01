'''Group members for this project are

1-Bealprasim Demere UGR/25540/14
2-Gelila Mihirke UGR/25683/14
3-Tesfalem Badeg UGR/25473/14
4-Saba Delelegn UGR/26849/14
5-Fatiya Jeylan UGR/26030/14   '''
"submitted to mr ______________ "

from cs1graphics import *
import time

from random import *
import threading

arcade = Canvas(1000, 700, "Black", "Group arcade")
#score = Text(" SCORE ", 20)

# Creating Habesh our very own creation
habesh = Layer()

face = Circle(10, Point(0,0))
face.setFillColor("Brown")
face.setDepth(-11)
hair = Circle(14, Point(0,-3))
hair.setFillColor('yellow')
hair.setDepth(-1)
eye1 = Ellipse(5,6, Point(-3,-3))
eye1.setFillColor('white')
eye1.setDepth(-13)
eye2 = Ellipse(5,6,Point(3,-3))
eye2.setFillColor('white')
eye2.setDepth(-13)

habesh.add(eye2)
habesh.add(eye1)
habesh.add(face)
habesh.add(hair)

body=Polygon(Point(0,8),Point(-20,8),Point(-20,26),Point(-10,24),Point(-7,40),Point(-15,42),Point(-15,45),Point(-2,45),Point(-2,24),Point(10,25),Point(13,40),Point(5,42),Point(5,45),Point(17,45),Point(17,24),Point(20,26),Point(20,8))
body.setFillColor("brown")

arm1 = Polygon(Point(-20,14),Point(-30,25),Point(-32,30),Point(-34,34),Point(-31,34),Point(-30,31),Point(-30,34),Point(-28,34),Point(-28,31),Point(-28,34),Point(-26,34),Point(-25,31),Point(-23,34),Point(-21,34),Point(-24,25),Point(-20,20))
arm1.setFillColor('grey')
arm1.setDepth(-12)

arm2 = Polygon(Point(20,14),Point(30,25),Point(32,30),Point(34,34),Point(31,34),Point(30,31),Point(30,34),Point(28,34),Point(28,31),Point(28,34),Point(26,34),Point(25,31),Point(23,34),Point(21,34),Point(28,25),Point(20,20))
arm2.setFillColor('green')
arm2.setDepth(-12)
habesh.add(arm1)
habesh.add(arm2)
habesh.add(body)
habesh.move(130,580)    #The Habesha man's layer is centered at (130,590)


# Creating The level's in the game graphics

levelmini= Path(Point(400,100),Point(600,110),Point(600,130),Point(400,120),Point(400,100))
levelmini.setBorderColor('red')
levelmini.setBorderWidth(3)

string = Path(Point(400,100),Point(420,119),Point(440,106),Point(460,120),Point(480,108),Point(500,125),Point(520,110),Point(540,125),Point(560,110),Point(580,125),Point(600,110))
string.setBorderColor('blue')
string.setBorderWidth(4)


#Creating the torch found at level mini
prize = Layer()
torch = Polygon(Point(-5,22),Point(5,22),Point(5,-12),Point(7,-12),Point(-7,-12),Point(-5,-12))
torch.setFillColor('grey')
torch.setDepth(-12)
prize.move(425,68)
prize.add(torch)
pp=0  #constant
for i in range(5):
    fire = Polygon(Point(7-pp,-10),Point(7-pp,-32),Point(3-pp,-10))
    #fire.setBorderWidth(4)
    fire.setFillColor('orange')
    prize.add(fire)
    pp+=3

arcade.add(prize)


level1 = Path(Point(0,200),Point(950,235),Point(940,250),Point(950,260),Point(0,220))
level1.setBorderColor('Red')
level1.setBorderWidth(3)

q=0        #constant distances
g=0        #to be added
for i in range(45):  #arrows
    pointers = Path(Point(15+q,205+g),Point(5+q,212+g),Point(15+q,215+g))#level 1
    pointers.setBorderColor('green')

    arcade.add(pointers)
    q+=20
    g+=0.75

level2 = Path(Point(1000,300),Point(30,320),Point(40,330),Point(30,340),Point(1000,320))
level2.setBorderColor('red')
level2.setBorderWidth(3)

x=0


level3 = Path(Point(0,370),Point(950,390),Point(940,400),Point(950,410),Point(0,390))
level3.setBorderColor('red')
level3.setBorderWidth(3)

a=0
b=0
for i in range(45):
    pointers1 = Path(Point(15+a,375+b),Point(5+a,382+b),Point(15+a,385+b))#level3
    pointers1.setBorderColor('orange')
    arcade.add(pointers1)
    a+=20
    b+=0.4

level4 = Path(Point(1000,440),Point(40,460),Point(50,470),Point(40,480),Point(1000,460))
level4.setBorderColor('red')
level4.setBorderWidth(3)

level5 = Path(Point(0,520),Point(950,540),Point(940,550),Point(950,560),Point(0,540))
level5.setBorderColor('red')
level5.setBorderWidth(3)

l=0
w=0
for i in range(45):
    pointy=Path(Point(15+l,525+w),Point(5+l,532+w),Point(15+l,535+w)) #level4
    pointy.setBorderColor('white')
    arcade.add(pointy)
    l+=20
    w+=0.4
level6 = Path(Point(0,630),Point(1000,610),Point(1000,630),Point(0,650))
level6.setBorderColor('red')
level6.setBorderWidth(3)

#Creating the ladders

ladder = Path(Point(400,217),Point(400,0),Point(370,0),Point(370,218)) #escape ladder  x=30 y=217
ladder.setBorderColor('yellow')
ladder.setBorderWidth(3)

t=0
for i in range(16):   #steps for escape ladder
    stepE=Rectangle(30,4,Point(385,217-t))
    stepE.setFillColor('sky blue')
    arcade.add(stepE)
    t+=14

ladder0 = Path(Point(550,222),Point(550,128),Point(580,127),Point(580,223)) #ladder between level 1 and the mini level x=30 y=94
ladder0.setBorderColor('yellow')
ladder0.setBorderWidth(3)

w=0
for i in range(5):   #steps for ladder 0
    stepr = Rectangle(30,4,Point(565,222-w))
    stepr.setFillColor('sky blue')
    arcade.add(stepr)
    w+=20

ladder2 = Polygon(Point(800,305),Point(800,254),Point(830,254),Point(830,305)) #ladder between level 1 and 2 x =30, y=51
ladder2.setBorderColor('yellow')
ladder2.setBorderWidth(3)

n=0
for i in range(6):             #steps for ladder 2
    step=Rectangle(30,4,Point(815,305-n))
    step.setFillColor('sky blue')
    arcade.add(step)
    n+=10
ladder3 = Path(Point(200,375),Point(200,337),Point(230,337),Point(230,375)) #ladder between level 2 and 3 x= 30, y=38
ladder3.setBorderColor('yellow')
ladder3.setBorderWidth(3)

x=0
for i in range(4):                          # steps for ladder3
    stepx=Rectangle(30,4,Point(215,375-x))
    stepx.setFillColor('sky blue')
    arcade.add(stepx)
    x+=10

ladder4 = Path(Point(800,442),Point(800,408),Point(830,408),Point(830,442)) #ladder between level 3 and 4 x=30, y=36
ladder4.setBorderColor('yellow')
ladder4.setBorderWidth(3)

y=0
for i in range(4):  # steps for ladder4
    step0=Rectangle(30,4,Point(815,442-y))
    step0.setFillColor('sky blue')
    arcade.add(step0)
    y+=10

ladder5 = Path(Point(150,522),Point(150,480),Point(180,480),Point(180,522)) #ladder between levels 4 and 5 x=30 y=42
ladder5.setBorderColor('yellow')
ladder5.setBorderWidth(3)

j=0
for i in range(5):   #steps for ladder 5
    stepd = Rectangle(30,4,Point(165,522-j))
    stepd.setFillColor('sky blue')
    arcade.add(stepd)
    j+=10



ladder6 = Path(Point(800,613),Point(800,558),Point(770,558),Point(770,613)) #ladder between level 5 and 6 x=30 y=55
ladder6.setBorderColor('yellow')
ladder6.setBorderWidth(3)

p=0
for i in range(5):     #Steps for ladder 6
    stepp = Rectangle(30,4,Point(785,602-p))
    stepp.setFillColor('sky blue')
    arcade.add(stepp)
    p+=11

arcade.add(ladder6)
arcade.add(ladder5)
arcade.add(ladder4)
arcade.add(ladder2)
arcade.add(ladder3)


# Building the snowman
snowman = Layer()

head = Ellipse(30,25,Point(0,5))
head.setFillColor('white')
head.setDepth(-2)
belly = Ellipse(50,30,Point(0,23))
belly.setFillColor('white')
nose = Path(Point(0,0),Point(-1,1),Point(1,2))
nose.setBorderColor('orange')
nose.setBorderWidth(6)
nose.setDepth(-3)

#creating Snow in Bulk
n=0
for i in range(5):
    y=156+n
    snow=Circle(7,Point(50,y))
    snow.setFillColor('white')
    snow.setDepth(-16)
    arcade.add(snow)
    n+=10
    p=0
    for j in range(5):
        snow=Circle(7,Point(50+p,y-0.7))
        snow.setFillColor('white')
        snow.setDepth(-16)
        arcade.add(snow)
        p+=10

stick1 = Path(Point(-25,25),Point(-35,35))
stick1.setBorderColor('brown')
stick1.setBorderWidth(3)
stick1ext=Path(Point(-35,35),Point(-40,45))
stick1ext.setBorderColor('brown')
stick1ext.setBorderWidth(3)
snowman.add(stick1ext)

for i in range(100):
    stick1ext.rotate(45)
    stick1ext.rotate(-45)



stick2=Path(Point(25,25),Point(35,35))
stick2.setBorderColor('brown')
stick2.setBorderWidth(3)
stick2ext = Path(Point(35,35),Point(40,45))
stick2ext.setBorderColor('brown')
stick2ext.setBorderWidth(3)
snowman.add(stick2ext)

for i in range(100):
    stick2ext.rotate(45)
    stick2ext.rotate(-45)

#remaining life indicators

life1 = habesh.clone()
life1.moveTo(800,15)
life1.scale(0.7)

life2 = habesh.clone()
life2.moveTo(830,15)
life2.scale(0.7)

life3 = habesh.clone()
life3.moveTo(870,15)
life3.scale(0.7)

arcade.add(life3)
arcade.add(life2)
arcade.add(life1)
snowman.add(stick2)
snowman.add(stick1)
snowman.add(nose)
snowman.add(belly)
snowman.add(head)
snowman.moveTo(70,120)   #coordinates for the snow man

arcade.add(ladder0)
arcade.add(snowman)
arcade.add(ladder)
arcade.add(level6)
arcade.add(level5)
arcade.add(level4)
arcade.add(level3)
arcade.add(string)
arcade.add(levelmini)
arcade.add(level2)
arcade.add(level1)
arcade.add(habesh)

#snowballs
snowball = Circle(15,Point(69,185))
snowball.setDepth(-15)
snowball.setFillColor("white")
arcade.add(snowball)

snowfrenzy= Circle(15,Point(69,185))
snowfrenzy.setDepth(-15)
snowfrenzy.setFillColor('white')
arcade.add(snowfrenzy)
'''
#Displayed numbers

one = Layer()
ande=Polygon(Point(-20,-15),Point(15,-15),Point(15,-11),Point(10,-11),Point(10,-13),Point(-15,-13),Point(-15,-11),Point(-20,-11),Point(-20,-15))
ande.setFillColor('green')
ande.setDepth(-12)
zeng=Path(Point(0,-8),Point(-12,-7),Point(-10,7),Point(-5,11),Point(-2,6),Point(-5,1),Point(-10,7))
zeng.setBorderWidth(5)
zeng.setBorderColor('yellow')
one.add(zeng)
one.add(ande)
arcade.add(one)
one.moveTo(600,20)
'''

#Habesh and snowball movement animation control

def anime():
    c=0
    while c<8:
        if c==0:
        #leg1.flip()
            body.flip()
            for i in range(648):
                #arm1.rotate(45)
                #time.sleep()
                #arm1.rotate(-45)
                #arm2.rotate(45)
                #time.sleep(0.2)
                #arm2.rotate(-45)
                habesh.move(1,-0.005)
                #snowball.move(0.8,0.05)
                continue

        if c==1:
            face.flip()
            hair.setDepth(-14)
            for i in range(270):
                habesh.move(0,-0.3)
                #snowball.move(0.7,0.008)
                #snowball.move(0.7,0.008)
        #leg1.flip()
        #leg2.flip()
            body.flip()
            hair.setDepth(-3)
            for i in range(615):
                habesh.move(-1,-0.003)
               # snowball.move(-0.01,0.13)
                continue
        if c==2:
            hair.setDepth(-14)
            for i in range(350):
                habesh.move(0,-0.2)
                #snowball.move(-1.1,-0.003)
                #snowball.move(-1,-0.005)
            hair.setDepth(2)
        #leg2.flip()
        #leg1.flip()
            body.flip()
            for i in range(720):
                habesh.move(1,-0.04)
                if i ==228:
                   #habesh.flip(180)
                    habesh.rotate(45)
                    #snowball.setRadius(0.2)
                    for i in range(10):
                        habesh.move(-6,-2)
                        time.sleep(0.4)
                    habesh.rotate(-45)
                    arcade.remove(life2)
                    for i in range(10):
                        habesh.move(0,2)
                        time.sleep(0.03)
                    for i in range(10):
                        habesh.move(-1,0.01)

               # if i%4==0:
                #    snowball.move(0.003,0.34)
                continue
        if c==3:
            for i in range(250):
                hair.setDepth(-14)
                habesh.move(0,-0.2)
              #  snowball.move(1.1,0.1)
                #snowball.move(1.3,0.04)
            body.flip()
            hair.setDepth(1)
        #leg2.flip()
        #leg1.flip()
        if c==4:
            for i in range(600):
                habesh.move(-1,-0.02)
            for i in range(300):
                hair.setDepth(-14)
                habesh.move(0,-0.2)
                snowfrenzy.move(0.9,0.04)
                continue
        #leg2.flip()
        #leg1.flip()
            hair.setDepth(1)
            body.flip()
        if c==5:
            for i in range(600):
                habesh.move(1,-0.02)
                snowfrenzy.move(0.5,0.04)
            for i in range(332):
                hair.setDepth(-14)
                habesh.move(0,-0.2)
                snowfrenzy.move(0.45,0.03)
                if i==330:
                    snowfrenzy.setRadius(0.0002)
                    hair.setDepth(1)
                    habesh.flip()
                    for i in range(10):
                        habesh.move(4,-3)
                        time.sleep(0.1)
                    for i in range(10):
                        habesh.move(0,3)
                        time.sleep(0.1)
                    arcade.remove(life3)
                    for i in range(10):
                        habesh.move(1,0.009)
        #leg1.flip()
        #leg2.flip()
            hair.setDepth(1)
        if c==6:
            for i in range(300):
                habesh.move(-1,-0.03)
            for i in range(320):
                hair.setDepth(-14)
                habesh.move(0,-0.4)
                continue
            hair.setDepth(1)
            for i in range(110):
                habesh.move(-1,-0.0002)
            for i in range(170):
                prize.move(-1.9,0.5)
                time.sleep(0.005)
        if c==7:
            arcade.remove(snowman)
            for i in range(70):
                habesh.move(-1,0.02)
            for i in range(100):
                habesh.move(0.09,-1)        

        c+=1
def body_movement():
    for i in range(200):
        arm1.rotate(15)
        time.sleep(0.1)
        arm1.rotate(-15)
        time.sleep(0.1)
        arm2.rotate(15)
        time.sleep(0.1)
        arm2.rotate(-15)

def snowball_roll():
    count=0
    while count<7:
        if count==0:
            for i in range(620):
                snowball.move(1.5,0.06)
        if count==1:
            for i in range(90):
                snowball.move(-0.7,0.7)
            for i in range(510):
                snowball.move(-1.4,0.07)
        if count==2:
            for i in range(50):
                snowball.move(0,1)
            for i in range(370):
                snowball.move(2.1,0.009)
        if count==3:
            for i in range(90):
                snowball.move(-0.7,0.7)
            for i in range(541):
                snowball.move(-1.4,0.008)
                #snowfrenzy.move(1,0.05)
                if i==520:
                    snowball.setRadius(0.001)
        count+=1


thread1 = threading.Thread(target=anime)
thread2 = threading.Thread(target=body_movement)
thread3 = threading.Thread(target=snowball_roll)
thread1.start()
time.sleep(0.1)
thread3.start()
time.sleep(0.2)
thread2.start()
thread1.join()
thread3.join()
thread2.join()


