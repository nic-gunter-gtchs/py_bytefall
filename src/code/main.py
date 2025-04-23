import pygame as pg
import sys
from time import sleep
print("py_bytefall by Nic Gunter")
source = input("Input file (including full path): ")
with open(source, "rb") as s:
    data = s.read()
    hbytes = data.hex()
hold = []
bytelist = []
for i in range(len(hbytes)):
    if i % 2 == 0:
        hold.append(hbytes[i])
    else:
        bytelist.append(''.join([hold[0],hbytes[i]]))
        hold.clear()
print(bytelist) # debug
r = 0 # red value
g = 0 # green value
b = 0 # blue value
colref = {}
for i in range(256):
    colref[i] = (r,g,b)
    r += 1
    g += 1
    b += 1
colbytes = []
for i in bytelist:
    colbytes.append(colref[int(i,16)])
print(colbytes) # debug
pg.init()
def rain():
    global scrol, x, y, tuplist, rectlist
    for hi in range(len(colbytes)):
        if x == GRID_SIZE:
            y += bsize
            x = 0
            pg.display.flip()
            sleep(delay/1000)
        if y >= SIZE:
            rec = len(rectlist)
            screen.fill((255, 255, 255))
            for re in range(rec):
                tuplist = rectlist[0]
                if tuplist[1] == 0:
                    del rectlist[0]
                else:
                    pg.draw.rect(screen, tuplist[2], (tuplist[0], tuplist[1] - bsize, bsize, bsize))
                    rectlist.append([tuplist[0], tuplist[1] - bsize, tuplist[2]])
                    del rectlist[0]
            y -= bsize
        pg.draw.rect(screen, colbytes[hi], (x * bsize, y, bsize, bsize))
        rectlist.append([x * bsize, y, colbytes[hi]])
        x += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
rectlist =[]
tuplist = []
SIZE = 640
scrol = 640
bsize = 16
y = 0
x = 0
delay = 0.5
GRID_SIZE = SIZE // bsize
screen = pg.display.set_mode((SIZE, SIZE))
screen.fill((255,255,255))
bytelist.clear()
colref.clear()
rain()