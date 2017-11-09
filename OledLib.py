from OmegaExpansion import oledExp
import time

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
	return

def drawLine(startX, startY, endX, endY):
	
	return

def blit():
	start = int(round(time.time() * 1000))
        global pagebuffer
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
        #after blitting to screen, clear the pagebuffer
        pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
	end = int(round(time.time() * 1000))
	print("blit() took: " + str(end-start) )
        return

def blit2():
	start = int(round(time.time() * 1000))
	global pagebuffer
	page = 0
	while page < rows:
		count = 0
		while count < width*rowSize:
			byte = 0b00000000
			for j in range(rowSize-1, -1, -1):
				byte = (byte << 1) | pagebuffer[page][count+j]
			if byte > 0b00000000:
				pixel = count/rowSize
				oledExp.setCursorByPixel(page, pixel)
				oledExp.writeByte(byte)
			count += rowSize
		page += 1
	#after blitting to screen, clear the pagebuffer
	pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
	end = int(round(time.time() * 1000))                               
        print("blit2() took: " + str(end-start) )  
	return

def blit3():                                  
        start = int(round(time.time() * 1000))
        global compactbuffer      
	    global pagebuffer               
        page = 0                              
        while page < rows:                  
                count = 0                                 
                while count < width:                                  
                        byte = compactbuffer[page][count]
                        if byte > 0b00000000:                                 
                                pixel = count                      
                                oledExp.setCursorByPixel(page, pixel)
                                oledExp.writeByte(byte)              
                        count += 1                                   
                page += 1                                                  
        #after blitting to screen, clear the pagebuffer                    
        pagebuffer=[[0 for i in range(width*rowSize)] for j in range(rows)]
        compactbuffer=[[0 for i in range(width)] for j in range(rows)]
	    end = int(round(time.time() * 1000))                               
        print("blit3() took: " + str(end-start) )                          
        return
