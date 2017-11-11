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

def clearBuffers():
	""" clear the framebuffers (all elements to 0) """
	global pagebuffer, compactbuffer
	pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
	compactbuffer=[[0 for i in range(width)] for j in range(rows)]

def putPixel(x, y):
	""" puts a pixel to x, y coordinates """
	global pagebuffer, compactbuffer
	pagebuffer[(y/rowSize)%rows][x*rowSize+y%rows] = 1
	byte = 0
	for j in range(rowSize-1, -1, -1):                    
		byte = (byte << 1) | pagebuffer[(y/rowSize)%rows][x*rowSize+j]
	compactbuffer[(y/rowSize)%rows][x] = byte

def clearPixel(x, y):
	""" clears the pixel of x, y coordinates """
	global pagebuffer, compactbuffer
	pagebuffer[(y/rowSize)%rows][x*rowSize+y%rows] = 0
	byte = 0
	for j in range(rowSize-1, -1, -1):                    
		byte = (byte << 1) | pagebuffer[(y/rowSize)%rows][x*rowSize+j]
	compactbuffer[(y/rowSize)%rows][x] = byte

def putRectangle(x, y, width, height, fill):
	""" 
	Puts a rectangle (width x height) at the specified x, y coordinates.
	Setting 'fill' to True will fill the rectangle, 
	where False will draw just the borders 
	"""

	if fill:
		for i in range(width):
			for j in range(height):
				putPixel(x + i, y + j)
	else :
		for i in range(width):
			putPixel(x + i, y)
			putPixel(x + i, y + height-1)
		for j in range(height):
			putPixel(x, y + j)
			putPixel(x + width-1, y + j)

def putBitmap(x, y, bitmap):
	""" puts a bitmap MxN array of 0s and 1s to x, y coordinates """
	height = len(bitmap)
	width = len(bitmap[0])
	for i in range(width):
		for j in range(height):
			if bitmap[j][i] == 1:
				putPixel(x+i, y+j)
			else:
				clearPixel(x+i, y+j)

def blit():
	""" Blits the whole framebuffer to screen at maximum fast rate """
	# start = int(round(time.time() * 1000))
        global compactbuffer, pagebuffer
        page = 0
        while page < rows:
                count = 0
                while count < width:
			bytes=[compactbuffer[page][count+i] for i in range(OLED_I2C_MAX_BUFFER)]
			i2c.writeBytes(OLED_EXP_ADDR, OLED_EXP_REG_DATA, bytes)
                        count += OLED_I2C_MAX_BUFFER
                page += 1
        #after blitting to screen, clear the pagebuffer
        clearBuffers()
	# end = int(round(time.time() * 1000))
	# print("blit() took: " + str(end-start) )

def dma(x, y, bitmap):
	""" 
	Direct Memory Access to blit a specific bitmap in x, y coordinates leaving everyting else on-screen untouched.
	Extremely fast but prone to bugs
	"""
	start = int(round(time.time() * 1000))
	global compactbuffer, pagebuffer
	height = len(bitmap)
	width = len(bitmap[0])
	putBitmap(x, y, bitmap)
	page = (y/rowSize)%rows
	maxPage = page + (height/rowSize)%rows
	# print("page: " + str(page))
	# print("maxPage: " + str(maxPage) + " ... " +str((height/rowSize)%rows))
	while page < maxPage+1:
		count = 0
		while count < width:
			byte = compactbuffer[page][count+x]
			pixel = count+x
			# print(str(pixel) + ", " + str(page) + ", byte: " + bin(byte))
			oledExp.setCursorByPixel(page, pixel)
			oledExp.writeByte(byte)
			count += 1
		page += 1
	# clearBuffers()
	end = int(round(time.time() * 1000))
	# print("dma() took: " + str(end-start) )

def dmaClear(x, y, width, height):
	emptybitmap=[[0 for i in range(width)] for j in range(height)]
	dma(x, y, emptybitmap)
