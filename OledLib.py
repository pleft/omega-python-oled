from OmegaExpansion import oledExp
from OmegaExpansion import onionI2C
import time

OLED_EXP_ADDR = 0x3C
OLED_EXP_REG_DATA = 0x40
OLED_I2C_MAX_BUFFER = 32

i2c = onionI2C.OnionI2C()

oledExp.driverInit()
oledExp.setImageColumns()
oledExp.setMemoryMode(0)

rowSize=8
rows=8
width=128
height=rowSize*rows

pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
compactbuffer=[[0 for i in range(width)] for j in range(rows)]

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def putPixel(x, y):
	pagebuffer[(y/rowSize)%rows][x*rowSize+y%rows] = 1
	byte = 0
	for j in range(rowSize-1, -1, -1):                    
		byte = (byte << 1) | pagebuffer[(y/rowSize)%rows][x*rowSize+j]
	compactbuffer[(y/rowSize)%rows][x] = byte

def putBitmap(x, y, bitmap):
	height = len(bitmap)
	width = len(bitmap[0])
	for i in range(width):
		for j in range(height):
			if bitmap[j][i] == 1:
				putPixel(x+i, y+j)

def blit():
	""" Blits the framebuffer to screen at maximum fast rate """
	start = int(round(time.time() * 1000))
        global compactbuffer
        page = 0
        while page < rows:
                count = 0
                while count < width:
			bytes=[compactbuffer[page][count+i] for i in range(OLED_I2C_MAX_BUFFER)]
			i2c.writeBytes(OLED_EXP_ADDR, OLED_EXP_REG_DATA, bytes)
                        count += OLED_I2C_MAX_BUFFER
                page += 1
        #after blitting to screen, clear the pagebuffer
        pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
	compactbuffer=[[0 for i in range(width)] for j in range(rows)]
	end = int(round(time.time() * 1000))
	print("blit() took: " + str(end-start) )
