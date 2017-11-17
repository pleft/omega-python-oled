import OledLib
from OmegaExpansion import oledExp
from random import randint
import time

bitmap = [
    [[1 for i in range(64)] for j in range(64)],
    [[1 for i in range(32)] for j in range(32)], 
    [[1 for i in range(24)] for j in range(24)],
    [[1 for i in range(16)] for j in range(16)],
    [[1 for i in range(8)] for j in range(8)],
    [[1 for i in range(4)] for j in range(4)],
    [[1 for i in range(2)] for j in range(2)],
    [[1 for i in range(1)] for j in range(1)]
    ]

for i in range(len(bitmap)):
    translated = OledLib.translateBitmap(bitmap[i])
    oledExp.clear()
    w = len(bitmap[i][0])
    h = len(bitmap[i])
    oledExp.write("Bitmap bliting size: " + str(w) + "x" + str(h))
    time.sleep(2)
    oledExp.clear()
    frames = 0
    exampleStart = int(round(time.time() * 1000))
    for i in range(200):
        x = randint(0, OledLib.OLED_WIDTH-1-w) if OledLib.OLED_WIDTH>w else 0
        y = randint(0, OledLib.OLED_HEIGHT-1-h) if OledLib.OLED_HEIGHT>h else 0
        # print("x: " + str(x) + ", y: " + str(y)) 
        OledLib.bitmapBlit(x, y, translated)
        frames += 1
    exampleEnd = int(round(time.time() * 1000))
    millis = exampleEnd - exampleStart
    time.sleep(1)
    oledExp.clear()
    oledExp.write("FPS: " + str(frames*1000/float(millis)))
    time.sleep(2)