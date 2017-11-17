import OledLib

for i in range(10):
	OledLib.putRectangle(5 + i*2, 5 + i*2, 4*i, 4*i, False)
	OledLib.putRectangle(OledLib.OLED_WIDTH - 30 - (10-i)*2, 5 + i*2, 4*(10-i), 4*(10-i), False)
OledLib.blit()
