from cs1graphics import *
import time

c = Canvas(500,500,'black',"Bersa's canvas")

#################################################creating the trees

tree = Layer()
branches = Polygon(Point(0,-35),Point(-15,-20),Point(-10,-20),Point(-15,-5),Point(-10,-5),Point(-15,10),Point(15,10),Point(10,-5),Point(15,-5),Point(10,-20),Point(15,-20))
branches.setFillColor('green')
tree.add(branches)
tree.move(50,70)
tree.setDepth(-10)
stem = Polygon(Point(-5,10),Point(-5,30),Point(5,30),Point(5,10))
stem.setFillColor('brown')
tree.add(stem)

###################################################################cloning trees

tree1 = tree.clone()
tree1.moveTo(100,120)
tree1.scale(1.4)

tree_clone = tree.clone()
tree_clone.moveTo(120,220)
tree_clone.scale(1.6)

fourth_tree = tree.clone()
fourth_tree.moveTo(50,300)
fourth_tree.scale(1.7)

c.add(fourth_tree)
x = 300
for i in range(4):
    if i==0:
        tree_on_the_otherside = tree.clone()
        tree_on_the_otherside.moveTo(100+x,70)
        c.add(tree_on_the_otherside)
        x-=50
    if i==1:
        tree_on_the_otherside = tree1.clone()
        tree_on_the_otherside.moveTo(100+x,120)
        c.add(tree_on_the_otherside)
        x-=40
    if i==2:
        tree_on_the_otherside = tree_clone.clone()
        tree_on_the_otherside.moveTo(120+x,220)
        c.add(tree_on_the_otherside)
        x+=140
    if i==3:
        tree_on_the_otherside = fourth_tree.clone()
        tree_on_the_otherside.moveTo(50+x,300)
        c.add(tree_on_the_otherside)

ground = Polygon(Point(0,90),Point(500,90),Point(500,500),Point(0,500))
ground.setFillColor('dark green')

#################################################################creating stars

star = Polygon(Point(80,40),Point(100,60),Point(100,30),Point(75,60),Point(110,40),Point(80,40))
star.setFillColor('white')
c.add(star)

n=0
m=10
for i in range(20):
    if i%2==0:
        star_new=star.clone()
        star_new.moveTo(140-n,40-m)
        star_new.scale(0.5)
        c.add(star_new)
        m+=5
        n+=40
    if i%2!=0:
        star_new=star.clone()
        star_new.moveTo(80+n,30+m)
        star_new.scale(0.6)
        c.add(star_new)
        m-=10

c.add(ground)
#####################################################house Build

home = Layer()

ground_floor = Rectangle(80,50,Point(0,0))
ground_floor.setFillColor('grey')
ground_floor.setDepth(-40)

door = Rectangle(30,30,Point(20,10))
door.setFillColor('white')
door.setDepth(-44)

first_floor = Square(50,Point(15,-50))
first_floor.setFillColor('grey')
first_floor.setDepth(-40)
home.add(first_floor)
home.add(door)
home.add(ground_floor)
home.move(430,200)
c.add(home)

#########################################fence creation########

fence = Rectangle(5,60,Point(65,490))
fence.setFillColor('grey')
fence.setDepth(-20)
c.add(fence)

j = 30
k = 10
for i in range(13):
    fence_clone = fence.clone()
    fence_clone.moveTo(63+k,490-j)
    c.add(fence_clone)
    j+=30
    k+=10

fence2 = Rectangle(5,60,Point(400,490))
fence2.setFillColor('purple')
fence2.setDepth(-20)

o=10
p=30
for i in range(13):
    fence2_clone=fence2.clone()
    fence2_clone.moveTo(390-o,490-p)
    c.add(fence2_clone)
    o+=10
    p+=30
########################################## PATH for a RIVER
river_path = Polygon(Point(76,500),Point(215,90),Point(240,90),Point(370,500))
river_path.setFillColor('sky blue')
c.add(river_path)
###################################### Boat and animation

boat = Layer()
body = Polygon(Point(-5,-25),Point(-18,-5),Point(-18,5),Point(-5,25),Point(5,25),Point(18,5),Point(18,-5),Point(5,-25),Point(-5,-25))
body.setFillColor('brown')
body.setDepth(-10)
boat.add(body)
boat.moveTo(225,100)
flag = Polygon(Point(0,-10),Point(0,-40),Point(10,-40),Point(10,-30),Point(0,-30))
flag.setFillColor('white')
flag.setDepth(-60)
boat.add(flag)
c.add(boat)
c.add(fence2)
c.add(tree_clone)
c.add(tree1)
c.add(tree)

for i in range(310):
    boat.move(0.1,1.4)
    time.sleep(0.08)
    if i==100:
        boat.scale(1.2)
    if i==150:
        boat.scale(1.3)
