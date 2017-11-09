from OmegaExpansion import oledExp

oledExp.setImageColumns()

oledExp.driverInit()
oledExp.setMemoryMode(0)

rowSize=8
rows=8
width=128
height=rowSize*rows

pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def putPixel(x, y):
	pagebuffer[(y/rowSize)%rows][x*rowSize+y%rows] = 1
	return

def drawLine(startX, startY, endX, endY):
	return

def blit():
	page = 0
	while page < rows:
		count = 0
		while count < width*rowSize:
			byte = 0b00000000
			for j in range(rowSize-1, -1, -1):
				byte = (byte << 1) | pagebuffer[page][count+j]
			oledExp.writeByte(byte)
			count += rowSize
		page += 1
	end = int(round(time.time() * 1000))	
	return

# for i in range(width):
# 	putPixel(i, 0)
# 	putPixel(i, height -1)
# for j in range(height):
# 	putPixel(0, j)
# 	putPixel(width - 1, j)

for i in range(width):
	for j in range(height):
		putPixel(i, j)

blit()
