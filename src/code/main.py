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
for i in range(255):
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
    y = 0
    x = 0
    for i in range(len(colbytes)):
        if x == GRID_SIZE:
            y += bsize
            x = 0
        if y == GRID_SIZE:
            pass # implement scrolling here
        pg.draw.rect(screen, colbytes[i], (x*bsize,y,bsize,bsize))
        pg.display.flip()
        sleep(0.005)
        x += 1
clock = pg.time.Clock()
SIZE = 640
bsize = 16
GRID_SIZE = SIZE // bsize
screen = pg.display.set_mode((SIZE, SIZE))
screen.fill((255,255,255))
rain()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()