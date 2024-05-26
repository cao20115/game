import pgzrun
import time

WIDTH = 600
HEIGHT = 400

a = Actor("n")
hp = 10000
b = Actor("boss")
hp2 = 100000
a.pos = (300, 200)
b.pos = (100, 100)
flag = False
bj = 5
s = 10
up = 0


def draw():
    global hp
    global flag
    screen.fill((255, 255, 255))
    screen.blit("a", (0, 0))
    if flag:
        screen.draw.text("Boss: " + str(hp2), (300, 30), color="yellow")
        screen.draw.text("rampage!!!", (300, 60), color = "red")
    else:
        screen.draw.text("Boss: " + str(hp2), (300, 30), color="blue")
    screen.draw.text("HP: " + str(hp), (30, 30), color="red")
    a.draw()
    b.draw()

    
def on_key_down(key):
    global hp2
    global hp
    if key == keys.SPACE:
        if a.colliderect(b):
            hp2 -= 9999
            print("一刀999!")
        else:
            if hp <= 8000:
                hp += 2000
            else:
                hp = 10000


def update():
    global flag
    global hp
    global hp2
    global bj
    global s
    global up
    b.angle = b.angle_to(a)
    animate(b, tween="decelerate", duration=s, pos=a.pos)
    if hp + 1 <= 10000:
        hp += 1
    if flag:
        if hp2 < 1000000:
            hp2 += 1
    if hp2 <= 2000 and flag == False:
        b.image = "boss2"
        bj = 10
        s = 4
        hp2 = 1000000
        flag = True
    if a.colliderect(b):
        hp -= bj
    if keyboard[keys.UP]:
        a.y -= 3;
        print("w")
    if keyboard[keys.DOWN]:
        a.y += 3;
        print("s")
    if keyboard[keys.LEFT]:
        a.x -= 3;
        a.image = "n"
        print("a")
    if keyboard[keys.RIGHT]:
        a.x += 3
        a.image = "n2"
        print("d")
    if a.y < 0:
        a.y = HEIGHT
    elif a.y > HEIGHT:
        a.y = 0
    elif a.x < 0:
        a.x = WIDTH
    elif a.x > WIDTH:
        a.x = 0
    if hp <= 0:
        for i in range(10086):
            print("\n")
        print("You are DIE")
        print("Try again!")
        exit()
    if hp2 <= 0:
        for i in range(10086):
            print("\n")
        print("       Great!")
        print("You are the winner!!!")
        exit()


pgzrun.go()

time.sleep(1)
