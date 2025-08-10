import pygame as pg
import sys
from collections import deque
print("py_bytefall by Nic Gunter")
source = input("Input file (including full path): ")
delay = float(input("Delay between lines of rain (ms, higher values = slower): "))
bsize = int(input("What size should the grid be? "))
with open(source, "rb") as s:
    hbytes = s.read().hex() # unnecessary variable removed, conversion now handled in one line
bytelist = []
for i in range(0, len(hbytes), 2): # I don't know what the heck was going on here before, this is much faster and more readable
    pair = hbytes[i:i+2] # slicing internally runs in C, makes a large improvement
    bytelist.append(pair)
colbytes = []
for hexstr in bytelist:
    val = int(hexstr, 16) #why did I use 3 vars for this?? idk, also who knows why I made a LUT for 0-255 :sob: now it just directly converts the hexbyte to decimal
    colbytes.append((val, val, val)) # it's grayscale, only one value needed
pg.init()
SIZE = 640
GRID_SIZE = SIZE // bsize
screen = pg.display.set_mode((SIZE, SIZE))
screen.fill((255, 255, 255))
pg.display.set_caption("py_bytefall")
x, y = 0, 0
rectlist = deque() # alright chatgpt helped me with this one, this data struct is more efficient for value access
for color in colbytes:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if x == GRID_SIZE:
        x = 0
        y += bsize
        pg.display.flip()
        pg.time.delay(int(delay)) # pygame has its own delay builtin, no need for sleep, also prevents window handling bugs
    if y >= SIZE:
        screen.fill((255, 255, 255))
        new_rectlist = deque()
        for rx, ry, rc in rectlist:
            if ry > 0:
                ny = ry - bsize
                pg.draw.rect(screen, rc, (rx, ny, bsize, bsize))
                new_rectlist.append((rx, ny, rc))
        rectlist = new_rectlist
        y -= bsize
    px = x * bsize
    pg.draw.rect(screen, color, (px, y, bsize, bsize))
    rectlist.append((px, y, color))
    x += 1
input("Done. Press ENTER to exit.")
pg.quit()
sys.exit()
