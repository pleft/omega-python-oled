import OledLib as OL
from OmegaExpansion import oledExp
from random import randint
import time
import OmegaGameResources as OGR

def detectCollision(x, y, block):
    blockWidth= len(block[0])
    blockHeight = len(block)
    for i in range(blockWidth):
        for j in range(blockHeight):
            if block[j][i]>0 and playfield[y][x+i] == 1:
                print("collision")
                return True
    if y>1:
        blank = [[0 for i in range(len(block[0]))] for j in range(1)]
        OL.bitmapBlit(x, y-1, blank)
    OL.bitmapBlit(x, y, block)
    return False

squareBlock = OGR.getTile(0, 0)
highBlock = OGR.getTile(0, 1)
leftBlock = OGR.getTile(0, 2)
rightBlock = OGR.getTile(0, 3)
leftZigZagBlock = OGR.getTile(0, 4)
rightZigZagBlock = OGR.getTile(0, 5)

blocks = [squareBlock, highBlock, leftBlock, rightBlock, leftZigZagBlock, rightZigZagBlock]

OL.init()

speed = 8
frames = 0
y = 0
x = (OL.OLED_WIDTH-1)/2
playfield = [[0 if j < OL.OLED_HEIGHT-1 else 1 for i in range(OL.OLED_WIDTH)] for j in range(OL.OLED_HEIGHT)]
block = blocks[0]

OL.putBitmap(0, 0, playfield)
OL.blit()

while True:
    if y==0:
        block = blocks[randint(0,len(blocks)-1)]
    y = y + 1 if y<OL.OLED_HEIGHT-1 else 0 if y>=OL.OLED_HEIGHT-1 else y
    collision = detectCollision(x, y, block)
    if collision:
        y = 0
    frames += 1


